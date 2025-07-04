# -*- coding: utf-8 -*-
"""v2.1.0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19pTy0RtznE4ADztL7dSnkxiVE13Bqqtu
"""

import json
from difflib import SequenceMatcher
from braille_dictionary import BRAILLE_DICTIONARY

# A file to store correction history
CORRECTION_FILE = "corrections.json"

# Load previous corrections
try:
    with open(CORRECTION_FILE, "r") as f:
        correction_history = json.load(f)
except FileNotFoundError:
    correction_history = {}

def save_corrections():
    with open(CORRECTION_FILE, "w") as f:
        json.dump(correction_history, f)

def parse_input(input_string):
    chars = input_string.strip().split()
    return [set(char.upper()) for char in chars]

def length_tolerant_match_score(input_seq, word_seq):
    input_seq_hashable = [tuple(sorted(s)) for s in input_seq]
    word_seq_hashable = [tuple(sorted(s)) for s in word_seq]

    matcher = SequenceMatcher(None, input_seq_hashable, word_seq_hashable, autojunk=False)
    score = 0
    for opcode, i1, i2, j1, j2 in matcher.get_opcodes():
        if opcode == 'equal':
            for inp, actual in zip(input_seq[i1:i2], word_seq[j1:j2]):
                score += len(inp & actual)
        elif opcode == 'replace':
            for inp, actual in zip(input_seq[i1:i2], word_seq[j1:j2]):
                score += len(inp & actual) // 2
        elif opcode in ['insert', 'delete']:
            score -= 1 * (i2 - i1 + j2 - j1)
    return score

def suggest_top_words(user_input, top_n=3):
    parsed_input = parse_input(user_input)
    input_key = " ".join(sorted("".join(sorted(c)) for c in parsed_input))

    scored_words = []
    remembered_word = None

    for word, pattern in BRAILLE_DICTIONARY.items():
        score = length_tolerant_match_score(parsed_input, pattern)

        # Boost if this word was previously corrected for this input
        if input_key in correction_history and correction_history[input_key] == word:
            score += 5
            remembered_word = word

        scored_words.append((score, word))

    scored_words.sort(reverse=True)
    top = [word for score, word in scored_words[:top_n] if score > 0]
    return top, remembered_word

def real_time_loop():
    while True:
        user_input = input("\nEnter Braille input (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        if user_input == "":
            continue

        suggestions, remembered_word = suggest_top_words(user_input)

        if suggestions:
            print("Suggestions:", suggestions)
            if remembered_word and remembered_word in suggestions:
                print(f"✅ Remembered from previous correction: your word might be '{remembered_word}'.")
        else:
            print("No match found.")

        corrected = input("Did you mean one of these? If not, type the correct word (or press ENTER if correct): ").strip().lower()
        if corrected and corrected not in suggestions:
            parsed_input = parse_input(user_input)
            input_key = " ".join(sorted("".join(sorted(c)) for c in parsed_input))
            correction_history[input_key] = corrected
            save_corrections()
            print("🧠 Thanks! We'll remember that for next time.")


if __name__ == "__main__":
    real_time_loop()

