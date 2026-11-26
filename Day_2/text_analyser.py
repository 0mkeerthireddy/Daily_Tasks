import re
import string

text = ""   # the paragraph; empty until the user enters it


# ---------- helper functions ----------

def get_words(t):
    """Return a list of lowercase words with punctuation removed."""
    words = []
    for w in t.split():
        w = w.strip(string.punctuation).lower()
        if w != "":
            words.append(w)
    return words


def get_sentences(t):
    """Split the text into sentences using . ! and ?"""
    t = t.replace("!", ".").replace("?", ".")
    sentences = []
    for s in t.split("."):
        s = s.strip()
        if s != "":
            sentences.append(s)
    return sentences


def count_frequency(words):
    """Return a dictionary {word: count}."""
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq


def sorted_frequency(freq):
    """Return (word, count) pairs, highest count first, then alphabetical."""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


# ---------- A. Text input ----------

def enter_text():
    raw = input("Enter a paragraph: ")
    cleaned = " ".join(raw.split())          # removes extra spaces
    if cleaned == "":
        print("Error: input cannot be empty.")
        return ""
    print("Text entered successfully!")
    return cleaned


# ---------- B. Character analysis ----------

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
        elif not ch.isalnum() and not ch.isspace():
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


# ---------- C. Word analysis ----------

def word_analysis(t):
    words = get_words(t)
    if len(words) == 0:
        print("No words found.")
        return

    longest = words[0]
    shortest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
        if len(w) < len(shortest):
            shortest = w

    freq = count_frequency(words)
    duplicates = []
    for w in sorted(freq):
        if freq[w] > 1:
            duplicates.append(w)

    print("\n===== WORD ANALYSIS =====")
    print("Total words:", len(words))
    print("Longest word:", longest)
    print("Shortest word:", shortest)
    if len(duplicates) == 0:
        print("Duplicate words: None")
    else:
        print("Duplicate words:", ", ".join(duplicates))
    print("Words in alphabetical order:", ", ".join(sorted(words)))


# ---------- D. Sentence analysis ----------

def sentence_analysis(t):
    sentences = get_sentences(t)
    if len(sentences) == 0:
        print("No sentences found.")
        return

    longest = sentences[0]
    shortest = sentences[0]
    total_words = 0
    for s in sentences:
        total_words += len(s.split())
        if len(s.split()) > len(longest.split()):
            longest = s
        if len(s.split()) < len(shortest.split()):
            shortest = s

    average = total_words / len(sentences)

    print("\n===== SENTENCE ANALYSIS =====")
    print("Total sentences:", len(sentences))
    print("Longest sentence:", longest)
    print("Shortest sentence:", shortest)
    print("Average words per sentence:", round(average, 2))


# ---------- E. Search and replace ----------

def search_word(t):
    word = input("Enter the word to search: ").strip()
    if word == "":
        print("Error: word cannot be empty.")
        return
    pattern = r"\b" + re.escape(word) + r"\b"
    count = len(re.findall(pattern, t, flags=re.IGNORECASE))
    if count == 0:
        print("The word '" + word + "' was not found.")
    else:
        print("The word '" + word + "' appears", count, "time(s).")


def replace_word(t):
    old = input("Enter the word to replace: ").strip()
    new = input("Enter the new word: ").strip()
    if old == "" or new == "":
        print("Error: words cannot be empty.")
        return t
    pattern = r"\b" + re.escape(old) + r"\b"
    if len(re.findall(pattern, t, flags=re.IGNORECASE)) == 0:
        print("The word '" + old + "' was not found. Nothing replaced.")
        return t
    updated = re.sub(pattern, new, t, flags=re.IGNORECASE)
    print("\nUpdated paragraph:")
    print(updated)
    return updated


# ---------- F. Text transformation ----------

def text_transformation(t):
    print("\n===== TEXT TRANSFORMATION =====")
    print("Uppercase :", t.upper())
    print("Lowercase :", t.lower())

    title_words = []
    for w in t.split():
        title_words.append(w.capitalize())
    print("Title case:", " ".join(title_words))

    print("Reversed  :", t[::-1])

    word = input("\nEnter a word to check for palindrome: ").strip()
    if word == "":
        print("Error: word cannot be empty.")
    elif word.lower() == word.lower()[::-1]:
        print(word, "is a palindrome.")
    else:
        print(word, "is not a palindrome.")


# ---------- 8. Word frequency ----------

def word_frequency(t):
    words = get_words(t)
    if len(words) == 0:
        print("No words found.")
        return
    pairs = sorted_frequency(count_frequency(words))

    print("\n===== WORD FREQUENCY =====")
    for word, count in pairs:
        print(f"{word:<15} {count}")

    print("\nTop 5 most frequent words:")
    rank = 1
    for word, count in pairs[:5]:
        print(f"{rank}. {word} ({count})")
        rank += 1


# ---------- 9. Complete report ----------

def complete_report(t):
    print("\n======= COMPLETE REPORT =======")
    print("\nParagraph:")
    print(t)
    character_analysis(t)
    word_analysis(t)
    sentence_analysis(t)
    word_frequency(t)


# ---------- G. Interactive menu ----------

while True:
    print("\n======= ADVANCED TEXT ANALYSER =======\n")
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
        if result != "":
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
