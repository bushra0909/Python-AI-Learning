# Project: Day 14 - Emotion Detection Improvement
# Concepts:
# - Tokenization (NLTK)
# - Phrase detection (priority first)
# - Word-level detection
# - Avoid double-counting using used_words
# - Clean scoring system
# - Improved output formatting

# ------------------------------
# Step 1: Emotion dictionaries

# Multi-word phrases (HIGH priority)
phrase_dict = {
    "very happy": 4,
    "extremely happy": 6,
    "not happy": -2,
    "not very happy": -4,
    "not extremely happy": -6
}

word_dict = {
    "happy": 2,
    "sad": -2,
    "angry": -3
}
# ------------------------------
# Step 2: Take user input
text = input("Enter how you are feeling: ").lower()
# ------------------------------
# Step 3: Tokenization
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
words=word_tokenize(text)
words=[w for w in words if w.isalpha()]
print("Tokens:", words)

# ------------------------------
# Step 4: Initialize variables
score = 0
detected = []
used_words=set() #Why set() specifically:A set only stores unique items → avoids duplicates automatically
# ------------------------------
# Step 5: Phrase detection (PRIORITY FIRST)
for phrase in phrase_dict:
    if phrase in text:
        value=phrase_dict[phrase]
        score+=value
        detected.append((phrase,value))
#mark words as used (add them in usedwords variable to avoid repetitive counting)
for w in phrase.split():
    used_words.add(w)
# ------------------------------
# Step 6: Word detection (skip used words)
for word in word_dict:
    if word in text:
        value=word_dict[word]
        score+=value
        detected.append((word,value))

# ------------------------------
# Step 7: Display detected emotions
print("\nDetected emotions:")
for item ,val in  detected:
    print(f"Detected-> ${item}: ${val}")
    # ------------------------------
# Step 8: Final score
print("\nTotal Score:", score)

# ------------------------------
# Step 9: Mood classification
if score > 0:
    print("Mood: Positive 😊")
elif score < 0:
    print("Mood: Negative 😢")
else:
    print("Mood: Neutral 😐")

# ------------------------------
# Notes:
# - Phrases are detected first (higher priority)
# - used_words prevents double-counting
# - Words already in phrases are skipped
# - Clean output improves readability

"""
Memory Shortcut:
used_words = set() → prevents counting the same word twice

Flow:
Text → Tokenize → Detect phrases → Mark words → Detect remaining words → Score → Mood
"""





