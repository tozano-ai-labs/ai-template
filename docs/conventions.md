# Conventions

Règles de code communes. Elles s'appliquent par défaut à tout projet consommant ce
dépôt ; un projet peut s'en écarter, mais l'écart doit être écrit dans son `AGENTS.md`.

## Principe directeur

**Le code est lu beaucoup plus souvent qu'il n'est écrit.** Écriver moins, écrire
clair. Un nom explicite vaut mieux qu'un commentaire. Une duplication courte vaut
mieux qu'une abstraction incorrecte.

## Structure

- Le code vit dans des modules qui font une chose. Un fichier qui exceed ~300 lignes ou
  qui porte deux verbes différents (« parse et envoie ») doit être scindé.
- Les fonctions sont courtes et font une seule chose. early return plutôt que
  cascade de conditions.
- Pas de dépendance circulaire. Si deux modules se connaît mutuellement, il manque un
  troisième module.
- Le code mort est supprimé, pas commenté. Un commentaire « à utiliser plus tard » est
  une dette sans échéance.

## Nommage

| Élément | Règle |
| --- | --- |
| Fichiers | `kebab-case` (`gestion-session.ts`), aligné sur la convention en place |
| Types, classes, composants | `PascalCase` |
| Fonctions, variables | `camelCase` |
| Constantes | `UPPER_SNAKE_CASE` |
| Booléens | `is`, `has`, `can`, `should` en tête |
| Tests | le nom décrit le comportement attendu, en français ou en anglais selon le projet |

Nomme les choses d'après leur **rôle**, pas leur type : `connexion_ollama` plutôt que
`objet_client`. Un nom qui doit être commenté pour être compris est un mauvais nom.

## Commentaire

- Un commentaire explique **pourquoi**, jamais **quoi**.
- Pas de code commenté.
- Pas de commentaire qui répète l'identifiant : `// compte les tokens` au-dessus de
  `countTokens()` est du bruit.
- Un TODO porte un propriétaire et une échéance, ou c'est une tâche dans le suivi.

## Gestion d'erreur

- On n'attrape que ce qu'on sait traiter. Un `catch` qui ne fait que logger et
  réémettre est inutile.
- Les erreurs portent un contexte : ce qui échoue, sur quelle entrée.
- Aucun secret, aucune donnée personnelle, aucun prompt dans un message d'erreur ou un
  journal. Voir `securite-ia.md`.
- Les erreurs envoyées au client sont génériques ; le détail reste côté serveur.

## Dépendances

Avant d'ajouter une dépendance :

1. le standard library ne suffit vraiment pas ? c'est le seul motif acceptable ;
2. le paquet est maintenu et compatible avec la version du projet ;
3. ce qu'il apporte est proportionné à ce qu'il coûte en surface d'attaque ;
4. une dépendance de production n'est jamais utilisée dans un outil de développement
   au moment de l'exécution, ni l'inverse.

Épingler les versions en production. Une dépendance de sécurité et de disponibilité doit
être vue comme du code tiers non relu.

## Contrôle de version

- Un changement = un commit, voir [`commits.md`](commits.md).
- Ne jamais committer de secret ni de `.env`.
- Le formatage global est un commit à part, jamais mélangé à une fonctionnalité.

## Typage

Si le projet est typé : le typage strict est preferable, les `any` sont interdits dans le
code applicatif, et un `unknown` se réduit explicitement. Dans un projet non typé, on
documente les formes de données aux frontières : entrée d'API, sortie de modèle, fichier
de configuration.