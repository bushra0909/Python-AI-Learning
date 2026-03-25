# Project: Day 1 - Functions & Simple Mood Detection
# Concept: Functions, Local Variables, and Dictionary Counting

# Step 1: Create dictionary to store moods
emotionals = {
    "happy": 0,
    "sad": 0,
    "angry": 0,
    "fear": 0
}

# Step 2: Define function to detect mood
def overall_mood(emotionals):
    user = input("Enter your mood: ").lower()  # get input
    words = user.split()  # split input into words

    # Step 3: Count moods
    for word in words:
        if word in emotionals:
            emotionals[word] += 1

    print("OH! You are:", emotionals)  # show detected moods

# Step 4: Call function
overall_mood(emotionals)

"""
New Concepts Learned:
1. Functions: Block of code reusable with a name.
2. Local Variables: Variables inside a function exist only there.
3. Dictionaries: Store mood counts as key-value pairs.
4. .split(): Splits a string into words.
"""
