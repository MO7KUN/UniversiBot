import importlib.util
import unittest
from unittest.mock import Mock

HAS_SDK = importlib.util.find_spec("rasa_sdk") is not None
if HAS_SDK:
    from actions.actions import ActionHoraires
    from rasa_sdk.executor import CollectingDispatcher


@unittest.skipUnless(HAS_SDK, "Rasa SDK 3.6.2 requires the Python 3.10 test environment")
class ActionTests(unittest.TestCase):
    def run_action(self, entity=None, slot=None):
        tracker = Mock()
        tracker.get_latest_entity_values.return_value = iter([entity] if entity else [])
        tracker.get_slot.return_value = slot
        dispatcher = CollectingDispatcher()
        events = ActionHoraires().run(dispatcher, tracker, {})
        self.assertEqual(events[0]["name"], "service")
        self.assertIsNone(events[0]["value"])
        return dispatcher.messages[0]

    def test_missing_service_asks_for_clarification(self):
        self.assertEqual(self.run_action()["response"], "utter_ask_service")

    def test_unknown_service_asks_for_clarification(self):
        self.assertEqual(self.run_action("restaurant")["response"], "utter_ask_service")

    def test_entity_has_priority_over_previous_slot(self):
        message = self.run_action("bibliothèque", "scolarité")["text"]
        self.assertIn("18 h", message)
        self.assertIn("fictifs", message)

    def test_slot_is_used_when_no_current_entity(self):
        self.assertIn("16 h", self.run_action(slot="scolarité")["text"])


if __name__ == "__main__":
    unittest.main()
