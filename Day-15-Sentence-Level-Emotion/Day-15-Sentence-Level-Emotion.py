# Project: Day 15 - Sentence-Level Emotion Detection
# Concepts:
# - Sentence tokenization (NLTK)
# - Word tokenization
# - Phrase-level emotion detection (priority first)
# - Word-level detection
# - Avoid double-counting using used_words
# - Emotion scoring per sentence

from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')  # download tokenizer (only needed first time)

# ------------------------------
# Step 1: Emotion dictionaries

# Multi-word phrases (HIGH priority)
phrase_dict = {
    "very happy": 4,
    "very sad": -4,
    "extremely happy": 6,
    "extremely sad": -6,
    "not happy": -2,
    "not sad": 2,
    "not very happy": -4,
    "not very sad": 4,
    "not extremely happy": -6,
    "not extremely sad": 6
}

# Single-word emotions
word_dict = {
    "happy": 2,
    "sad": -2,
    "angry": -3
}

# ------------------------------
# Step 2: Take user input
text = input("Enter text: ").lower()  # convert to lowercase for consistent matching

# ------------------------------
# Step 3: Split text into sentences
sentences = sent_tokenize(text)

# ------------------------------
# Step 4: Process each sentence separately
for sentence in sentences:
    print("Sentence:", sentence)
    
    # Tokenize sentence into words
    words = word_tokenize(sentence)
    # Keep only alphabetic words (remove punctuation/numbers)
    words = [w for w in words if w.isalpha()]
    
    # Initialize variables for this sentence
    score = 0
    detected = []
    used_words = set()  # tracks words already used in phrases
    
    # ------------------------------
    # Step 5: Phrase detection (PRIORITY FIRST)
    for phrase in phrase_dict:
        if phrase in sentence:
            value = phrase_dict[phrase]
            score += value
            detected.append((phrase, value))
            # Mark words in phrase as used to avoid double-counting
            for w in phrase.split():
                used_words.add(w)
    
    # ------------------------------
    # Step 6: Word detection (skip used words)
    for word in words:
        if word in used_words:
            continue
        if word in word_dict:
            value = word_dict[word]
            score += value
            detected.append((word, value))
    
    # ------------------------------
    # Step 7: Display results for this sentence
    print("Detected:", detected)
    print("Score:", score)
    
    # ------------------------------
    # Step 8: Mood classification
    if score > 0:
        print("Mood: Positive 😊")
    elif score < 0:
        print("Mood: Negative 😢")
    else:
        print("Mood: Neutral 😐")

# ------------------------------
# Notes / Memory Recap:
# 1. Split text into sentences → analyze each separately
# 2. Detect phrases first (higher priority)
# 3. Mark words from phrases → avoid double-counting
# 4. Detect remaining words
# 5. Calculate score per sentence → assign mood

"""
Memory Trick:
sent_tokenize → splits paragraph into sentences

Flow:
Text → Sentences → Words → Phrase detection → Word detection → Score → Mood

Detective analogy:
Each sentence = separate case
Phrases = strong clues
Words = small clues
Score = final verdict for each case

in list comprehension 
[w for w in words if w.isalpha()]
First w → “take this and put it in the new list”
Second w → “this is the loop variable”"""