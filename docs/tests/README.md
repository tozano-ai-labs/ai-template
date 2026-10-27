# Stratégie de tests

Règles communes à tout projet consommant ce dépôt. L'outillage dépend de la stack :
voir [`node-vitest.md`](node-vitest.md) ou [`python-pytest.md`](python-pytest.md).

## Ce que la stratégie garantit

1. Un test qui échoue signale un bug réel, pas un problème d'environnement.
2. Un test couvre un comportement observable, pas une implémentation.
3. La suite tourne entière, vite, sans réseau ni service externe.
4. Le chiffre de couverture reflète une vérification, pas une exécution.

## Les trois niveaux

| Niveau | Objet | Dépendances externes | Fréquence |
| --- | --- | --- | --- |
| **Unitaire** | une fonction ou une règle métier | aucune | à chaque commit |
| **Intégration** | une collaboration : route, base, client HTTP, fichier, modèle | conteneur ou doublure locale | à chaque push |
| **End-to-end** | le parcours utilisateur complet | l'application démarrée | avant livraison |

Règle simple : **tout ce qui contient une branche métier a un test unitaire**. Un
parcours n'est testé de bout en bout que s'il est le cœur de la valeur du produit ;
sinon il devient un test lent, instable, et abandonné au premier incident.

## Ce que l'on teste en priorité

1. **Les cas d'erreur** : entrée vide, champ absent, fichier illisible, réseau coupé,
   réponse invalide d'un modèle, réponse démesurée, délai dépassé.
2. **Les frontières** : 0, 1, N-1, N, N+1, valeurs négatives, caractères accentués.
3. **Les règles métier** : chaque branche de décision, chaque condition de purge.
4. **Les entrées hostiles** : injections, chemins de fichiers truqués, désérialisation
   de données non fiables.

## Ce que l'on ne teste pas

- Les accesseurs qui renvoient un champ.
- Le framework lui-même.
- Les détails d'implémentation internes, qui changent sans changer le comportement.
- Les trivialités qui ne peuvent pas échouer.

## Règles de rédaction

- **Un test, une raison d'échouer.** Plusieurs assertions sur un même comportement
  sont acceptables ; plusieurs comportements dans un test ne le sont pas.
- **Nommage descriptif** : le nom doit permettre de comprendre l'échec sans ouvrir le
  fichier. `should refuse a message when the model returns HTML` plutôt que `test 3`.
- **Hérédité nulle** : deux tests ne se suivent jamais, l'ordre d'exécution est
  indifférent.
- **Pas de `sleep`** : on attend un événement, pas une durée. Un test qui dort est un
  test instable en intégration continue.
- **Pas de réseau réel** : doublure, conteneur de service, ou réponse enregistrée.
- **Pas de donnée réelle** : les fixtures sont synthétiques. Jamais de nom, d'adresse,
  de numéro, de secret issus d'une production.
- **Les données personnelles sont des données** : une fixture qui ressemble à une
  adresse réelle reste une donnée à protéger dans un dépôt.

## Couverture

| Périmètre | Seuil par défaut |
| --- | --- |
| Global | **80 %** |
| Logique métier | **90 %** |
| Configuration, point d'entrée, mocks | non mesurée |

Le seuil est **configuré dans l'outil**, en échec de build, et non seulement affiché.
Un projet peut durcir ses seuils ; les assouplir doit s'écrire dans son `AGENTS.md`.

La couverture ne dit pas si les assertions sont justes. Un test qui appelle une fonction
sans vérifier son retour fait monter le chiffre sans protéger quoi que ce soit : la
relecture compte autant que le chiffre.

## Tests et IA

Pour tout appel à un modèle, la réponse est une **donnée non fiable**. Tester
explicitement : texte vide, texte très long, sortie qui n'est pas du JSON attendu, sortie
contenant une tentative d'injection, réponse retardée, fournisseur indisponible.

Pour tout traitement de données personnelles, tester aussi **l'effacement et la purge** :
si un droit d'accès ou d'effacement existe dans le produit, il a un test qui prouve
qu'il marche.

## Avant de livrer

- [ ] La suite complète passe, en une seule exécution, sans relance.
- [ ] Aucun test ignoré (`skip`, `xit`, `@pytest.mark.skip`) sans raison écrite.
- [ ] Aucun test dépendant de l'ordre, de l'heure, du fuseau ou du réseau.
- [ ] Les seuils de couverture sont atteints et appliqués par l'outil.
- [ ] Un flaky est traité comme un échec, pas comme un test qu'on relance.