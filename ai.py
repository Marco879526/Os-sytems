#!/usr/bin/env python3
"""Jednoduchá lokální AI konzole v češtině."""

from __future__ import annotations

import argparse
import re
from datetime import datetime


class MiniAI:
    """Malý pravidlový asistent bez externích závislostí."""

    def __init__(self) -> None:
        self.name = "MiniAI"
        self._positive_words = {"super", "skvělé", "dobré", "díky", "paráda"}
        self._negative_words = {"špatné", "hrozné", "bolí", "naštvaný", "smutný"}

    def reply(self, message: str) -> str:
        text = message.strip()
        if not text:
            return "Napiš mi prosím nějakou otázku nebo zprávu."

        lower = text.lower()

        if lower in {"ahoj", "čau", "dobrý den"}:
            return "Ahoj! Jsem MiniAI. Jak ti mohu pomoct?"

        if "kolik je hodin" in lower or "čas" == lower:
            return f"Aktuální čas je {datetime.now().strftime('%H:%M')}"

        if lower.startswith("spočítej"):
            return self._calculate(lower.removeprefix("spočítej").strip())

        sentiment = self._sentiment(lower)
        if sentiment > 0:
            return "To zní pozitivně — rád to slyším!"
        if sentiment < 0:
            return "Mrzí mě, že to není ideální. Chceš s tím pomoct?"

        return (
            "Rozumím. Zkus se zeptat konkrétněji, třeba: "
            "'spočítej 12 * (3 + 1)' nebo 'kolik je hodin'."
        )

    def _sentiment(self, text: str) -> int:
        words = set(re.findall(r"[a-zá-ž]+", text.lower()))
        score = len(words & self._positive_words) - len(words & self._negative_words)
        return score

    def _calculate(self, expression: str) -> str:
        if not expression:
            return "Napiš výraz po slově 'spočítej', např. 'spočítej 2+2'."

        if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
            return "Umím počítat jen základní matematické výrazy."

        try:
            result = eval(expression, {"__builtins__": {}}, {})
        except Exception:
            return "Tento výraz nejde spočítat."

        return f"Výsledek je {result}."


def preview_conversation(ai: MiniAI) -> None:
    """Krátký náhled chování bez interaktivního psaní."""
    samples = [
        "ahoj",
        "spočítej 12 * (3 + 1)",
        "to je super",
        "konec",
    ]
    print("MiniAI: Ahoj! Tohle je rychlý náhled.")
    for message in samples:
        print(f"Ty: {message}")
        if message == "konec":
            print("MiniAI: Měj se hezky!")
            return
        print(f"MiniAI: {ai.reply(message)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="MiniAI asistent")
    parser.add_argument(
        "--preview",
        action="store_true",
        help="spustí krátký neinteraktivní náhled",
    )
    args = parser.parse_args()

    ai = MiniAI()

    if args.preview:
        preview_conversation(ai)
        return

    print("MiniAI: Ahoj! Napiš 'konec' pro ukončení.")
    while True:
        user = input("Ty: ")
        if user.strip().lower() in {"konec", "exit", "quit"}:
            print("MiniAI: Měj se hezky!")
            break
        print(f"MiniAI: {ai.reply(user)}")


if __name__ == "__main__":
    main()
