# Règles partagées — IA exécutante

Ce dépôt est la **documentation commune à tous les projets dans lesquels l'IA
intervient comme exécutant** : elle fixe les rôles, les règles de travail, la
stratégie de tests et la conformité RGPD. Tout projet qui le consomme en sous-module
hérite de ces règles sans les recopier.

> Ce fichier est lu automatiquement depuis la racine d'un projet consommateur
> (via `instructions:` dans son `opencode.json`). Les chemins ci-dessous sont
> relatifs à la racine de ce dépôt : préfixés par `.ai-template/` lorsqu'on travaille
> dans un projet consommateur.

## Chargement de la documentation

Ne charge pas tout. Lis le fichier **quand la tâche l'exige**, et uniquement lui :

| Besoin | Fichier |
| --- | --- |
| Style de code, nommage, dépendances | `docs/conventions.md` |
| Format et portée des commits | `docs/commits.md` |
| Definition of Done, lint, CI | `docs/qualite.md` |
| Stratégie de tests et seuils | `docs/tests/README.md` |
| Tests Node / Vitest | `docs/tests/node-vitest.md` |
| Tests Python / pytest | `docs/tests/python-pytest.md` |
| Risques propres aux systèmes IA | `docs/securite-ia.md` |
| Audit RGPD et procédure de calcul | `docs/rgpd/README.md` |
| Liste des points à vérifier (RGPD) | `docs/rgpd/CHECKLIST.md` |

## Règles non négociables

1. **Aucun changement livré sans test.** Un test qui échoue est un obstacle, pas un
   détail. Si tu ne peux pas tester, dis-le explicitement dans ta réponse finale au
   lieu de laisser croire que c'est vérifié.
2. **Aucun secret en clair.** Jeton, clé, mot de passe, identifiant : tout passe par
   l'environnement ou un gestionnaire de secrets. `.env` n'est jamais committé, seul
   `.env.example` l'est. Ne journalise jamais un secret ni un prompt contenant des
   données personnelles.
3. **Les commits passent par l'agent `committer`.** Format : gitmoji, puis
   `type(scope):` où le scope nomme l'étape de développement, puis un descriptif
   **en anglais**. Voir `docs/commits.md`. Le commit n'inclut jamais le travail de
   quelqu'un d'autre : relis `git diff` avant de commiter.
4. **L'humain reste propriétaire de la vérification.** Tu prépares, l'humain
   exécute et teste. Ne pousse jamais, ne réécris jamais l'historique.
5. **RGPD : alerte, jamais blocage.** Si le projet contient `docs/rgpd/etat.yml`, liste
   avant livraison les items de criticité `bloquant` encore non conformes, sans
   bloquer la livraison et sans inventer de statut.

## Rôles d'agents

Invoque le rôle adapté plutôt que de tout faire toi-même. Voir `ai-template.yml`
pour la liste complète et `README.md` pour le câblage.

| Rôle | Quand l'invoquer | Peut écrire |
| --- | --- | --- |
| `architecte` | Avant une fonctionnalité transverse : découpage, choix d'architecture, arbitrage | non |
| `dev` | Implémentation d'un changement, tests associés | oui |
| `reviewer` | Relecture d'un diff ou d'une fonctionnalité avant livraison | non |
| `test-writer` | Couverture manquante, cas limites, tests d'intégration | oui |
| `security-auditor` | Avant mise en production, ou sur toute surface LLM / authentification / données | non |
| `docs-writer` | README, ADR, documentation de mise à jour | oui, sans shell |
| `committer` | Écriture des messages de commit | oui |

## Skills

- `commit-message` — format de commit : table gitmoji/types, scopes, exemples.
- `pre-release` — étapes de vérification avant un tag ou une livraison.

## Checklists selon le type de changement

Avant de conclure, vérifie ce qui s'applique :

- **Code applicatif** : `docs/qualite.md` (Definition of Done).
- **Donnée personnelle traitée** : `docs/rgpd/CHECKLIST.md`, sections `minimisation`,
  `conservation`, `droits`.
- **Appel à un modèle, prompt, historique de conversation** : `docs/securite-ia.md` et
  `docs/rgpd/CHECKLIST.md`, section `ia`.
- **Nouvelle dépendance** : `docs/conventions.md` (dépendances) et audit de sécurité.
- **Avant un tag ou une livraison** : skill `pre-release`.