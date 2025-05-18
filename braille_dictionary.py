from braille_mapping import LETTER_TO_KEYS

WORDS = [
    "hello", "help", "apple", "cat", "cab", "bat", "dog", "dot", "cap", "cup", "cut",
    "bad", "dad", "bag", "bug", "cot", "cop", "top", "tap", "pat", "pod"
]

def word_to_braille(word):
    return [LETTER_TO_KEYS[char] for char in word]

BRAILLE_DICTIONARY = {word: word_to_braille(word) for word in WORDS}

