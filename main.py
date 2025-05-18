from braille_dictionary import BRAILLE_DICTIONARY

def parse_input(input_string):
    chars = input_string.strip().split()
    return [set(char.upper()) for char in chars]

def match_score(input_seq, word_seq):
    if len(input_seq) != len(word_seq):
        return 0
    return sum(len(inp & actual) for inp, actual in zip(input_seq, word_seq))

def suggest_top_words(user_input, top_n=3):
    parsed_input = parse_input(user_input)
    scored_words = []

    for word, pattern in BRAILLE_DICTIONARY.items():
        score = match_score(parsed_input, pattern)
        scored_words.append((score, word))

    scored_words.sort(reverse=True)
    return [word for score, word in scored_words[:top_n] if score > 0]

if __name__ == "__main__":
    user_input = input("Enter Braille input (e.g., DK DOP DKP): ")
    suggestions = suggest_top_words(user_input)
    print("Top suggestions:", ", ".join(suggestions) if suggestions else "No match found.")

