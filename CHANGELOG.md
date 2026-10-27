# Journal des modifications

Toutes les versions de ce dépôt suivent le [SemVer](https://semver.org/lang/fr/).
Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

La version déclarée dans `ai-template.yml` ne prend effet qu'à la création du tag
git correspondant. Une version modifiée sans tag n'est pas opposable à un projet
consommateur : les sous-modules restent figés sur le commit qu'ils ont résolu.

## [Non publié]

### Ajouté

- Rôles d'agents : `architecte`, `dev`, `reviewer`, `test-writer`,
  `security-auditor`, `docs-writer`, `committer`.
- Skills : `commit-message`, `pre-release`.
- Documentation partagée : `docs/conventions.md`, `docs/commits.md`,
  `docs/qualite.md`, `docs/securite-ia.md`.
- Stratégie de tests : `docs/tests/README.md`, `node-vitest.md`,
  `python-pytest.md`.
- Checklist RGPD : `docs/rgpd/checklist.yml` (source de vérité) et `CHECKLIST.md`
  (généré), socle de 12 sections plus une section `ia`.
- Modèles d'installation : `templates/`.

[Non publié]: https://github.com/tozano-ai-labs/ai-template/compare/main...HEAD