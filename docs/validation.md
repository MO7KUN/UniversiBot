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

## Vérifications à confirmer

Le [workflow initial](https://github.com/MO7KUN/UniversiBot/actions/runs/38094713058) a réussi : construction des trois images, validation Rasa, entraînement, commandes d’évaluation NLU/Core, démarrage avec contrôles de santé et test HTTP réel via Nginx. Les requêtes « bonjour » et « Quels sont les horaires de la bibliothèque ? » ont reçu les réponses attendues. Les rapports d’évaluation sont publiés en artefacts du workflow ; aucun score NLU n’est affirmé sans lecture de ces rapports.

Le workflow inclut également une seconde pile isolée sur le port 8081 pour vérifier la simulation cloud. Son résultat sera confirmé dans l’exécution correspondante.

Le moteur Docker local n’était pas joignable pendant la préparation, même après une tentative de démarrage de Docker Desktop. Aucun entraînement local Rasa, score NLU, test Core, démarrage complet des conteneurs ni simulation cloud exécutée n’est revendiqué.

La présence d’un workflow ne signifie pas qu’il a réussi. Consulter son état et ses artefacts dans l’onglet Actions du dépôt avant de présenter des résultats d’évaluation. Une vidéo de démonstration n’a pas été enregistrée.
