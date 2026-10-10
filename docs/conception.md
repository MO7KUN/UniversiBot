# Conception du chatbot

## Domaine et objectifs

UniversiBot accompagne les étudiants dans leurs questions administratives courantes. Son périmètre inclut inscriptions, dossiers, aides, examens, documentation, logement, contacts et horaires. Il ne réalise pas d’inscription, de paiement ni de décision d’éligibilité.

## Intentions et entités

Le fichier `data/nlu.yml` comporte 15 intentions avec 8 exemples chacune. Les messages de salutation, aide et clôture sont séparés des questions métier. Les questions de prêts de livres sont séparées des horaires pour limiter leur ambiguïté.

L’entité `service` identifie la scolarité, la bibliothèque et le service des bourses. L’entité `formation` identifie notamment informatique, gestion et droit ; elle sert d’exemple d’extraction et ne déclenche aucune procédure spécialisée. Pour améliorer cette dernière, ajouter davantage d’annotations et des formulations couvrant chaque formation.

## Fichiers Rasa

- `nlu.yml` : messages annotés pour entraîner classification et extraction.
- `domain.yml` : vocabulaire des intentions, entités, slot `service`, textes et action personnalisée.
- `rules.yml` : comportement déterministe par intention et fallback NLU.
- `stories.yml` : parcours d’inscription et clarification du service.
- `config.yml` : pipeline lexical/DIET et politiques de dialogue.
- `credentials.yml` : activation du canal REST.
- `endpoints.yml` : connexion au serveur d’actions par le nom DNS Docker `actions`.

## Traitement d’un message

Le navigateur envoie un identifiant de session aléatoire et le texte au proxy. Rasa calcule l’intention et les entités. La politique sélectionne une réponse ou une action. Pour les horaires, l’action consulte le fichier de connaissances, répond ou demande une précision. La réponse revient sous forme de liste JSON, puis le navigateur affiche les textes sans interpréter de HTML.

## Choix et limites

Un modèle NLU entraîné localement évite les API payantes et rend l’exercice reproductible. Les règles facilitent la traçabilité. Le chatbot ne comprend pas tous les sujets : les exemples hors domaine et les seuils de fallback limitent certains mauvais routages, sans les éliminer. Tester les phrases ambiguës, fautes de frappe et demandes combinées avant d’ajouter des fonctionnalités.

L’apprentissage doit être évalué sur des formulations absentes des données d’entraînement. Ne pas présenter les tests structurels comme une mesure de précision : seul un modèle entraîné et évalué produit des métriques exploitables.
