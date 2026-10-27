# Checklist RGPD

> **Fichier généré.** Source de vérité : [`checklist.yml`](checklist.yml).
> Ne pas éditer ce fichier à la main : modifier le YAML puis régénérer avec
> `python3 scripts/generate-checklist.py`.

Version 1.0.0 — 84 items : 29 bloquants, 51 importants, 4 recommandés.

## Utilisation

1. Lire [`README.md`](README.md) pour la méthode et les statuts.
2. Examiner le projet et reporter le résultat dans `docs/rgpd/etat.yml` du
   projet, jamais dans ce dépôt.
3. Ne retenir un item comme `conforme` que si une preuve existe.

Un item `bloquant` non conforme produit une alerte avant livraison ; il
n'interdit pas la livraison. La décision reste humaine.

## Sommaire

| Section | Items | Dont bloquants |
| --- | ---: | ---: |
| [Finalités et périmètre](#finalites) | 5 | 2 |
| [Bases légales](#baselegale) | 5 | 2 |
| [Consentement](#consentement) | 6 | 2 |
| [Minimisation](#minimisation) | 5 | 1 |
| [Durées de conservation](#conservation) | 5 | 2 |
| [Destinataires et sous-traitance](#destinataires) | 5 | 2 |
| [Transferts hors Union européenne](#transferts) | 3 | 2 |
| [Droits des personnes](#droits) | 11 | 3 |
| [Sécurité des données](#securite) | 7 | 4 |
| [Cookies et traceurs](#cookies) | 5 | 1 |
| [Violations de données](#violations) | 4 | 1 |
| [Gouvernance](#gouvernance) | 6 | 2 |
| [Systèmes IA](#ia) | 17 | 5 |

## Détail des items

<a id="finalites"></a>

### Finalités et périmètre

> Avant toute autre question, savoir ce que le projet fait et pourquoi. Un traitement sans finalité écrite ne peut pas être loyal.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-FIN-01` | Les finalités du projet sont-elles écrites, déterminées et explicites ? | Une section « finalités » dans un document interne ou le README | 🔴 bloquant | RGPD art. 5.1.b |
| `RGPD-FIN-02` | Chaque traitement a-t-il un périmètre délimité, et sait-on ce qui n'est pas traité ? | Liste des traitements couverts et exclus | 🟠 important | RGPD art. 5.1.b, art. 30 |
| `RGPD-FIN-03` | Les personnes concernées sont-elles identifiées (utilisateurs, prospects, salariés, visiteurs) ? | Mention des catégories de personnes concernées | 🟠 important | RGPD art. 30 |
| `RGPD-FIN-04` | Les données réellement collectées sont-elles celles annoncées aux utilisateurs ? | Comparaison entre le formulaire ou l'API et la documentation | 🔴 bloquant | RGPD art. 5.1.a, art. 12 |
| `RGPD-FIN-05` | Les usages secondaires (statistiques, amélioration, démonstration) sont-ils séparés des usages annoncés ? | Liste des usages et de leur qualification | 🟠 important | RGPD art. 5.1.b, art. 6.4 |

<a id="baselegale"></a>

### Bases légales

> Aucun traitement n'est licite sans base légale. L'intérêt légitime n'est pas une formule magique : il se documente et se teste.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-BL-01` | Chaque traitement repose-t-il sur une base légale identifiée et documentée ? | Colonne « base légale » non vide pour chaque ligne du registre des traitements | 🔴 bloquant | RGPD art. 6, art. 13.1.c |
| `RGPD-BL-02` | L'intérêt légitime est-il mis en balance, pesé, et documenté ? | Note d'intérêt légitime : intérêt, impact, mesures de sauvegarde | 🟠 important | RGPD art. 6.1.f, RGPDL 29 |
| `RGPD-BL-03` | Les données sensibles ou les données concernant des mineurs font-ils l'objet d'un traitement renforcé ? | Mention du caractère sensible ou du public jeune âge, et mesures prévues | 🔴 bloquant | RGPD art. 9, RGPDL 28 |
| `RGPD-BL-04` | Les champs obligatoires sont-ils réellement indispensables à la finalité annoncée ? | Justification champ par champ | 🟠 important | RGPD art. 5.1.c |
| `RGPD-BL-05` | Les données prévues à l'origine pour une finalité ne sont-elles pas réemployées sans nouvelle base légale ? | Revue des champs réutilisés et de leur nouvelle base légale | 🟠 important | RGPD art. 5.1.b, art. 6.4 |

<a id="consentement"></a>

### Consentement

> Le consentement n'est qu'une base légale parmi cinq. Il ne sert que lorsque les autres ne s'appliquent pas, et il a des exigences de forme strictes.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-CNS-01` | Le consentement est-il recueilli lorsque c'est la base légale retenue, et seulement dans ce cas ? | Base légale retenue par traitement et formulaire de recueil | 🔴 bloquant | RGPD art. 6.1.a, art. 7 |
| `RGPD-CNS-02` | Le consentement est-il libre, spécifique, informé, explicite et dénué d'ambiguïté ? | Texte du consentement et granularité des finalités proposées séparément | 🟠 important | RGPD art. 4.11, art. 7.2 |
| `RGPD-CNS-03` | Le refus est-il aussi simple que l'acceptation, et le silence vaut-il refus ? | Parcours de refus et absence de consentement par défaut | 🟠 important | RGPD art. 7.3, RGPDL 25 |
| `RGPD-CNS-04` | Le retrait du consentement est-il aussi accessible que l'acceptation, à tout moment ? | Lien ou bouton de retrait, et son effet effectif sur le traitement | 🟠 important | RGPD art. 7.3 |
| `RGPD-CNS-05` | L'historique des consentements est-il conservé pour prouver le consentement ? | Journal horodaté des acceptations et refus | 🟠 important | RGPD art. 7.1 |
| `RGPD-CNS-06` | L politique de confidentialité présente-t-elle clairement le responsable, ses coordonnées et les droits ? | Page ou fichier de politique de confidentialité accessible | 🔴 bloquant | RGPD art. 13, art. 14 |

<a id="minimisation"></a>

### Minimisation

> Ne collecter que ce qui sert la finalité, et rien de plus.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-MIN-01` | Chaque champ collecté est-il nécessaire à la finalité annoncée ? | Tableau champ / finalité / nécessité | 🔴 bloquant | RGPD art. 5.1.c |
| `RGPD-MIN-02` | Les champs facultatifs sont-ils réellement facultatifs, et leur saisie acceptée sans justification particulière ? | Comportement du formulaire pour un champ optionnel | 🟠 important | RGPD art. 5.1.c |
| `RGPD-MIN-03` | Les données techniques collectées (adresse IP, identifiant, user-agent) sont-elles limitées au nécessaire ? | Liste des en-têtes et métadonnées collectés, et usage de chacun | 🟠 important | RGPD art. 5.1.c |
| `RGPD-MIN-04` | Les données sont-elles pseudonymisées ou anonymisées quand l'identification n'est pas nécessaire ? | Mécanisme de pseudonymisation en place, clés conservées séparément | 🟠 important | RGPD art. 5.1.c, art. 25, RGPDL 26 |
| `RGPD-MIN-05` | Les données libres sont-elles exclues ou nettoyées avant exploitation ? | Liste des champs libres et règle de nettoyage | 🟠 important | RGPD art. 5.1.c |

<a id="conservation"></a>

### Durées de conservation

> Une donnée conservée indéfiniment est une donnée conservée sans base légale. Chaque catégorie a une durée, et la purge est automatique et vérifiable.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-CON-01` | Une durée de conservation est-elle définie pour chaque catégorie de données ? | Table des durées par catégorie | 🔴 bloquant | RGPD art. 5.1.e, art. 13.2.a |
| `RGPD-CON-02` | La purge est-elle automatique, et non dépendante d'une intervention manuelle ? | Tâche planifiée ou déclencheur de purge, et sa fréquence | 🔴 bloquant | RGPD art. 5.1.e |
| `RGPD-CON-03` | La purge couvre-t-elle les journaux, sessions, sauvegardes et fichiers temporaires ? | Inventaire des emplacements de stockage et règle appliquée à chacun | 🟠 important | RGPD art. 5.1.e |
| `RGPD-CON-04` | La durée du cookie de consentement expire-t-elle au plus tard après sa pose ? | Durée maximale du cookie | 🟠 important | RGPD art. 5.1.e, RGPDL 25 |
| `RGPD-CON-05` | Un compte inactif est-il purgé automatiquement au terme de la durée prévue ? | Règle d'inactivité et tâche associée | 🟡 recommandé | RGPD art. 5.1.e |

<a id="destinataires"></a>

### Destinataires et sous-traitance

> Chaque destinataire est un sous-traitant tant qu'il traite pour le compte du responsable. Un hébergeur, un service d'email, un fournisseur de modèle : tous doivent figurer dans la liste.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-DES-01` | La liste des destinataires et sous-traitants est-elle connue, complète et à jour ? | Liste nominative avec rôle pour chacun | 🔴 bloquant | RGPD art. 28, art. 30.2 |
| `RGPD-DES-02` | Chaque sous-traitant est-il encadré par un contrat conforme à l'article 28 ? | Référence aux contrats ou clauses de sous-traitance | 🔴 bloquant | RGPD art. 28.3 |
| `RGPD-DES-03` | Les sous-traitants hors Union européenne sont-ils encadrés par une garantie de transfert ? | Décision d'adéquation, clauses contractuelles types ou disposition particularisée | 🟠 important | RGPD art. 44 à 49 |
| `RGPD-DES-04` | Les utilisateurs sont-ils informés des destinataires et de leurs finalités ? | Mention dans la politique de confidentialité | 🟠 important | RGPD art. 13.1.e, art. 14.1.e |
| `RGPD-DES-05` | Les accès internes sont-ils limités au strict nécessaire, avec une traçabilité des accès ? | Matrice des rôles et journal des accès aux données | 🟠 important | RGPD art. 5.1.f, art. 32 |

<a id="transferts"></a>

### Transferts hors Union européenne

> Distinguer transfert et traitement dans l'Union. Les lignes ci-dessous ne concernent que les seconds.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-TRF-01` | Les données quittent-elles l'Union européenne, et pour quels destinataires ? | Inventaire des flux sortants et des pays de destination | 🔴 bloquant | RGPD art. 44 |
| `RGPD-TRF-02` | Chaque transfert est-il encadré par un mécanisme reconnu ? | Référence au mécanisme utilisé par transfert | 🔴 bloquant | RGPD art. 45 à 49 |
| `RGPD-TRF-03` | Les transferts sont-ils mentionnés à l'information des personnes ? | Mention des transferts dans la politique de confidentialité | 🟠 important | RGPD art. 13.1.f |

<a id="droits"></a>

### Droits des personnes

> Six droits d'identique portée : accès, rectification, effacement, limitation, portabilité, plus l'opposition. Le backlog existe tant qu'on ne sait pas les exécuter.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-DRT-01` | Le droit d'accès est-il outillé : une demande aboutit-elle à une extraction complète de la personne concernée ? | Parcours testé de bout en bout, avec sa date de test | 🔴 bloquant | RGPD art. 15 |
| `RGPD-DRT-02` | La rectification est-elle possible par la personne elle-même, sans passer par un tiers ? | Parcours de modification testé | 🟠 important | RGPD art. 16 |
| `RGPD-DRT-03` | L'effacement est-il réellement exécuté, données comprises, dans tous les systèmes ? | Procédure d'effacement avec liste des systèmes traversés et test | 🔴 bloquant | RGPD art. 17 |
| `RGPD-DRT-04` | L'effacement atteint-il les copies, sauvegardes, index de recherche et vecteurs ? | Inventaire des emplacements et traitement de chacun | 🟠 important | RGPD art. 17, art. 5.1.e |
| `RGPD-DRT-05` | La limitation du traitement est-elle possible, et le traitement reprend-il correctement ensuite ? | Drapeaux de limitation dans le schéma de données | 🟠 important | RGPD art. 18 |
| `RGPD-DRT-06` | La portabilité est-elle fournie dans un format lisible par machine ? | Format de l'export et procédure de génération | 🟠 important | RGPD art. 20 |
| `RGPD-DRT-07` | L'opposition est-elle outillée, y compris pour la prospection ? | Liste des traitements fondés sur l'intérêt légitime et sur le consentement, avec leur liste d'exclusion | 🟠 important | RGPD art. 21 |
| `RGPD-DRT-08` | Le délai de réponse d'un mois est-il suivi, et les demandes sont-elles registrées ? | Registre des demandes avec date de réception et de réponse | 🟠 important | RGPD art. 12.3 |
| `RGPD-DRT-09` | L'identité du demandeur est-elle vérifiée avant l'exécution d'un droit ? | Procédure de vérification d'identité | 🟠 important | RGPD art. 12.6 |
| `RGPD-DRT-10` | Le responsable et un contact sont-ils identifiés et joignables pour les demandes ? | Coordonnées publiées et surveillées | 🔴 bloquant | RGPD art. 13.1.a, art. 37.1.b |
| `RGPD-DRT-11` | Une décision automatisée produisant un effet juridique est-elle signalée, motivée et contestable ? | Description du dispositif, intervention humaine et voie de contestation | 🟠 important | RGPD art. 22 |

<a id="securite"></a>

### Sécurité des données

> Les mesures techniques sont adaptées au risque, pas à la tendance.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-SEC-01` | Les données circulent-elles en TLS, y compris entre services internes ? | Configuration et en-têtes observés | 🔴 bloquant | RGPD art. 32.1.a |
| `RGPD-SEC-02` | Les données au repos sont-elles chiffrées quand le risque le justifie ? | Chiffrement du stockage, des sauvegardes et des volumes | 🟠 important | RGPD art. 32.1.a |
| `RGPD-SEC-03` | Les secrets sont-ils hors du dépôt, dans l'environnement ou un gestionnaire dédié ? | Absence de secret versionné, présence de .env.example | 🔴 bloquant | RGPD art. 32.1.b |
| `RGPD-SEC-04` | L'authentification et l'autorisation sont-elles vérifiées côté serveur sur chaque route sensible ? | Test d'accès non autorisé sur une route protégée | 🔴 bloquant | RGPD art. 25, art. 32.1.b |
| `RGPD-SEC-05` | Les entrées sont-elles validées avant traitement, et les sorties échappées au rendu ? | Comportement sur entrée malformée et test de rendu | 🟠 important | RGPD art. 25, art. 32.1.a |
| `RGPD-SEC-06` | Les en-têtes de sécurité et la politique CORS sont-ils restreints au nécessaire ? | Configuration effective et en-têtes produits | 🟠 important | RGPD art. 25, art. 32.1.b |
| `RGPD-SEC-07` | Les données personnelles sont-elles absentes des journaux, y compris les messages d'erreur ? | Extraction d'un échantillon de journaux et recherche de champs personnels | 🔴 bloquant | RGPD art. 5.1.f, art. 32 |

<a id="cookies"></a>

### Cookies et traceurs

> Soumis au RGPD et à la directive ePrivacy : le consentement préalable s'applique à tout traceur non strictement nécessaire.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-COO-01` | Chaque cookie et traceur est-il inventorié avec sa finalité et sa durée ? | Table des cookies ou du bandeau de consentement | 🟠 important | RGPD art. 6.1.a, RGPDL 25 |
| `RGPD-COO-02` | Aucun traceur non essentiel n'est-il déposé avant consentement ? | Observation du dépôt de traceurs avant action sur la bannière | 🔴 bloquant | RGPDL 25, RGPD art. 7 |
| `RGPD-COO-03` | Le refus est-il aussi simple que l'acceptation, par le même nombre de clics ? | Parcours comparé des deux choix | 🟠 important | RGPDL 25 |
| `RGPD-COO-04` | Le consentement est-il demandé pour chaque finalité distincte, et non en bloc ? | Catégories de finalités dans la bannière | 🟠 important | RGPDL 25, RGPD art. 7.2 |
| `RGPD-COO-05` | Le retrait du consentement aux cookies est-il accessible à tout moment ? | Lien de retrait présent sur toutes les pages | 🟠 important | RGPD art. 7.3 |

<a id="violations"></a>

### Violations de données

> La procédure existe avant l'incident, pas pendant.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-VIO-01` | Une procédure de détection et de qualification d'une violation est-elle écrite et connue ? | Procédure datée et accessible | 🟠 important | RGPD art. 33 |
| `RGPD-VIO-02` | Le délai de notification de 72 heures est-il outillé et connu de l'équipe ? | Mention du délai, du responsable et du canal d'escalade | 🔴 bloquant | RGPD art. 33.1 |
| `RGPD-VIO-03` | Les personnes concernées sont-elles informées lorsque le risque est élevé ? | Modèle de message et critère de déclenchement | 🟠 important | RGPD art. 34 |
| `RGPD-VIO-04` | Les violations sont-elles registrées, y compris celles non notifiées ? | Registre des violations avec date, type, impact | 🟠 important | RGPD art. 33.5 |

<a id="gouvernance"></a>

### Gouvernance

> Ce qui permet de démontrer la conformité le jour où on la demande.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-GOV-01` | Le registre des traitements est-il tenu à jour et contient-il les éléments exigés par l'article 30 ? | Registre avec finalité, catégories de données, base légale, destinataires, durées | 🔴 bloquant | RGPD art. 30 |
| `RGPD-GOV-02` | L'information des personnes est-elle à jour et réellement lisible par elles ? | Politique de confidentialité publiée, datée, testée | 🔴 bloquant | RGPD art. 12.1, art. 13 |
| `RGPD-GOV-03` | Les personnes concernées reçoivent-elles l'information au moment de la collecte, pas seulement sur demande ? | Mention visible au moment de la collecte | 🟠 important | RGPD art. 13, art. 14 |
| `RGPD-GOV-04` | Un contact désigné pour la protection des données existe-t-il, ou la non-nomination est-elle justifiée ? | Nomination écrite, ou motif de non-nomination selon la taille | 🟠 important | RGPD art. 37, RGPDL 16 |
| `RGPD-GOV-05` | L'équipe connaît-elle les règles applicables et sait-elle où les trouver ? | Document d'accueil et accès à la présente documentation | 🟡 recommandé | RGPD art. 39 |
| `RGPD-GOV-06` | Les personnes concernées sont-elles sensibilisées au traitement de leurs données ? | Trace d'une action de sensibilisation | 🟡 recommandé | RGPD art. 39.1.b |

<a id="ia"></a>

### Systèmes IA

> Points spécifiques à un projet qui appelle un modèle. Héritent des exigences des sections précédentes : le traitement d'un prompt obéit aux mêmes règles que n'importe quelle donnée personnelle.

| Item | Vérification | Preuve attendue | Criticité | Références |
| --- | --- | --- | --- | --- |
| `RGPD-IA-01` | Le contenu exact envoyé au modèle est-il connu, champ par champ, y compris l'historique et les métadonnées ? | Reconstruction du prompt à partir du code, avec la liste des champs | 🔴 bloquant | RGPD art. 5.1.c, art. 30 |
| `RGPD-IA-02` | Les données envoyées au modèle sont-elles minimisées, et le contenu non nécessaire est-il retiré ? | Comparaison entre les données disponibles et les données envoyées | 🔴 bloquant | RGPD art. 5.1.c, art. 25 |
| `RGPD-IA-03` | Les données sont-elles pseudonymisées ou anonymisées avant l'envoi au modèle ? | Transformation appliquée avant appel, clés conservées côté serveur | 🟠 important | RGPD art. 25, RGPDL 26 |
| `RGPD-IA-04` | Aucun secret ni identifiant direct ne figure-t-il dans un prompt ? | Revue des prompts et des gabarits, test sur un jeu d'entrées | 🔴 bloquant | RGPD art. 32.1.b |
| `RGPD-IA-05` | Le fournisseur du modèle est-il identifié, et son rôle de sous-traitant est-il encadré ? | Nom du fournisseur, localisation, référence au contrat de sous-traitance | 🔴 bloquant | RGPD art. 28 |
| `RGPD-IA-06` | Les données envoyées à un fournisseur hors Union européenne sont-elles encadrées ? | Mécanisme de transfert appliqué au fournisseur de modèle | 🟠 important | RGPD art. 44 à 49 |
| `RGPD-IA-07` | L'usage des données envoyées pour entraîner ou améliorer un modèle chez le fournisseur est-il exclu contractuellement ? | Clause de non-entraînement, ou mention de l'absence d'usage | 🟠 important | RGPD art. 28.3.h |
| `RGPD-IA-08` | Les prompts et réponses sont-ils journalisés en clair ? | Absence de contenu de prompt dans les journaux, ou hachage en place | 🔴 bloquant | RGPD art. 5.1.f, art. 32 |
| `RGPD-IA-09` | Une durée de conservation est-elle appliquée aux conversations conservées ? | Règle de purge des conversations et tâche associée | 🟠 important | RGPD art. 5.1.e |
| `RGPD-IA-10` | Les vecteurs, index de similarité et bases de connaissances sont-ils inclus dans la purge ? | Inventaire des index et règle appliquée à chacun | 🟠 important | RGPD art. 17, art. 5.1.e |
| `RGPD-IA-11` | La conservation est-elle désactivable par l'utilisateur ? | Option de non-conservation et effet effectif | 🟠 important | RGPD art. 5.1.a |
| `RGPD-IA-12` | L'utilisateur est-il informé de façon explicite qu'il dialogue avec un système IA ? | Mention visible dans l'interface et dans la politique de confidentialité | 🟠 important | RGPD art. 13 |
| `RGPD-IA-13` | Les données d'entraînement ou d'évaluation du modèle sont-elles documentées, y compris leur provenance ? | Inventaire des jeux utilisés, origine et licéité des données | 🟠 important | RGPD art. 5.1.b, RGPDL 18 |
| `RGPD-IA-14` | Les biais connus du modèle sont-ils connus de l'équipe et documentés là où l'IA produit une décision ? | Note de biais connus et mesures d'atténuation | 🟠 important | RGPD art. 22, RGPD art. 5.1.d |
| `RGPD-IA-15` | Une analyse d'impact relative à la protection des données a-t-elle été menée pour un usage à haut risque ? | AIPD réalisée, ou justification écrite de son absence | 🟠 important | RGPD art. 35, RGPDL 65 |
| `RGPD-IA-16` | Le mode d'hébergement du modèle est-il documenté, en distinguant hébergement local et fournisseur externe ? | Mention de l'hébergeur, de la localisation et de l'absence de sortie de données en local | 🟠 important | RGPD art. 28, art. 44 |
| `RGPD-IA-17` | Le coût et le volume des appels au modèle sont-ils plafonnés pour éviter un traitement non maîtrisé ? | Quotas ou plafonds par utilisateur et par période | 🟡 recommandé | RGPD art. 5.1.b |

## Lexique

- **Bloquant** — À corriger avant toute mise en production.
- **Important** — À corriger ou à justifier par écrit.
- **Recommandé** — Utile, non bloquant.

Statuts possibles dans l'état du projet : `a_verifier`, `conforme`, `non_conforme`, `non_applicable`.

---

Outil de travail, pas un avis juridique. Voir la section « Portée »
de [`README.md`](README.md).
