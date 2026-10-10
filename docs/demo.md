# Scénario de démonstration — 2 min 50

Préparer et entraîner les deux piles avant l’enregistrement. Ne pas consacrer la vidéo au téléchargement des images. Masquer les informations personnelles de l’écran.

1. **0:00–0:20** — Présenter l’objectif : assistant universitaire en français, données fictives, Rasa et Docker.
2. **0:20–1:10** — Ouvrir localhost:8080. Envoyer « Bonjour », « Comment m’inscrire ? » et « Quels documents fournir ? ».
3. **1:10–1:40** — Demander « Quels sont les horaires ? », puis préciser « La bibliothèque ». Montrer la réponse issue de l’action Python.
4. **1:40–2:00** — Envoyer « Commande une pizza » pour illustrer le hors domaine. Utiliser « Nouvelle discussion ».
5. **2:00–2:25** — Montrer `docker compose ps` et expliquer les trois services et le réseau interne. Mentionner le conteneur d’entraînement ponctuel et le volume du modèle.
6. **2:25–2:50** — Montrer localhost:8081 et `docker compose -p universibot-cloud -f docker-compose.yml -f deploy/cloud-simulation.yml ps`. Expliquer qu’il s’agit d’une pile locale isolée simulant un déploiement et qu’une VM cloud peut reprendre la même stack.

La durée indiquée est un guide. La capture vidéo doit être réalisée sur une machine où Docker et les modèles fonctionnent ; ce document n’est pas une preuve d’exécution.
