# État des vérifications

Les résultats ci-dessous distinguent la validation du code de l’exécution du modèle.

## Vérifications effectuées lors de la préparation

- `docker compose config --quiet` : configuration principale valide.
- Fusion avec `deploy/cloud-simulation.yml` : configuration valide avec Compose 5.2.0.
- `node --check web/app.js` : syntaxe JavaScript valide.
- Aperçu HTTP local : interface chargée dans le navigateur.
- Envoi d’une suggestion sans backend : message d’erreur affiché, boutons réactivés, texte conservé pour réessayer.

## Vérifications à confirmer

L’état des tests Python sera mis à jour après leur exécution. Le workflow GitHub Actions est fourni pour valider, entraîner et évaluer Rasa sous Linux et tester le canal REST.

Le moteur Docker local n’était pas joignable pendant la préparation, même après une tentative de démarrage de Docker Desktop. Aucun entraînement local Rasa, score NLU, test Core, démarrage complet des conteneurs ni simulation cloud exécutée n’est revendiqué.

La présence d’un workflow ne signifie pas qu’il a réussi. Consulter son état et ses artefacts dans l’onglet Actions du dépôt avant de présenter des résultats d’évaluation. Une vidéo de démonstration n’a pas été enregistrée.
