# Project: Day 13 - Phrase Priority System in NLP Emotion Detection Upgrade
# Concepts:
# - Tokenization (NLTK)
# - Phrase detection (priority-wise)
# - Word-level detection
# - Negation handling (basic)
# - Emotion scoring system

# ------------------------------
# Step 1: Emotion dictionary (words + phrases)
# Priority-wise: phrases first, then single words
phrase_dict = {
    "happy": 2,
    "sad": -2,
    "angry": -3,
    "very happy": 4,
    "extremely happy": 6,
    "not happy": -2,
    "not very happy": -4,
    "not extremely happy": -6
}

# ------------------------------
# Step 2: Take user input
text = input("Enter how you are feeling: ").lower()  # lowercase for uniform matching

# ------------------------------
# Step 3: Tokenization (production-level)
import nltk
nltk.download('punkt')  # download tokenizer model first time only
from nltk.tokenize import word_tokenize

# Split text into words using NLTK's tokenizer
words = word_tokenize(text)  # converts text into list of words & punctuation

# Remove punctuation or numbers, keep only letters
words = [w for w in words if w.isalpha()]  
print("Tokens:", words)  # sanity check for tokens

# ------------------------------
# Step 4: Phrase detection (priority-wise)
score = 0  # running total of emotion score
detected = []  # list of detected phrases/words with score
used_words = set()  # track words used in phrases to avoid double-counting

# Detect multi-word phrases first
for phrase in phrase_dict:
    if " " in phrase and phrase in text:  # check only multi-word phrases
        value = phrase_dict[phrase]  # get score of phrase
        score += value  # add to total score
        detected.append((phrase, value))  # record detected phrase & its score

        # Mark words in phrase as used to avoid counting them again
        for w in phrase.split():
            used_words.add(w)

# ------------------------------
# Step 5: Word-level detection (single words)
for word in words:
    if word in used_words:  # skip words already counted in phrases
        continue #skip the rest of this loop iteration and move to the next word
    if word in phrase_dict:  # check if single word has emotion score
        value = phrase_dict[word]  # looks up phrase_dict["sad"] → -2
        score += value # adds -2 to the running score
        detected.append((word, value))  # record detected word & its score

# ------------------------------
# Step 6: Display results
print("\nDetected emotions and their scores:")
for item, val in detected:
    print(f"{item}: {val}")

# ------------------------------
# Step 7: Overall mood evaluation
print("\nOverall mood score:", score)
if score > 0:
    print("Mood is positive")
elif score < 0:
    print("Mood is negative")
else:
    print("Neutral mood")

# ------------------------------
# Notes / Visual Memory Recap:
# 1. Tokenize text into clean words (Step 3)
# 2. Detect multi-word phrases first (Step 4)
#    - Prevent double-counting by marking words as used
# 3. Detect single words not already counted (Step 5)
# 4. Keep running score & record detected emotions
# 5. Calculate final mood based on total score
# Detective analogy: phrases = big clues, words = leftover clues, score = final verdict

"""Why we use continue

If the word "happy" was already counted as part of "very happy", we don’t want to score it again

Without continue, you’d double-count "happy" → wrong total score

used_words + continue = safeguard against double-counting
"""
