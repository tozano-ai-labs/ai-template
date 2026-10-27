# Sécurité des systèmes IA

Les risques propres à un système qui appelle un modèle. Complète, sans le remplacer,
une revue de sécurité classique.

## Principe fondateur

**Tout ce qui entre dans un prompt et tout ce qui en sort est une donnée non
fiable.** Un modèle est un composant externe qui ne respecte aucune contrainte du
programme : il ne filtre pas, il ne valide pas, il ne s'excuse pas de divulguer.

## 1. Le prompt comme surface d'attaque

| Attaque | Effet | Contre-mesure |
| --- | --- | --- |
| Injection indirecte | un document lu par le modèle contient des instructions qui contredisent le system prompt | séparer strictement les instructions des données, ne jamais laisser une donnée remplacer une instruction |
| Exfiltration | le modèle restitue des éléments du system prompt ou du contexte | filtrer la sortie, ne jamais considérer le system prompt comme confidentiel face au contenu utilisateur |
| Empoisonnement de la mémoire | une donnée injectée dans un historique ou une base de connaissances agit plus tard | assainir avant écriture, isoler par utilisateur |
| Déni de service | requête Huge, boucle d'outils, coût non maîtrisé | limites de longueur, quotas, budget de tokens par requête et par utilisateur |
| Extraction de modèle | l'utilisateur cherche à reproduire le modèle ou ses données d'entraînement | pas de secrets dans le prompt, pas d'indication sur l'entraînement dans les réponses |

La sortie d'un modèle est traitée comme une entrée utilisateur : validation de schéma,
échappement au rendu, jamais d'exécution.

## 2. Ce qui part chez le fournisseur

Avant tout appel à une API tierce, savoir précisément :

- quelles données entrent dans le prompt : champs préremplis, historique, pièces
  jointes, métadonnées techniques, identifiant de session ;
- où elles vont : pays du fournisseur, durée de conservation, sous-traitance
  éventuelle, transfert hors Union européenne ;
- si elles servent à entraîner le modèle — et, si oui, comment l'empêcher ;
- ce qui reste chez soi : un identifiant technique est-il, lui aussi, une donnée
  personnelle ? oui, s'il permet de rattacher une session à une personne.

C'est le point de départ des items de la section `ia` de
[`rgpd/CHECKLIST.md`](rgpd/CHECKLIST.md).

## 3. Journalisation

- **Ne jamais journaliser un prompt brut** s'il peut contenir une donnée personnelle.
  Alternatives : hacher, tronquer, journaliser un identifiant de conversation et sa
  longueur.
- Journaliser le fournisseur appelé, le modèle, la durée, le statut, le nombre de
  tokens — c'est utile au débogage et sans risque.
- Un journal d'accès contient une donnée personnelle : il entre dans le registre des
  traitements et il a une durée de conservation.

## 4. Secrets

- Aucune clé d'API dans le dépôt, dans une image Docker, dans un prompt ou dans un
  message d'erreur.
- Clés par environnement, pas par service : une clé par usage permet de révoquer une
  fuite sans casser tout.
- Rotation documentée : qui, quand, et comment on sait que c'est fait.

## 5. IA locale et IA hébergée

| | IA locale (Ollama sur sa propre machine) | IA hébergée (API tierce) |
| --- | --- | --- |
| Sortie des données | La donnée ne quitte pas la machine | La donnée part chez un tiers |
| Base légale | Pas de transfert, mais le traitement reste soumis au RGPD | Transfert et sous-traitance à documenter |
| Coût | Aucun coût par requête, matériel à maintenir | Coût par token, plafond à mettre en place |
| Qualité | Modèles plus petits, qualité moindre | Généralement supérieure |
| Exploitation | Aucune | Dépendance à un service externe |

Le choix « local » réduit fortement l'exposition des données, il ne supprime pas les
obligations : finalité, base légale, information des personnes, durées de conservation
et droits restent pleinement applicables.

## 6. Garde-fous d'usage

- Limite de longueur sur l'entrée utilisateur, avant l'appel.
- Plafond de tokens par requête et par utilisateur, avec un message d'erreur clair.
- Timeout sur l'appel : une requête qui n'aboutit pas ne doit pas bloquer une requête
  suivante à l'infini.
- Repli explicite quand le modèle est indisponible : le produit doit rester utilisable.
- Tests dédiés aux entrées hostiles : texte vide, texte très long, JSON invalide,
  instruction d'injection, tentatives d'extraction du system prompt.

## 7. Transparence

L'utilisateur doit savoir qu'il dialogue avec un modèle : mention explicite dans
l'interface, et information dans la politique de confidentialité quand la
conversation est conservée.

Une décision prise automatiquement et produisant un effet juridique ou significatif
relève de l'article 22 du RGPD : information de la personne, intervention humaine,
possibilité de contester, et motivation de la décision. Voir la section `droits` de la
checklist.