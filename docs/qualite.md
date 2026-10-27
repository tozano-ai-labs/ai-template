# Qualité et Definition of Done

## Definition of Done

Un changement est terminé quand **toutes** ces lignes sont vraies. Une ligne non
vraie se dit, elle ne se contourne pas.

- [ ] Le code compile et démarre réellement.
- [ ] La suite de tests passe, et le nouveau comportement est couvert par un test qui
      échoue si on casse le code.
- [ ] Le linter, le formateur et le vérificateur de types passent.
- [ ] Aucun secret, aucun `.env`, aucun fichier généré dans le diff.
- [ ] Les cas limites sont traités : entrée vide, valeur absente, erreur réseau,
      réponse invalide d'un modèle.
- [ ] La documentation utilisateur est à jour si le comportement visible change.
- [ ] Les variables d'environnement ajoutées sont documentées **et** dans `.env.example`.
- [ ] Si des données personnelles sont touchées : les points de
      [`rgpd/CHECKLIST.md`](rgpd/CHECKLIST.md) concernés ont été examinés.
- [ ] Le commit suit le format de [`commits.md`](commits.md).

## Outillage attendu

Un projet qui consomme ce dépôt fournit au minimum :

```bash
npm run lint          # ESLint, ruff, ou équivalent
npm run format        # Prettier, ruff format
npm test              # suite complète
npm run test:coverage # couverture
npm run typecheck     # si typé
```

Si l'un de ces scripts n'existe pas, il est créé avec la première fonctionnalité, pas
plus tard. L'absence d'outillage est la première cause de dérive de code.

## Couverture

- **80 % global**, **90 % sur la logique métier** (branchements, calculs, règles).
- Le seuil est configuré dans l'outil de couverture et **fait échouer la CI**, pas
  seulement l'affichage.
- La couverture mesure l'exécution des lignes, pas la justesse des assertions. Un test
  qui ne vérifie rien fait monter le chiffre sans rien protéger : la relecture compte
  autant que le chiffre.

## Intégration continue

Le projet fournit un workflow qui, sur chaque push et chaque pull request :

1. installe les dépendances de manière reproductible (lockfile committé) ;
2. lance le linter et le vérificateur de types ;
3. lance les tests avec couverture et compare aux seuils ;
4. construit l'application ;
5. échoue explicitement, avec la commande et la sortie en cas d'échec.

Le modèle `templates/github-ci-node.yml` fournit un point de départ pour Node, à adapter
au projet plutôt qu'à copier tel quel.

## Revues

Avant fusion :

- `reviewer` relit le diff en cherchant les bugs, les régressions et les tests
  manquants ;
- `security-auditor` intervient si le changement touche l'authentification, des
  données personnelles, une surface LLM ou une dépendance ;
- `docs-writer` vérifie que la documentation décrit le code réellement livré.

Une revue qui ne trouve rien doit le dire explicitement. Un rapport qui trouve toujours
quelque chose ne sert à rien.

## Dette assumée

Une dette connue s'écrit dans le suivi de tâches avec son propriétaire et son échéance.
Une dette invisible est une dette qu'on transmet sans le savoir : c'est la première
source de surprises dans un projet repris six mois plus tard.