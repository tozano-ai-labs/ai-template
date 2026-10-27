# Audit RGPD — mode d'emploi

Cette checklist sert à **examiner un projet point par point**, pas à cocher des cases
en vitesse. Un item marqué conforme doit correspondre à une preuve vérifiable dans le
projet : une capture d'écran, un nom de fichier, une ligne de configuration. Une case
cochée sans preuve ne sert à rien le jour où la conformité est demandée.

## Les trois fichiers

| Fichier | Rôle | Modifiable par un projet ? |
| --- | --- | --- |
| `checklist.yml` | Source de vérité : les 13 sections et 84 items | non, c'est le template |
| `CHECKLIST.md` | Rendu lisible, généré depuis le YAML | non, généré |
| `etat.yml` | L'état du projet : un statut par item | **oui, c'est le fichier du projet** |

Un projet consommateur copie [`modele-etat.yml`](modele-etat.yml) vers
`docs/rgpd/etat.yml` et ne touche jamais aux deux premiers. Ainsi, une mise à jour du
template ne casse pas l'audit déjà réalisé.

## Statuts

| Statut | Signification |
| --- | --- |
| `a_verifier` | Item non encore examiné. Valeur par défaut. |
| `conforme` | La pratique observée correspond à l'exigence, avec une preuve. |
| `non_conforme` | L'exigence n'est pas remplie. Décrire l'écart. |
| `non_applicable` | Le projet ne traite pas ce point. Justifier brièvement. |

Un item ne passe pas directement à `conforme` : il passe par `non_conforme` le temps que
la correction soit en place. Cette trace montre ce qui a été corrigé, pas seulement
l'état final.

## Criticité

| Criticité | Rôle |
| --- | --- |
| `bloquant` | Risque élevé : exposition de données, absence de base légale, secret exposé. À traiter avant mise en production. |
| `important` | Conformité attendue : à corriger ou à justifier par écrit. |
| `recommande` | Bonne pratique, sans risque immédiat. |

**Un item bloquant non conforme n'empêche pas la livraison.** Il produit une alerte
listée avant livraison, et la décision reste humaine. Voir
[`../../AGENTS.md`](../../AGENTS.md) et la compétence `pre-release`.

## Remplir l'état

Dans `docs/rgpd/etat.yml`, un item reprend son identifiant, son statut et sa preuve :

```yaml
etat:
  RGPD-BL-01:
    statut: conforme
    note: "Chaque traitement a une base légale dans docs/rgpd/registre-traitements.md"
    preuve: "docs/rgpd/registre-traitements.md, colonne base légale"
    verifie_le: 2026-10-16
```

- `note` : pourquoi c'est conforme, ou ce qui manque.
- `preuve` : où l'on peut le constater dans le projet ou dans un document.
- `verifie_le` : date de la dernière vérification. Une preuve de six mois n'est plus
  une preuve.

## Méthode d'audit

1. **Lire le code avant le document.** Une politique de confidentialité décrit une
   intention ; seul le code décrit le traitement.
2. **Reconstruire les flux** : quelles données entrent, où elles vont, ce qui en est
   fait, ce qui est journalisé, ce qui est conservé.
3. **Examiner les points d'entrée** : formulaires, API, fichiers importés, paramètres
   d'URL, webhooks.
4. **Vérifier la preuve** de chaque item conforme. Un item sans preuve redevient
   `a_verifier`.
5. **Traiter la section `ia`** en dernier, ou dès qu'un appel à un modèle est
   identifié : elle conditionne plusieurs items des sections `minimisation`,
   `conservation` et `securite`.

## Calculer la progression

Aucun outil n'est fourni : le calcul se fait à la demande, et l'agent applique la
procédure suivante à partir de `checklist.yml` et `etat.yml`.

Pour chaque item `i`, on lit le statut correspondant dans `etat.yml` ; un item absent
vaut `a_verifier`.

```text
total        = nombre d'items de checklist.yml
examines     = items dont le statut est différent de a_verifier
conformes    = items au statut conforme
non_conf     = items au statut non_conforme
na           = items au statut non_applicable
restants     = total - examines

taux_examen      = examines / total × 100
taux_conformite  = conformes / (total - na) × 100
```

Le dénominateur de conformité exclut les items `non_applicable` : un projet qui ne
traite pas de cookies ne doit pas être pénalisé pour des cookies.

Pour le compte des bloquants, ne filtrer que sur `criticite: bloquant`, tous statuts
confondus :

```text
bloquants_total     = items de criticite bloquant
bloquants_resolus   = bloquants au statut conforme
bloquants_restants  = bloquants au statut different de conforme et de non_applicable
```

Un item `bloquant` `non_applicable` doit être justifié dans sa note : c'est une
décision, elle se documente.

Exemple de rapport :

```markdown
## RGPD — audit du 2026-10-16 (template 1.0.0)
Examinés : 41 / 84 (49 %)
Conformes : 34 / 81 (42 %)

Bloquants : 12 / 29 résolus
Restants : RGPD-FIN-04, RGPD-SEC-03, RGPD-IA-08
```

## Mise à jour du template

Quand le sous-module est mis à jour, de nouveaux items peuvent apparaître dans
`checklist.yml`. Ils sont absents de `etat.yml`, donc comptés `a_verifier` : le calcul
reste juste sans retouche. Les identifiants ne sont jamais renumérotés ni réutilisés,
pour qu'un état reste rattaché au bon item.

## Portée

Cette checklist est un outil de travail, pas un avis juridique. Elle couvre les points
courants d'un projet numérique avec intelligence artificielle. Elle ne remplace pas une
analyse requise dans un contexte particulier : données sensibles, sectoriel encadré,
décision automatisée à effet juridique, ou personnes concernées en situation de
vulnérabilité. Dans ces cas, faire appel à un professionnel.