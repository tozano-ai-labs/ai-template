#!/usr/bin/env python3
"""Génère docs/rgpd/CHECKLIST.md depuis docs/rgpd/checklist.yml.

Usage, depuis la racine du dépôt :

    python3 scripts/generate-checklist.py
    python3 scripts/generate-checklist.py --check

--check n'écrit rien : il sort en code 1 si le fichier généré diffère de la
source. À utiliser en revue pour détecter un CHECKLIST.md désynchronisé.

Ce script sert à la rédaction du template. Un projet consommateur n'a rien à
installer : il ne modifie jamais checklist.yml.
"""

import argparse
import pathlib
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML est requis : pip install pyyaml")

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "docs" / "rgpd" / "checklist.yml"
CIBLE = RACINE / "docs" / "rgpd" / "CHECKLIST.md"

CRITICITE = {
    "bloquant": "🔴 bloquant",
    "important": "🟠 important",
    "recommande": "🟡 recommandé",
}


def compter(items):
    total = len(items)
    bloquants = sum(1 for i in items if i["criticite"] == "bloquant")
    importants = sum(1 for i in items if i["criticite"] == "important")
    recommandes = sum(1 for i in items if i["criticite"] == "recommande")
    return total, bloquants, importants, recommandes


def rendre(donnees):
    meta = donnees["meta"]
    sections = donnees["sections"]
    items = [i for s in sections for i in s["items"]]
    total, bloquants, importants, recommandes = compter(items)

    lignes = [
        "# Checklist RGPD",
        "",
        "> **Fichier généré.** Source de vérité : [`checklist.yml`](checklist.yml).",
        "> Ne pas éditer ce fichier à la main : modifier le YAML puis régénérer avec",
        "> `python3 scripts/generate-checklist.py`.",
        "",
        f"Version {meta['version']} — {total} items : "
        f"{bloquants} bloquants, {importants} importants, {recommandes} recommandés.",
        "",
        "## Utilisation",
        "",
        "1. Lire [`README.md`](README.md) pour la méthode et les statuts.",
        "2. Examiner le projet et reporter le résultat dans `docs/rgpd/etat.yml` du",
        "   projet, jamais dans ce dépôt.",
        "3. Ne retenir un item comme `conforme` que si une preuve existe.",
        "",
        "Un item `bloquant` non conforme produit une alerte avant livraison ; il",
        "n'interdit pas la livraison. La décision reste humaine.",
        "",
        "## Sommaire",
        "",
        "| Section | Items | Dont bloquants |",
        "| --- | ---: | ---: |",
    ]

    for section in sections:
        section_items = section["items"]
        n, b, _, _ = compter(section_items)
        lignes.append(
            f"| [{section['titre']}](#{section['id'].replace('-', '')}) | {n} | {b} |"
        )

    lignes.append("")
    lignes.append("## Détail des items")
    lignes.append("")

    for section in sections:
        lignes.append(f'<a id="{section["id"].replace("-", "")}"></a>')
        lignes.append("")
        lignes.append(f"### {section['titre']}")
        lignes.append("")
        if section.get("intro"):
            lignes.append(f"> {section['intro'].strip()}")
            lignes.append("")
        lignes.append("| Item | Vérification | Preuve attendue | Criticité | Références |")
        lignes.append("| --- | --- | --- | --- | --- |")
        for item in section["items"]:
            question = item["question"].replace("|", "\\|")
            preuve = item["preuve"].replace("|", "\\|")
            criticite = CRITICITE[item["criticite"]]
            refs = ", ".join(item.get("refs", []))
            lignes.append(
                f"| `{item['id']}` | {question} | {preuve} | {criticite} | {refs} |"
            )
        lignes.append("")

    lignes.append("## Lexique")
    lignes.append("")
    for crit in donnees["criticites"]:
        lignes.append(f"- **{crit['libelle']}** — {crit['description']}")
    lignes.append("")
    lignes.append("Statuts possibles dans l'état du projet : "
                  + ", ".join(f"`{s['id']}`" for s in donnees["statuts"]) + ".")
    lignes.append("")
    lignes.append("---")
    lignes.append("")
    lignes.append("Outil de travail, pas un avis juridique. Voir la section « Portée »")
    lignes.append("de [`README.md`](README.md).")
    lignes.append("")

    return "\n".join(lignes)


def main():
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument(
        "--check",
        action="store_true",
        help="ne rien écrire, échouer si le fichier généré est désynchronisé",
    )
    args = parseur.parse_args()

    donnees = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    genere = rendre(donnees)

    if args.check:
        actuel = CIBLE.read_text(encoding="utf-8") if CIBLE.exists() else ""
        if actuel != genere:
            sys.exit(f"{CIBLE.relative_to(RACINE)} est désynchronisé : relancez le script.")
        print(f"{CIBLE.relative_to(RACINE)} est à jour.")
        return

    CIBLE.write_text(genere, encoding="utf-8")
    total = sum(len(s["items"]) for s in donnees["sections"])
    print(f"{CIBLE.relative_to(RACINE)} généré — {total} items.")


if __name__ == "__main__":
    main()