

from braille_dictionary import BRAILLE_DICTIONARY
from difflib import SequenceMatcher

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
                score += len(inp & actual) // 2  # penalized partial match
        elif opcode in ['insert', 'delete']:
            score -= 1 * (i2 - i1 + j2 - j1)

    return score


def suggest_top_words(user_input, top_n=3):
    parsed_input = parse_input(user_input)
    scored_words = []

    for word, pattern in BRAILLE_DICTIONARY.items():
        score = length_tolerant_match_score(parsed_input, pattern)
        scored_words.append((score, word))

    scored_words.sort(reverse=True)
    return [word for score, word in scored_words[:top_n] if score > 0]

def real_time_loop():
    print("Real-time Braille suggestion (type space-separated keys like 'D K DOP'):")
    current_input = ""
    while True:
        char = input("Add Braille character (or ENTER to reset, 'exit' to quit): ").strip()
        if char.lower() == 'exit':
            break
        if not char:
            current_input = ""
            continue
        current_input += f"{char} "
        suggestions = suggest_top_words(current_input)
        print("Top suggestions:", ", ".join(suggestions) if suggestions else "No match yet.")

if __name__ == "__main__":
    real_time_loop()


