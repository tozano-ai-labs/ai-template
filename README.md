# ai-template

**Documentation commune à tous les projets dans lesquels l'IA intervient comme
exécutant.**

Ce dépôt n'est pas une bibliothèque. C'est le socle de règles, de rôles et de
méthode qu'un projet **référence** au lieu de les réécrire : rôles d'agents, règles de
travail, stratégie de tests, checklist RGPD, format de commit.

Un projet l'intègre en **sous-module git**, ce qui lui donne les fichiers sur disque,
une version verrouillée et un historique synchronisé avec le sien. Le sous-module
résout un commit précis : deux personnes qui travaillent sur deux projets ne peuvent
pas se retrouver avec des règles différentes sans que ça se voie dans `git status`.

## Sommaire

- [Ce que contient ce dépôt](#ce-que-contient-ce-dépôt)
- [Installation dans un projet](#installation-dans-un-projet)
- [Câblage d'opencode](#câblage-dopencode)
- [Gérer les versions](#gérer-les-versions)
- [Les sept rôles](#les-sept-rôles)
- [Les compétences](#les-compétences)
- [La checklist RGPD](#la-checklist-rgpd)
- [Mettre à jour le template](#mettre-à-jour-le-template)
- [Dépannage](#dépannage)

## Ce que contient ce dépôt

```text
ai-template/
├── AGENTS.md                     règles partagées, chargées automatiquement
├── ai-template.yml               manifeste : version, profils, rôles, checklists
├── CHANGELOG.md                  versions SemVer
├── .opencode/
│   ├── agents/                   les sept rôles
│   └── skills/                   compétences chargées à la demande
├── docs/
│   ├── conventions.md            style de code, nommage, dépendances
│   ├── commits.md                format de commit, périmètre de l'agent
│   ├── qualite.md                Definition of Done, seuils, intégration continue
│   ├── securite-ia.md            injections de prompt, secrets, fournisseurs
│   ├── tests/                    stratégie, Vitest, pytest
│   └── rgpd/                     checklist, mode d'emploi, modèle d'état
├── scripts/generate-checklist.py  génère la checklist — usage rédaction
└── templates/                    fichiers à copier dans un projet
```

## Installation dans un projet

Prérequis : le projet est un dépôt git.

```bash
cd /chemin/vers/le-projet

# 1. Référencer ce dépôt sur sa branche
git submodule add -b main https://github.com/tozano-ai-labs/ai-template.git .ai-template

# 2. Faire découvrir les agents au projet
mkdir -p .opencode
ln -s ../.ai-template/.opencode/agents .opencode/agents

# 3. Partir des modèles
cp .ai-template/templates/AGENTS.md.projet AGENTS.md
cp .ai-template/templates/ai-template.json ai-template.json
mkdir -p docs/rgpd .github/workflows
cp .ai-template/docs/rgpd/modele-etat.yml docs/rgpd/etat.yml

# 4. Déclarer les versions dans .gitmodules, une fois pour toutes
git config -f .gitmodules submodule.ai-template.branch main

git add .gitmodules .ai-template .opencode AGENTS.md ai-template.json docs/rgpd .github
git commit -m "🔧 chore(deps): add ai-template submodule"
```

Le modèle de pipeline CI est à choisir selon la pile :

```bash
cp .ai-template/templates/github-ci-node.yml .github/workflows/ci.yml    # Node
cp .ai-template/templates/github-ci-python.yml .github/workflows/ci.yml  # Python
```

Puis personnaliser : `AGENTS.md` (commandes, langue, règles propres),
`ai-template.json` (profils actifs), et `docs/rgpd/etat.yml` (audit).

## Câblage d'opencode

`opencode.json` du projet — ou `.opencode/opencode.json`. Le fragment complet est dans
[`templates/opencode.json.projet`](templates/opencode.json.projet).

```jsonc
{
  "instructions": [
    "AGENTS.md",                    // règles propres au projet, en priorité
    ".ai-template/AGENTS.md",       // règles partagées
    ".ai-template/docs/**/*.md"     // documentation, à la demande
  ],
  "skills": {
    "paths": [".ai-template/.opencode/skills"]
  }
}
```

Deux détails qui ne sont pas évidents :

- **`skills.paths` est obligatoire.** opencode ne scanne pas les sous-modules de
  lui-même : sans cette ligne, les compétences existent sur le disque mais ne sont
  jamais chargées.
- **`instructions` s'ajoute à `AGENTS.md`, il ne le remplace pas.** Le fichier du
  projet est lu en priorité ; les règles communes viennent s'y ajouter. Un projet peut
  donc assouplir une règle commune, mais l'écart doit être écrit dans son `AGENTS.md`.

Redémarrer opencode après toute modification : la configuration n'est pas rechargée à
chaud.

## Gérer les versions

La version du template est un **tag git** de ce dépôt, suivant le SemVer. La version
réellement utilisée par un projet est le **commit résolu de son sous-module** — c'est
ça qui garantit que tout le monde travaille avec les mêmes règles.

| Opération | Commandes |
| --- | --- |
| Voir la version en cours | `git -C .ai-template describe --tags` |
| Voir la version attendue | lire `version_attendue` dans `ai-template.json` |
| Épingler une version | voir ci-dessous |
| Passer à la branche `main` | `git submodule update --remote .ai-template` |

### Épingler une version

```bash
git -C .ai-template fetch --tags
git -C .ai-template checkout v1.0.0
git add .ai-template
git commit -m "🔧 chore(deps): pin ai-template to v1.0.0"
```

Le commit du sous-module est alors enregistré dans le projet : les collaborateurs, la
CI et le clone distant reçoivent exactement les mêmes règles.

### Conséquence pratique

Une version n'existe pas tant que le tag n'est pas créé. Tant que ce dépôt est en
`[Non publié]` dans [`CHANGELOG.md`](CHANGELOG.md), `version_attendue` dans
`ai-template.json` est déclaratif : `git -C .ai-template describe --tags` renverra
`main-<sha>` plutôt qu'un numéro. Créer le tag `v1.0.0` est une décision à prendre
explicitement.

## Les sept rôles

Invoqués par opencode, directement ou par `@nom`.

| Rôle | Ce qu'il fait | Écrit |
| --- | --- | --- |
| `architecte` | Découpe une fonctionnalité transverse, arbitre, rédige les ADR | non |
| `dev` | Implémente, écrit les tests, signale les points RGPD bloquants | oui |
| `reviewer` | Relit un diff : bugs, régressions, tests manquants | non |
| `test-writer` | Écrit les tests manquants, couvre les cas limites | oui |
| `security-auditor` | Audite la sécurité : entrées non fiables, secrets, surface LLM | non |
| `docs-writer` | Rédige et tient à jour README, ADR, guides | oui, sans shell |
| `committer` | Rédige et crée les commits, au format du dépôt | oui |

Définitions complètes : [`.opencode/agents/`](.opencode/agents/). Les permissions sont
déclarées dans l'en-tête de chaque fichier.

### Pourquoi l'agent `committer` ne pousse jamais

C'est un choix, pas une limite technique. L'IA écrit le code ; la personne qui le
livre doit l'avoir lu et testé. Autoriser un `git push` automatique retirerait de la
boucle le seul moment où cette vérification peut encore avoir lieu. L'agent rend
l'historique lisible, il ne l'authentifie pas. Voir [`docs/commits.md`](docs/commits.md).

## Les compétences

Chargées automatiquement par opencode quand le sujet s'y prête.

| Compétence | Déclencheur | Effet |
| --- | --- | --- |
| `commit-message` | « commit », « message de commit », « gitmoji » | table gitmoji/types, scopes, points de contrôle |
| `pre-release` | « release », « livrer », « créer un tag » | lint, tests, couverture, secrets, changelog, alerte RGPD |

## La checklist RGPD

84 points répartis en 13 sections : finalités, bases légales, consentement,
minimisation, conservation, destinataires, transferts, droits, sécurité, cookies,
violations, gouvernance, et une section **systèmes IA**.

- [`docs/rgpd/CHECKLIST.md`](docs/rgpd/CHECKLIST.md) — les points à vérifier, en
  lecture directe.
- [`docs/rgpd/README.md`](docs/rgpd/README.md) — méthode, statuts, calcul de la
  progression.
- `docs/rgpd/etat.yml` dans le projet — l'état, qui n'appartient qu'à lui.

Chaque point porte une question, la preuve attendue, une criticité et les articles
visés :

| Criticité | Sens |
| --- | --- |
| `bloquant` | à corriger avant mise en production |
| `important` | à corriger ou à justifier par écrit |
| `recommande` | bonne pratique, sans risque immédiat |

**Un point bloquant non conforme n'empêche pas la livraison.** Il est signalé avant
livraison, et la décision reste humaine.

### Modifier la checklist

`docs/rgpd/checklist.yml` est la source ; `CHECKLIST.md` est généré :

```bash
python3 scripts/generate-checklist.py           # régénère
python3 scripts/generate-checklist.py --check   # échoue si désynchronisé
```

Après modification, incrémenter `meta.version`, ajouter une entrée au `CHANGELOG.md`,
et ne **jamais renuméroter un identifiant** : un `RGPD-IA-08` doit désigner le même
point dans tous les projets, pour que leur état reste valide.

## Mettre à jour le template

```bash
git submodule update --remote .ai-template     # suit la branche
git -C .ai-template fetch --tags
git -C .ai-template log --oneline main..v1.1.0   # ce qui arrive
git -C .ai-template checkout v1.1.0
```

Puis, dans le projet : reporter la nouvelle version dans `ai-template.json`, relire les
points RGPD nouvellement ajoutés dans `docs/rgpd/CHECKLIST.md` — ils apparaîtront
`a_verifier`, ce qui est le bon comportement —, et committer.

## Dépannage

**Les agents n'apparaissent pas dans la liste `@`.**
Le lien symbolique n'est pas bon, ou il pointe dans le vide :

```bash
ls -l .opencode/agents
readlink -f .opencode/agents
```

Si opencode ne suit pas le lien au niveau du répertoire, lier les fichiers un par un :

```bash
mkdir -p .opencode/agents
for f in .ai-template/.opencode/agents/*.md; do
  ln -sf "../../.ai-template/.opencode/agents/$(basename "$f")" ".opencode/agents/$(basename "$f")"
done
```

**Les compétences ne sont jamais chargées.**
`skills.paths` manque dans `opencode.json`, ou le chemin est faux. Vérifier que
`.ai-template/.opencode/skills/commit-message/SKILL.md` existe.

**Les modifications de configuration n'ont aucun effet.**
opencode charge sa configuration au démarrage. Quitter et relancer la session.

**Le sous-module est vide après un clone.**

```bash
git submodule update --init --recursive
```

**Un repo cassé empêche opencode de démarrer.**
`OPENCODE_DISABLE_PROJECT_CONFIG=1 opencode` ignore la configuration du projet ;
`OPENCODE_CONFIG=/chemin/vers/autre.json opencode` en charge une autre.

## Périmètre

Outil de travail, pas un avis juridique. La checklist RGPD couvre les points courants
d'un projet numérique avec intelligence artificielle ; elle ne remplace pas une analyse
particulière lorsque le contexte l'exige — données sensibles, personnes vulnérables,
décision automatisée à effet juridique.

## Version

`1.0.0` déclarée dans [`ai-template.yml`](ai-template.yml), **non encore publiée** :
aucun tag n'existe. Voir « Gérer les versions ».