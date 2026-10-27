# Commits

## Pourquoi ce format existe

Un historique de commits est la documentation la plus consultée et la moins protégée
d'un projet. Il doit répondre à deux questions sans avoir à ouvrir le diff : **qu'est-ce
qui a changé**, et **pourquoi on l'a fait**.

Le format est donc volontairement rigide : gitmoji en premier élément pour une lecture
rapide, type standard pour un filtrage automatique, scope pour situer le changement,
message en anglais pour rester lisible par n'importe qui.

## Format

```text
<gitmoji> <type>(<scope>): <description>

<corps facultatif — pourquoi, en anglais>
```

```text
✨ feat(stream): render tokens as they arrive

The chat view buffered the whole response before painting, which made long
completions look frozen for several seconds. Tokens are now appended as each
NDJSON chunk is received.
```

Le détail operational — table des gitmoji, liste des scopes, points de contrôle — est
dans la compétence `commit-message`, qui est la source de vérité. Ce document fixe les
règles et l'intention.

## Règles

1. **Gitmoji en premier élément**, puis `type(scope):`, puis un descriptif **en
   anglais**.
2. Le **scope nomme l'étape du développement** ou le module touché : `api`, `ui`,
   `stream`, `deps`, `docker`, `ia`, `rgpd`. Pas le nom d'une branche, pas celui d'une
   personne.
3. Impératif, sans point final, 72 caractères maximum.
4. Le corps explique **pourquoi**. Trois lignes suffisent.
5. **Un changement logique par commit.** Deux sujets, deux commits.
6. Le formatage global est un commit à part, jamais mélangé à une fonctionnalité.
7. Aucun secret, aucun `.env`, aucun fichier généré dans un commit.

## Qui écrit les commits, et pourquoi l'agent ne pousse pas

Un rôle `committer` est fourni par ce dépôt. Il prépare le message, regroupe le travail
logique et crée le commit. Il lui est **interdit de pousser**.

Ce périmètre est délibéré. L'IA peut écrire du code, mais un code écrit par une IA doit
être lu, relu et testé par la personne qui le livre. Autoriser un push automatique
retirerait de la boucle le seul moment où cette vérification peut encore se produire.

Autrement dit : l'agent `committer` rend l'historique lisible, il ne l'authentifie pas.
Le développeur garde la décision de livrer, et par conséquent la responsabilité de ce
qui est livré.

Si ce contrôle vous paraît trop strict pour un projet, rappelez-vous ce qu'il protège :
la capacité de revenir en arrière.

## Processus

1. Le code est écrit et **testé** par le développeur.
2. `git status` et `git diff` pour voir ce qui est réellement modifié.
3. Le message est rédigé ou demandé à l'agent `committer`.
4. `git add` sur les fichiers nommés, `git commit`.
5. Le relu, puis **le développeur** pousse : `git push`.

## Messages interdits

| Interdit | Raison |
| --- | --- |
| `fix` | ne dit pas ce qui est corrigé |
| `wip` / `misc` | un travail inachevé ne se commite pas, ou se commit avec la mention |
| `update` | trop vague pour être utile dans un an |
| `ajout de la fonction de streaming du chat` | le corps du diff le dit déjà ; le message doit dire pourquoi |
| Un message en français dans un projet à documentation française | l'historique est relu par des outils et des personnes qui ne lisent pas le français |
| Un message qui décrit autre chose que le diff | pire qu'un mauvais message : il ment |

## Historique réécrit

Un commit n'est jamais réécrit : ni `amend`, ni `rebase` d'un commit déjà poussé, ni
`reset` destructif. Si une commit est réellement fausse, on la revert explicitement
avec `⏪ revert(scope): ...`, ce qui laisse une trace — ce qui est précisément l'intérêt
d'un historique.