
import re
import string

text = ""


# ---------- Helper Functions ----------

def get_words(t):
    """Return lowercase words without punctuation."""
    words = re.findall(r"\b[\w']+\b", t.lower())
    return words


def get_sentences(t):
    """Split text into sentences."""
    sentences = re.split(r'(?<=[.!?])\s+', t.strip())
    return [s.strip() for s in sentences if s.strip()]


def count_frequency(words):
    """Count frequency of each word."""
    freq = {}

    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return freq


def sorted_frequency(freq):
    """Sort by frequency and then alphabetically."""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


# ---------- 1. Text Input ----------

def enter_text():
    print("\nEnter your paragraph.")
    print("Press Enter on an empty line to finish:")

    lines = []

    while True:
        line = input()

        if line == "":
            break

        lines.append(line)

    cleaned = " ".join(" ".join(lines).split())

    if cleaned == "":
        print("Error: Input cannot be empty.")
        return ""

    print("Text entered successfully!")
    return cleaned


# ---------- 2. Character Analysis ----------

def character_analysis(t):
    total = len(t)
    without_spaces = 0
    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0
    vowels = 0
    consonants = 0

    for ch in t:

        if not ch.isspace():
            without_spaces += 1

        if ch.isupper():
            uppercase += 1
        elif ch.islower():
            lowercase += 1
        elif ch.isdigit():
            digits += 1

        if not ch.isalnum() and not ch.isspace():
            special += 1

        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("\n===== CHARACTER ANALYSIS =====")
    print("Total characters:", total)
    print("Characters without spaces:", without_spaces)
    print("Uppercase letters:", uppercase)
    print("Lowercase letters:", lowercase)
    print("Digits:", digits)
    print("Special characters:", special)
    print("Vowels:", vowels)
    print("Consonants:", consonants)


# ---------- 3. Word Analysis ----------

def word_analysis(t):
    words = get_words(t)

    if not words:
        print("No words found.")
        return

    longest = max(words, key=len)
    shortest = min(words, key=len)

    freq = count_frequency(words)

    duplicates = []

    for w in sorted(freq):
        if freq[w] > 1:
            duplicates.append(w)

    print("\n===== WORD ANALYSIS =====")
    print("Total words:", len(words))
    print("Longest word:", longest)
    print("Shortest word:", shortest)

    if duplicates:
        print("Duplicate words:", ", ".join(duplicates))
    else:
        print("Duplicate words: None")

    print("Words in alphabetical order:", ", ".join(sorted(words)))


# ---------- 4. Sentence Analysis ----------

def sentence_analysis(t):
    sentences = get_sentences(t)

    if not sentences:
        print("No sentences found.")
        return

    longest = max(sentences, key=lambda s: len(s.split()))
    shortest = min(sentences, key=lambda s: len(s.split()))

    total_words = sum(len(s.split()) for s in sentences)

    average = total_words / len(sentences)

    print("\n===== SENTENCE ANALYSIS =====")
    print("Total sentences:", len(sentences))
    print("Longest sentence:", longest)
    print("Shortest sentence:", shortest)
    print("Average words per sentence:", round(average, 2))


# ---------- 5. Search a Word ----------

def search_word(t):
    word = input("Enter the word to search: ").strip()

    if not word:
        print("Error: Word cannot be empty.")
        return

    pattern = r"\b" + re.escape(word) + r"\b"

    count = len(re.findall(pattern, t, flags=re.IGNORECASE))

    if count == 0:
        print("Word not found.")
    else:
        print("The word", word, "appears", count, "time(s).")


# ---------- 6. Replace a Word ----------

def replace_word(t):
    old = input("Enter the word to replace: ").strip()
    new = input("Enter the new word: ").strip()

    if not old or not new:
        print("Error: Words cannot be empty.")
        return t

    pattern = r"\b" + re.escape(old) + r"\b"

    if not re.search(pattern, t, flags=re.IGNORECASE):
        print("Word not found. Nothing replaced.")
        return t

    updated = re.sub(pattern, lambda match: new, t,
                     flags=re.IGNORECASE)

    print("\nUpdated paragraph:")
    print(updated)

    return updated


# ---------- 7. Text Transformation ----------

def text_transformation(t):
    print("\n===== TEXT TRANSFORMATION =====")

    print("Uppercase :", t.upper())
    print("Lowercase :", t.lower())
    print("Title case:", t.title())
    print("Reversed  :", t[::-1])

    word = input("\nEnter a word to check palindrome: ").strip()

    if not word:
        print("Error: Word cannot be empty.")
        return

    cleaned = "".join(ch.lower() for ch in word if ch.isalnum())

    if cleaned == cleaned[::-1]:
        print(word, "is a palindrome.")
    else:
        print(word, "is not a palindrome.")


# ---------- 8. Word Frequency ----------

def word_frequency(t):
    words = get_words(t)

    if not words:
        print("No words found.")
        return

    freq = count_frequency(words)
    pairs = sorted_frequency(freq)

    print("\n===== WORD FREQUENCY =====")

    for word, count in pairs:
        print(f"{word:<15} {count}")

    print("\nTop 5 Most Frequent Words:")

    for rank, (word, count) in enumerate(pairs[:5], start=1):
        print(f"{rank}. {word} ({count})")


# ---------- 9. Complete Report ----------

def complete_report(t):
    print("\n======= COMPLETE REPORT =======")

    print("\nParagraph:")
    print(t)

    character_analysis(t)
    word_analysis(t)
    sentence_analysis(t)
    word_frequency(t)


# ---------- 10. Interactive Menu ----------

while True:

    print("\n======= ADVANCED TEXT ANALYSER =======")
    print("1. Enter Text")
    print("2. Character Analysis")
    print("3. Word Analysis")
    print("4. Sentence Analysis")
    print("5. Search a Word")
    print("6. Replace a Word")
    print("7. Text Transformation")
    print("8. Display Word Frequency")
    print("9. Display Complete Report")
    print("10. Exit")

    choice = input("\nEnter Your Choice: ").strip()

    if choice == "1":
        result = enter_text()

        if result:
            text = result

    elif choice == "10":
        print("Thank you for using the Advanced Text Analyser!")
        break

    elif choice in ["2", "3", "4", "5", "6", "7", "8", "9"]:

        if text == "":
            print("Please enter text first (option 1).")

        elif choice == "2":
            character_analysis(text)

        elif choice == "3":
            word_analysis(text)

        elif choice == "4":
            sentence_analysis(text)

        elif choice == "5":
            search_word(text)

        elif choice == "6":
            text = replace_word(text)

        elif choice == "7":
            text_transformation(text)

        elif choice == "8":
            word_frequency(text)

        elif choice == "9":
            complete_report(text)

    else:
        print("Invalid choice! Please select 1 to 10.")
