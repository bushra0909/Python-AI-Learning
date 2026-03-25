# Project: Day 2 - Functions with Return Values
# Concept: Functions, return statements, nested loops, list lookup

def catch_emotion():
    moods = {
        "happy": ["happy", "joy", "excited"],
        "sad": ["sad", "cry", "upset"],
        "angry": ["angry", "mad", "furious"]
    }

    moody = input("Enter your mood: ").lower()  # Step 1: Get input

    # Step 2: Loop through dictionary to detect mood
    for mood, words in moods.items():
        for word in words:  # check each keyword
            if word in moody:
                return mood  # return as soon as match is found

    return "emotion not detected"  # default if nothing matches

# Step 3: Call function
result = catch_emotion()
print(result)

"""
New Concepts Learned:
1. Return Statement: Sends value from function to outside.
2. Nested Loops: Loop inside another loop.
3. List Lookup in Dictionary: Searching for keywords in a sentence.
"""
