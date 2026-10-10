import re
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return yaml.safe_load((ROOT / name).read_text(encoding="utf-8"))


def plain(text):
    return re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text).strip().casefold()


class ProjectTests(unittest.TestCase):
    def test_minimums_and_unique_training_messages(self):
        nlu = [r for r in load("data/nlu.yml")["nlu"] if "intent" in r]
        self.assertGreaterEqual(len(nlu), 10)
        examples = [plain(line.strip()[2:]) for r in nlu
                    for line in r["examples"].splitlines() if line.strip().startswith("- ")]
        self.assertGreaterEqual(len(examples), 30)
        self.assertEqual(len(examples), len(set(examples)))
        self.assertGreaterEqual(len(load("domain.yml")["responses"]), 10)

    def test_all_intents_have_rules_and_valid_actions(self):
        domain = load("domain.yml")
        nlu_intents = {r["intent"] for r in load("data/nlu.yml")["nlu"] if "intent" in r}
        self.assertEqual(nlu_intents, set(domain["intents"]))
        rules = load("data/rules.yml")["rules"]
        rule_intents = {s["intent"] for r in rules for s in r["steps"] if "intent" in s}
        self.assertTrue(nlu_intents <= rule_intents)
        valid = set(domain["responses"]) | set(domain["actions"])
        for source in ["data/rules.yml", "data/stories.yml", "tests/test_stories.yml"]:
            for group in load(source).values():
                if not isinstance(group, list):
                    continue
                for story in group:
                    for step in story.get("steps", []):
                        if "action" in step:
                            self.assertIn(step["action"], valid)

    def test_evaluation_is_held_out(self):
        train = {plain(line.strip()[2:]) for r in load("data/nlu.yml")["nlu"] if "intent" in r
                 for line in r["examples"].splitlines() if line.strip().startswith("- ")}
        test_intents = set()
        for row in load("tests/nlu.yml")["nlu"]:
            test_intents.add(row["intent"])
            for line in row["examples"].splitlines():
                if line.strip().startswith("- "):
                    self.assertNotIn(plain(line.strip()[2:]), train)
        self.assertEqual(test_intents, set(load("domain.yml")["intents"]))

    def test_entities_declared(self):
        declared = set(load("domain.yml")["entities"])
        annotations = set(re.findall(r"\[[^]]+\]\(([^)]+)\)",
                                     (ROOT / "data/nlu.yml").read_text(encoding="utf-8")))
        self.assertTrue(annotations <= declared)

    def test_rasa_is_not_published_on_host(self):
        services = load("docker-compose.yml")["services"]
        self.assertNotIn("ports", services["rasa"])
        self.assertNotIn("ports", services["actions"])
        self.assertNotIn("--enable-api", services["rasa"]["command"])


if __name__ == "__main__":
    unittest.main()
