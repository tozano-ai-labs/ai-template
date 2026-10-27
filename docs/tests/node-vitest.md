# Tests Node — Vitest

Outillage de référence pour les projets Node du dépôt. Adapte les principes de
[`README.md`](README.md), cette page ne décrit que l'outillage.

## Installation

```bash
npm install -D vitest @vitest/coverage-v8
```

## Scripts du projet

```json
{
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "lint": "eslint .",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "typecheck": "tsc --noEmit"
  }
}
```

`vitest run` en mode non interactif : la commande doit terminer et rendre un code de
sortie, jamais attendre une saisie.

## Configuration

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'node',
    include: ['**/*.{test,spec}.?(c|m)[jt]s?(x)'],
    exclude: ['**/node_modules/**', '**/dist/**'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'lcov', 'html'],
      thresholds: {
        lines: 80,
        functions: 80,
        branches: 80,
        statements: 80,
      },
      exclude: ['**/*.config.*', '**/index.ts', '**/node_modules/**', '**/dist/**'],
    },
  },
})
```

`test:coverage` échoue si les seuils ne sont pas atteints : c'est le comportement
recherche, pas une information affichée puis ignorée.

## Organisation

Les tests vivent **à côté du code**, jamais dans un dossier `tests/` séparé qui
finira par désynchroniser les chemins.

```text
src/
  chat/
    stream.ts
    stream.test.ts
    historique.ts
    historique.test.ts
```

Dans un dépôt à deux paquets, un dossier `test/` à la racine est acceptable, à condition
que l'arborescence reste parallèle au code.

## Nommage et structure

```ts
import { describe, expect, it } from 'vitest'

describe('decoupeFlux', () => {
  it('should emit a token for each NDJSON chunk', () => {
    // ...
  })

  it('should return an empty stream when the model returns nothing', () => {
    // ...
  })
})
```

Un `describe` par unité testée, des `it` qui décrivent un comportement attendu et non un
appel de fonction.

## Fixtures et doublures

```ts
import { beforeEach, vi } from 'vitest'

beforeEach(() => {
  vi.restoreAllMocks()
})
```

- **`vi.fn()`** pour doubler un collaborateur, jamais un module entier.
- **Pas de `vi.mock` global** sans raison : la doublure d'une dépendance entière rend
  le test faux positif dès que l'API change.
- **Fabriques explicites** pour les données partagées, avec des valeurs par défaut
  sobres :

```ts
const message = (surcharge: Partial<Message> = {}): Message => ({
  id: 'msg_1',
  role: 'user',
  contenu: 'bonjour',
  ...surcharge,
})
```

- **Aucune donnée réelle** dans une fixture : ni nom, ni adresse, ni numéro. Voir
  [`../rgpd/CHECKLIST.md`](../rgpd/CHECKLIST.md).

## Tests HTTP

Pour un serveur Express ou équivalent : `supertest` sur l'application, jamais sur un
port réel démarré. Les tests doivent tourner sans occupation de port.

## Tests de composants

Pour Vue ou React : environnement `jsdom` ou `happy-dom` déclaré **par fichier** ou par
projet de test, plutôt que globalement. Les composants sont testés par comportement rendu
— ce que voit l'utilisateur — pas par état interne.

## Points d'attention

- `vi.useFakeTimers()` pour tester un délai, puis `vi.useRealTimers()` : un test qui
  laisse des faux minuteries active casse les suivants.
- Les erreurs de promesse se vérifient avec `await expect(...).rejects.toThrow(...)`.
- Un test qui dépend d'un module avec état global doit le réinitialiser explicitement.
- Les flux (streaming, SSE) se testent en consommant l'async generator jusqu'au bout,
  pas en lisant l'état interne.