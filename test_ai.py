import subprocess
import sys
import unittest

from ai import MiniAI


class MiniAITest(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = MiniAI()

    def test_greeting(self):
        self.assertIn("Ahoj", self.ai.reply("ahoj"))

    def test_calculation(self):
        self.assertEqual("Výsledek je 8.", self.ai.reply("spočítej 2*4"))

    def test_invalid_calculation(self):
        self.assertEqual(
            "Umím počítat jen základní matematické výrazy.",
            self.ai.reply("spočítej import os"),
        )

    def test_preview_mode(self):
        result = subprocess.run(
            [sys.executable, "ai.py", "--preview"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("rychlý náhled", result.stdout)
        self.assertIn("Ty: spočítej 12 * (3 + 1)", result.stdout)


if __name__ == "__main__":
    unittest.main()
