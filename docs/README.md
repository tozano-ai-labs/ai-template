# Documentation partagée

Index des règles communes à tous les projets dans lesquels l'IA intervient comme
exécutant. Ne pas tout lire : ouvrir le fichier utile à la tâche en cours.

## Règles de fond

| Document | Contenu | À lire quand |
| --- | --- | --- |
| [`conventions.md`](conventions.md) | Style de code, nommage, structure, dépendances | Avant d'écrire du code dans un projet |
| [`commits.md`](commits.md) | Format de commit, périmètre de l'agent `committer` | Avant tout commit |
| [`qualite.md`](qualite.md) | Definition of Done, lint, formatage, intégration continue | Avant de livrer un changement |
| [`securite-ia.md`](securite-ia.md) | Risques propres aux systèmes IA : prompts, injections, fournisseurs | Dès qu'un modèle est appelé |
| [`tests/README.md`](tests/README.md) | Stratégie de tests, seuils de couverture | Avant d'écrire un test |
| [`tests/node-vitest.md`](tests/node-vitest.md) | Outillage Vitest, conventions de nommage, fixtures | Projet Node |
| [`tests/python-pytest.md`](tests/python-pytest.md) | Outillage pytest, fixtures, marquage | Projet Python |
| [`rgpd/README.md`](rgpd/README.md) | Comment utiliser la checklist et calculer la progression | Audit RGPD d'un projet |
| [`rgpd/CHECKLIST.md`](rgpd/CHECKLIST.md) | Liste des points à vérifier, par section | Audit RGPD, point par point |

## Raccourcis

- **Règles partagées** : [`AGENTS.md`](../AGENTS.md) à la racine du dépôt.
- **Rôles d'agents** : [`ai-template.yml`](../ai-template.yml) liste les sept rôles, leur
  mode et leur périmètre d'écriture.
- **Compétences** chargées par opencode depuis `.opencode/skills/`.

## Hiérarchie

En cas de conflit :

1. la documentation spécifique du projet (`AGENTS.md` de ce projet) ;
2. ce dépôt, via `.ai-template/AGENTS.md` ;
3. les conventions habituelles de l'agent.

Une règle projet peut donc assouplir une règle commune, mais l'expliciter : un
écart non écrit est un bug.