# État des vérifications

Les résultats ci-dessous distinguent la validation du code de l’exécution du modèle.

## Vérifications effectuées lors de la préparation

- `docker compose config --quiet` : configuration principale valide.
- Fusion avec `deploy/cloud-simulation.yml` : configuration valide avec Compose 5.2.0.
- `node --check web/app.js` : syntaxe JavaScript valide.
- Aperçu HTTP local : interface chargée dans le navigateur.
- Envoi d’une suggestion sans backend : message d’erreur affiché, boutons réactivés, texte conservé pour réessayer.
- Nouvelle discussion : historique d’affichage effacé et nouvel accueil affiché.
- Python 3.10.20 avec Rasa SDK 3.6.2 : **12 tests unitaires réussis**, sans test ignoré.
- GitHub Actions : job `unit` réussi, validation Rasa sans avertissements bloquants et entraînement réussis dans les conteneurs Linux.

## Exécution complète sous Linux

Le [workflow initial](https://github.com/MO7KUN/UniversiBot/actions/runs/38094713058) a réussi : construction des trois images, validation Rasa, entraînement, commandes d’évaluation NLU/Core, démarrage avec contrôles de santé et test HTTP réel via Nginx. Les requêtes « bonjour » et « Quels sont les horaires de la bibliothèque ? » ont reçu les réponses attendues. Les rapports d’évaluation sont publiés en artefacts du workflow ; aucun score NLU n’est affirmé sans lecture de ces rapports.

Le journal Core indique **3 conversations correctes sur 3** et **12 prédictions d’actions correctes sur 12**. Ce petit jeu teste les parcours déclarés ; ces résultats ne mesurent pas la généralisation du NLU sur des demandes libres.

La [seconde exécution](https://github.com/MO7KUN/UniversiBot/actions/runs/38095383460), portant sur le commit `3b36f8b`, a également réussi. Elle répète les vérifications de la pile principale, puis construit une seconde pile `universibot-cloud`, entraîne son propre modèle, attend la santé des services et teste les réponses HTTP sur le port 8081. Les deux piles sont arrêtées à la fin du workflow.

## Limites de vérification

Le moteur Docker du poste local n’était pas joignable pendant la préparation, même après une tentative de démarrage de Docker Desktop. L’entraînement et les tests complets des conteneurs ont donc été effectués sur le runner Linux GitHub Actions. Aucun déploiement sur un compte AWS réel n’a été exécuté.

La présence d’un workflow ne signifie pas qu’il a réussi. Consulter son état et ses artefacts dans l’onglet Actions du dépôt avant de présenter des résultats d’évaluation. Une vidéo de démonstration n’a pas été enregistrée.
