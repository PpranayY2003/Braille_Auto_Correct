# Braille Auto-Correct and Suggestion System

## <b>Description</b>

This project implements a basic auto-correct and suggestion system for Braille input typed via a standard QWERTY keyboard. The system accepts sequences of Braille dot key combinations (mapped to QWERTY keys) and returns the closest matching word(s) from a predefined dictionary.

Currently, suggestions are based on a custom scoring algorithm using dot-pattern overlap. The design is modular and optimized for future enhancement.

## <b>Tech Used</b>

- Python 3
- No external libraries required for the current version
- Designed for extensibility with future support for:
  - Levenshtein distance
  - Trie-based search
  - User feedback learning

## <b>Files</b>

- <b>main.py</b> – Handles user input, matching logic, and suggestions
- <b>braille_mapping.py</b> – Defines QWERTY key mapping for Braille dots
- <b>braille_dictionary.py</b> – Converts words to Braille key sequences
- <b>writeup.txt</b> – Explanation of the system, test cases, and future plans

## <b>Current Features</b>

- Accepts Braille-like input using QWERTY keys (D, W, Q, K, O, P)
- Parses multi-character Braille sequences into QWERTY dot sets
- Compares input sequences with known Braille representations of dictionary words
- Returns the <b>top 3 most similar suggestions</b> based on dot overlap score

## <b>Planned Features</b>

- <b>Length-tolerant matching:</b> Gracefully handle input with missing or extra characters
- <b>Real-time suggestions:</b> Display suggestions as characters are typed
- <b>Learning from user corrections:</b> Track mistakes and improve future predictions
- <b>Efficient search:</b> Integration of Levenshtein distance or Trie structures for larger datasets
- <b>GUI/Web interface:</b> Optional accessible front-end for Braille users

## <b>Author</b>

<b>Name:</b> Pranay Malhotra
<b>Email:</b> pranaymalhotra2003@gmail.com  
<b>LinkedIn:</b> https://www.linkedin.com/in/pranay-malhotra-190818343/


