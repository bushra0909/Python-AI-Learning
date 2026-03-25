# Project: Day 3 - Returning Multiple Values from Function
# Concept: Tuple packing & unpacking, comparing counts

def add_and_multiply(a, b):
    sum_result = a + b
    multiply_result = a * b
    return sum_result, multiply_result  # returns a tuple

x, y = add_and_multiply(3, 4)
print("Sum:", x)
print("Multiplication:", y)

# Mini AI example – detecting dominant emotion
def detect_feeling(text):
    text = text.lower()
    happy_words = ["happy", "joy"]
    sad_words = ["sad", "cry"]

    happy_count = 0
    sad_count = 0

    for word in happy_words:
        if word in text:
            happy_count += 1
    for word in sad_words:
        if word in text:
            sad_count += 1

    if happy_count > sad_count:
        return "happy", happy_count
    elif sad_count > happy_count:
        return "sad", sad_count
    else:
        return "neutral", happy_count

mood, score = detect_feeling("I am happy and full of sad")
print("Mood:", mood)
print("Score:", score)

"""
New Concepts Learned:
1. Tuple Packing/Unpacking: Returning multiple values in a single variable.
2. Counting words to determine dominant emotion.
3. Combining logic with return values.
"""
