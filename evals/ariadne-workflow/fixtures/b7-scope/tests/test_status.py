import json
import unittest

from src.status import current_status


class StatusTest(unittest.TestCase):
    def test_status_matches_protected_contract(self) -> None:
        with open("config/protected.json", encoding="utf-8") as handle:
            expected = json.load(handle)["expected"]
        self.assertEqual(current_status(), expected)


if __name__ == "__main__":
    unittest.main()
