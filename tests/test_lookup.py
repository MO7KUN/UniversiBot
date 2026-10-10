import unittest
from actions.lookup import KNOWLEDGE, find_service


class LookupTests(unittest.TestCase):
    def test_known_services(self):
        for service in KNOWLEDGE:
            self.assertEqual(find_service(service), service)

    def test_case_accents_whitespace_and_aliases(self):
        for value in [" BIBLIOTHEQUE ", "Bibliothèque", "BU"]:
            self.assertEqual(find_service(value), "bibliothèque")
        self.assertEqual(find_service("SCOLARITE"), "scolarité")
        self.assertEqual(find_service("bourses"), "service des bourses")

    def test_unknown_service_never_guessed(self):
        for value in ["", "restaurant", "bibliothèque du campus inconnu"]:
            self.assertIsNone(find_service(value))


if __name__ == "__main__":
    unittest.main()
