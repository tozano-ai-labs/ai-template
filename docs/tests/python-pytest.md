# Tests Python — pytest

Outillage de référence pour les projets Python du dépôt. Adapte les principes de
[`README.md`](README.md).

## Installation

```bash
pip install pytest pytest-cov ruff
```

## Configuration

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q --strict-markers --strict-config"

[tool.coverage.run]
source = ["src"]
omit = ["*/__main__.py", "*/config.py"]

[tool.coverage.report]
fail_under = 80
```

`addopts` avec `--strict-markers` interdit un marqueur inconnu : une faute de frappe
dans un marqueur ne transforme pas silencieusement le test en ignoré.

## Organisation

```text
src/
  chat/
    flux.py
tests/
  chat/
    test_flux.py
```

La suite est séparée du code quand le projet est un paquet installable : c'est le
standard. Pour un projet simple, les tests peuvent vivre à côté du code, comme en Node.

## Style

```python
def test_should_emit_one_token_per_chunk():
    flux = decoupe_flux('{"token":"a"}\n{"token":"b"}\n')

    assert list(flux) == ["a", "b"]


def test_should_return_empty_stream_when_model_returns_nothing():
    assert list(decoupe_flux("")) == []
```

Nommage : le nom est une phrase qui décrit le comportement. « test_should » est une
convention répandue et lisible ; une fois choisie, on s'y tient dans tout le projet.

## Fixtures

```python
import pytest

@pytest.fixture
def client():
    return Client(base_url="http://localhost:0", api_key="test-key")

@pytest.fixture
def message() -> dict:
    return {"id": "msg_1", "role": "user", "contenu": "bonjour"}
```

- Une fixture par dépendance, ** demanded à la fonction**, jamais par variable globale.
- Port `0` pour demander un port libre au système plutôt que d'en imposer un : deux
  exécutions en parallèle ne se marchent pas dessus.
- Clé d'API factice `"test-key"` : jamais une vraie, jamais une vraie-shaped value
  valide.
- Aucune donnée réelle dans une fixture. Voir
  [`../rgpd/CHECKLIST.md`](../rgpd/CHECKLIST.md).

## Marquage

```python
import pytest

@pytest.mark.integration
def test_should_persist_message(tmp_path):
    ...
```

```bash
pytest -m "not integration"   # rapide, à chaque commit
pytest                        # tout, avant livraison
```

Les tests d'intégration qui demandent un service externe sont marqués et exclus du
tir rapide. Un test marqué ne doit jamais être ignoré sans raison écrite.

## Doublures

`unittest.mock.patch` sur le point d'usage, en contexte :

```python
with patch("chat.flux.appeler_modele", return_value="bonjour"):
    assert decoupe_flux("bonjour") == ["bonjour"]
```

Patcher là où le symbole est **utilisé**, pas où il est défini : patching
`appeler_modele` dans le module qui l'appelle, sinon la doublure ne s'applique pas.

## Points d'attention

- **`tmp_path`** plutôt que `/tmp` en dur : le test s'isole et se nettoie.
- **`monkeypatch`** pour les variables d'environnement, avec `monkeypatch.delenv` quand
  le test doit vérifier le comportement en l'absence de la variable.
- **`caplog`** pour vérifier un journal — en vérifiant ce qu'il contient **et** ce
  qu'il ne doit pas contenir, notamment l'absence de donnée personnelle.
- Les tests asynchrones : `pytest-asyncio` avec `@pytest.mark.asyncio`, ou tout
  équivalent.
- `freezegun` ou équivalent pour le temps : un test qui dépend de la date réelle échoue
  le jour où un seuil de purge change.