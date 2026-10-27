---
name: pre-release
description: Use before creating a git tag, releasing a version, or merging to a stable branch. Runs lint, tests and coverage thresholds, build, secret scan, changelog update, RGPD alert and version bump in the right order. Triggers on "release", "livrer", "préparer la livraison", "créer un tag", "version".
---

# Avant livraison

Checklist exécutée dans l'ordre. Chaque étape donne un résultat vérifiable : si une étape
échoue, on s'arrête là et on ne passe pas à la suivante. On ne « contourne » pas une
étape en se disant que ce sera fait plus tard.

## 0. Identifier la livraison

```bash
git status --short
git log --oneline -10
git describe --tags --abbrev=0 2>/dev/null || echo "aucun tag"
```

Établir : ce qui est livré (commits depuis le dernier tag), et ce qui ne l'est pas
(travail non committé — il ne part pas).

## 1. Arborescence propre et sans secret

```bash
git diff --staged --stat
grep -rInE "(api[_-]?key|secret|password|token)\s*[:=]" --exclude-dir={.git,node_modules,dist} .
```

- Aucun secret dans le diff ni dans le dépôt. `.env` n'est jamais committé, seulement
  `.env.example`.
- Aucun fichier généré (`dist/`, `coverage/`, `*.log`) dans le diff.

## 2. Qualité statique

Lancer les commandes du projet, dans cet ordre :

```bash
npm run lint       # ou ruff / eslint selon la stack
npm run format:check
npm run typecheck  # si le projet est typé
```

Corriger avant de continuer. Un avertissement de typage ou de lint n'est pas bloquant
seulement s'il est connu et documenté dans le rapport.

## 3. Tests et couverture

```bash
npm test
npm run test:coverage
```

Vérifier :

- **zéro échec**, pas « zéro échec sauf celui déjà connu » ;
- la couverture atteint les seuils du projet, ceux de `docs/tests/README.md` par
  défaut : **80 % global, 90 % sur la logique métier** ;
- les tests sont déterministes : pas de `sleep`, pas de dépendance à l'ordre
  d'exécution, pas d'accès réseau réel.

Si un test est instable, il est traité comme un échec : on le signale, on ne le relance
pas en espérant que ça passe.

## 4. Build et démarrage

```bash
npm run build
```

Puis démarrer réellement l'application et vérifier qu'elle répond. Un build qui passe
n'est pas une preuve que l'application démarre.

## 5. Alerte RGPD

Si `docs/rgpd/etat.yml` existe :

```bash
cat docs/rgpd/etat.yml
```

Confronter aux items de `docs/rgpd/CHECKLIST.md` :

- lister les items de criticité `bloquant` au statut autre que `conforme` ;
- préciser lesquels sont touchés par les commits livrés ;
- **ne pas bloquer la livraison** : c'est une alerte destinée au développeur, la
  décision reste humaine ;
- ne jamais modifier `etat.yml` pendant cette étape : le statut se saisit quand
  l'audit est réellement fait.

Si le projet manipule des données personnelles et que le registre des traitements
(`docs/rgpd/`) n'existe pas, le signaler comme point à traiter.

## 6. Documentation à jour

- Le `README.md` décrit-il le comportement réellement livré ?
- Les variables d'environnement ajoutées sont-elles documentées **et** présentes dans
  `.env.example` ?
- Un changement d'interface ou de contrat d'API est-il répercuté dans la doc ?

## 7. Version et changelog

1. Choisir le bump selon [SemVer](https://semver.org/lang/fr/) :
   - **patch** : correction de bug, aucun changement de contrat ;
   - **minor** : nouvelle fonctionnalité rétrocompatible ;
   - **major** : changement incompatible, suppression, modification d'un contrat.
2. Mettre à jour la version dans le manifeste du projet (`package.json`,
   `pyproject.toml`).
3. Ajouter une section dans `CHANGELOG.md`, format
   [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), avec la date du jour et la
   liste des changements orientés utilisateur.

## 8. Bilan et suite

Rendre compte, sans rien exécuter qui modifie le dépôt :

```markdown
## Livraison prête
Version : <vX.Y.Z>
Commits livrés : <n> (<premier hash>..<dernier hash>)
Lint / types / tests / build : OK — couverture <n> % (seuil <n> %)
Alerte RGPD : <items bloquants concernés, ou « aucun »>

## Reste à faire à la main
- git tag -a vX.Y.Z -m "..."
- git push --follow-tags
```

## Interdits

- Ne jamais créer le tag ni pousser : la livraison reste une décision humaine.
- Ne jamais contourner une étape en échec pour « finir vite ».
- Ne jamais ajouter `--no-verify` pour faire passer un hook qui échoue.
- Ne jamais modifier `etat.yml` ou le changelog pour faire coïncider le rapport avec la
  réalité : on rapporte l'état réel.