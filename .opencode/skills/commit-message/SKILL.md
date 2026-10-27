---
name: commit-message
description: Use when writing or reviewing a git commit message in a project using ai-template. Formats the message as gitmoji first, then type(scope) where scope names the development step or module, then a descriptive subject in English. Triggers on "commit", "commite", "message de commit", "gitmoji", "conventional commit".
---

# Format de commit

Source de vérité du format de commit des projets qui consomment ce dépôt.
L'agent `committer` l'applique ; l'humain relit et pousse.

## Structure

```text
<gitmoji> <type>(<scope>): <description>

<corps facultatif — pourquoi, en anglais>
```

- **gitmoji en premier élément**, une seule espace avant la suite.
- `type(scope):` — le **scope nomme l'étape du développement** ou le module touché.
- Description **en anglais**, à l'impératif, sans point final, **72 caractères max**.
- Corps facultatif : explique **pourquoi**, pas quoi. Trois lignes maximum.
- Signe de rupture au-delà du corps : deux lignes vides en Markdown, une seule dans un
  message git.

## Exemples

```text
✨ feat(stream): render tokens as they arrive

The chat view buffered the whole response before painting, which made long
completions look frozen for several seconds. Tokens are now appended as each
NDJSON chunk is received.
```

```text
🐛 fix(models): drop empty model list when Ollama has no tag

/api/models returned [] with a 200 status, which the UI rendered as an empty
dropdown instead of an error message.
```

```text
🔒 security(rgpd): stop logging raw prompts

Conversation prompts can contain personal data. They are now hashed in the
access log before being written.
```

## Table gitmoji ↔ type

| Gitmoji | Type | Quand |
| --- | --- | --- |
| ✨ | `feat` | nouvelle fonctionnalité visible par l'utilisateur |
| 🐛 | `fix` | correction de bug |
| 📚 | `docs` | documentation uniquement |
| ♻️ | `refactor` | réorganisation **sans** changement de comportement |
| ✅ | `test` | ajout ou correction de tests |
| 🔧 | `chore` | outillage, configuration, mise à jour de dépendance |
| ⚡ | `perf` | gain de performance mesuré |
| 🎨 | `style` | formatage, CSS, mise en forme d'interface |
| 📦 | `build` | système de build, empaquetage, dépendances de build |
| 🚑 | `ci` | pipeline d'intégration continue, configuration CI |
| 🔒 | `security` | correctif ou durcissement lié à la sécurité ou aux données personnelles |
| ⏪ | `revert` | annulation d'un changement précédent |
| 🧪 | `test` | mise en place d'un test qui ne passe pas encore |
| 🌐 | `i18n` | traduction, formatage régional |
| 🔊 | `logs` | ajout ou correction de journaux |

## Scopes recommandés

Le scope désigne l'étape du développement ou le module. On ne met pas le nom d'une
branche, ni d'une personne.

| Scope | Désigne |
| --- | --- |
| `api` | la couche HTTP ou le contrat d'API |
| `ui` | l'interface |
| `stream` | le streaming temps réel |
| `deps` | les dépendances |
| `build` | la chaîne de build |
| `docker` | les conteneurs et l'orchestration |
| `ia` | la couche modèle, prompts, appels LLM |
| `rgpd` | le traitement de données personnelles |
| `docs` | la documentation |

Si aucun scope ne convient, un scope libre mais court vaut mieux qu'un scope absent.

## Règles de rédaction

1. **Anglais uniquement**, même dans un projet dont la documentation est en français.
   L'historique doit rester lisible et partageable.
2. **Imparfait ou impératif** : `add`, `fix`, `remove` — jamais `added`, `fixes`.
3. **Une seule idée par commit.** Deux sujets = deux commits.
4. **Le corps répond à « pourquoi ».** Le quoi est déjà dans le diff.
5. **Jamais de point final** sur la ligne de sujet.
6. **Jamais de secret, de `.env`, de fichier généré** dans un commit.
7. **Pas de message automatique de type « mise à jour de dépendances »** sans détail :
   nomme la dépendance et la raison.

## Points de contrôle avant commit

- `git diff --staged` contient-il uniquement ce qui est annoncé ?
- Le message décrit-il exactement ce que fait le diff ?
- Le type est-il exact ? `refactor` qui change un comportement = `feat` ou `fix`.
- Le scope désigne-t-il bien une étape de développement ?
- Le sujet tient-il en 72 caractères ?
- Y a-t-il un secret ou une donnée personnelle dans le diff ?

## Périmètre de l'agent `committer`

`git add` et `git commit` sont autorisés. `git push`, `git reset`, `git rebase`,
`git clean`, `git checkout`, `git switch` et `git commit --amend` sont refusés.
Raison : le développeur garde la maîtrise de la livraison et **doit tester son propre
code** plutôt que de déléguer à l'IA la totalité d'une tâche de développement simple.
Voir `docs/commits.md`.