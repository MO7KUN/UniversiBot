"""Actions Rasa : données fictives, sans accès à des dossiers étudiants."""
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from actions.lookup import KNOWLEDGE, find_service

class ActionHoraires(Action):
    def name(self) -> Text:
        return "action_horaires"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Prefer the current entity; consume the slot so an unrelated later query
        # cannot silently inherit a service from a previous answer.
        value = next(tracker.get_latest_entity_values("service"), None)
        service = find_service(str(value or tracker.get_slot("service") or ""))
        if not service:
            dispatcher.utter_message(response="utter_ask_service")
        else:
            info = KNOWLEDGE[service]
            dispatcher.utter_message(text=f"Horaires fictifs — {service} : {info['hours']}. "
                                         f"Lieu : {info['location']}. À confirmer auprès de votre établissement.")
        return [SlotSet("service", None)]

