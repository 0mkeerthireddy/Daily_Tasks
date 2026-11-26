# Daily Tasks – Python Internship

Daily Python assignments completed during my internship. Each day has its own folder with the source code, and a document with the explanations, sample outputs and screenshots is maintained alongside it.

**Author:** T. Om Keerthi

---

## Repository Structure

```
Daily_Tasks/
├── Day_1/
|   |-README.md
│   └── atm_banking_system.py   # Mini project: ATM Banking System
|
├── Day_2/
   ├README.md
   └── text_analyser.py        # Mini project: Advanced Text Analyser

```

---

## Progress

| Day | Topic | Mini Project | Status |
|-----|-------|--------------|--------|
| Day 1 | Loops and loop control statements | ATM Banking System | Completed |
| Day 2 | Python strings – indexing, slicing and string operations | Advanced Text Analyser | Completed |

---

## Day 1 – Loops and Loop Control Statements

**Concepts:** `for` loop, `while` loop, `range()`, nested loops, `break`, `continue`, `pass`, loop `else`.

**Exercises:** numbers 1–100, even/odd numbers, sum of 1 to N, multiplication table, factorial, prime check, star patterns, and `break` / `continue` / `pass` examples.

**Mini project – ATM Banking System** (`atm_banking_system.py`)
- Check balance, deposit money, withdraw money and view transaction history
- Validates the balance before every withdrawal
- Shows an error for invalid choices and keeps the menu running until Exit

---

## Day 2 – Python Strings

**Concepts:** string creation, positive and negative indexing, slicing, reversal, concatenation, repetition, immutability, escape sequences and raw strings, `len()`.

**Exercises** (`programs.py`): display a name, string length, first and last characters, slicing, reversing, joining, repeating, palindrome check, indexing, immutability, counting vowels and consonants, and counting uppercase, lowercase, digits and special characters.

**Mini project – Advanced Text Analyser** (`text_analyser.py`)
- **Character analysis:** total characters, uppercase, lowercase, digits, special characters, vowels and consonants
- **Word analysis:** total, longest and shortest words, duplicates, alphabetical order
- **Sentence analysis:** sentence count, longest and shortest sentence, average words per sentence
- **Search and replace:** count a word and replace it with another
- **Text transformation:** uppercase, lowercase, title case, reverse and palindrome check
- **Word frequency:** case-insensitive, ignores punctuation, shows the top 5 words
- **Complete report** and an interactive 10-option menu

---

## How to Run

**Requirements:** Python 3.8 or later. No external libraries are needed.

```bash
# Clone the repository
git clone <repository-url>
cd Daily_Tasks

# Run a program
cd Day_2
python text_analyser.py
```

Use `py` instead of `python` on Windows if `python` is not recognised. The programs are interactive, so enter the values when prompted.

---

## Sample Run – Advanced Text Analyser

```
======= ADVANCED TEXT ANALYSER =======

1. Enter Text
2. Character Analysis
3. Word Analysis
4. Sentence Analysis
5. Search a Word
6. Replace a Word
7. Text Transformation
8. Display Word Frequency
9. Display Complete Report
10. Exit

Enter Your Choice: 1
Enter a paragraph: Python is easy. Python is fun!
Text entered successfully!
```

---

## Notes

- All code is written independently as part of the daily internship tasks.
- The daily task document (with explanations, sample outputs and screenshots) is submitted along with the code.