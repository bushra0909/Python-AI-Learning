#DAY 5 (27 FEB)
#FUNCTIONS
#lets perform some mood detectipon using functions
   
emotionals={
    "happy": 0,
    "sad": 0,
    "angry": 0,
    "fear": 0
}
def overall_mood(emotionals):
  user=input("Enter your mood: ").lower()
  words=user.split()

  for word in words:
      if word in emotionals:
       emotionals[word] += 1
     
  print("OH! You are: ",emotionals)
overall_mood(emotionals)
      
"""#What “scope” means

#A variable created inside a function is local — it only exists inside that function.

#Outside the function, Python doesn’t know about it.

#If you want to use it outside, you have to return it or pass it somewhere.

Example 1 — Local variable (doesn’t exist outside)
def my_function():
    secret = 42  # this variable exists only inside the function
    print("Inside function:", secret)

my_function()

# Trying to use it outside:
print(secret)  # ❌ ERROR: secret is not defined outside

Output:

Inside function: 42
NameError: name 'secret' is not defined

✅ Lesson: secret is local to the function.

Example 2 — Using return to access variable outside
def my_function():
    secret = 42
    return secret  # send the value outside

value = my_function()  # catch the returned value
print("Outside function:", value)"""
# lets do one mmores eaxmpleusing function but this tiem using return
#DAY 6 (28 FEB 2026)
def catch_emotion():
     moods={
        "happy": ["happy", "joy", "excited"],
        "sad": ["sad", "cry", "upset"],
        "angry": ["angry", "mad", "furious"]
    }
     moody=input("Enter you mood: ").lower()
     for mood, words in moods.items():
         for word in words:
             if word in words:
                 return mood

     return "emotion not detected"

result = catch_emotion()
print(result)
           
   #Easy memory:

#Parameter = placeholder

#Argument = real value
     #What is a default parameter?

 #A parameter that already has a value if user doesn’t give one

#Example:

def greet(name="friend"):
    print("Hello", name)

#Calls:

greet()          # uses default → friend
greet("Bushra")  # overrides default
    
def catch_emotion(text):  # function receives a sentence

    # dictionary: mood → list of related words
    moods = {
        "happy": ["happy", "joy", "excited"],
        "sad": ["sad", "cry", "upset"],
        "angry": ["angry", "mad", "furious"]
    }

    text = text.lower()  # normalize input for matching

    # 🔁 OUTER LOOP
    # mood = key ("happy")
    # words = value (["happy","joy","excited"])
    for mood, words in moods.items():

        # 🔁 INNER LOOP
        # word becomes each item inside the list
        for word in words:

            # ✅ check if that word exists in the sentence
            if word in text:
                return mood  # return the detected emotion

    return "unknown"  # if nothing matched


# 🔹 function call
result = catch_emotion("I am very happy today")

print(result)
#DAY 7(2 MARCH 2026)
#Lets see what happenswhen we return multiple values from a function
def add_and_multiply(a, b):
    sum_result = a + b
    multiply_result = a * b
    return sum_result, multiply_result
x, y = add_and_multiply(3, 4)

print(x)  # 7
print(y)  # 12
## 🧠 What Just Happened?

#When we wrote:

#return sum_result, multiply_result

#Python automatically packed them into a **tuple**:


(7, 12)

#Then this line:

#python
#x, y = add_and_multiply(3, 4)
##Unpacked them.
#🌱 Small AI-Style Example
def detect_feeling(text):
    text.lower()
    happy_words = ["happy", "joy"]
    sad_words = ["sad", "cry"]
    happy_count=0
    sad_count=0
    for word in happy_words:
        if word in text:
            happy_count += 1
    #Similarly for sad words count

    for word in sad_words:
        if word in text:
            sad_count += 1
    
#lets create a twist that the word hwose count in text is hreater will be printed
    if happy_count > sad_count:
        return "happy", happy_count
    
    elif sad_count > happy_count:
        return "sad", sad_count
    
    else:
        return "neutral", happy_count

    #call
#res= detect_feeling("i am very happy happy but also sad sad")
#print(res)
#Another way to call it
mood, score = detect_feeling("I am happy and full of sad")

print(mood)   # happy
print(score)  # 2
def test():
    return 5, 10
a,b=test()
print(a) #5 #This is called tuple unpacking(Answer was in form of tuple(5,10) this code just seperateor unpacks it)
print(b) #10

#DAY 8 (3 MARCH 2026)
#MINI ai will find tghe word for us in mood dictionary

def my_emotion():

    mood_dict = {
        "happy": "Happy",
        "sad": "Sad",
        "angry": "Angry"
    }

    text = "i am upset"
    words = text.lower().split()
    found = False   # 👈 flag variable
    for word in words:
        if word in mood_dict:
            print("Found", mood_dict[word])
            found=True
       #change else to  if not found:
    if not found: 
             print("WORD NOT FOUND!")

my_emotion()
#we will use a flagvariable as i want my program to print else statement only once


#DAY 9(4 MARCH ,2026)
"""Easy → Fun → Useful for AI)

Today we are going to:

Clean text (remove punctuation)

Convert text to lowercase

Split text into words (tokenization)

Prepare it properly for AI systems

And we’ll go slow and simple 😌

🌱 Step 1: Why This Is Important for AI?

In real AI systems:

Raw text = ❌ messy
Clean text = ✅ useful

Example:

"I am HAPPY!!!"

AI should understand this same as:

"i am happy"

So we clean before analyzing.

🧼 Step 2: Lowercase (Super Easy)
text = "I Am HAPPY"
clean_text = text.lower()
print(clean_text)

👉 Why?
Because "Happy" and "happy" should be treated the same.

✂ Step 3: Remove Punctuation

Problem:

"I am happy!!!"

Word becomes "happy!!!"
Dictionary only has "happy"

So we remove punctuation.

Easy beginner way:

import string

text = "I am happy!!!"
text = text.lower()

for p in string.punctuation:
    text = text.replace(p, "")

print(text)

Now output:

i am happy
🧩 Step 4: Tokenization (Split into Words)

Tokenization = breaking sentence into words.

words = text.split()
print(words)

Output:

['i', 'am', 'happy']

Now your AI can check each word easily.

🧠 Combine Everything (Mini Clean AI Input)
import string

def preprocess(text):
    text = text.lower()

    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()
    return words


sentence = "I am VERY happy!!!"
clean_words = preprocess(sentence)

print(clean_words)

Output:

['i', 'am', 'very', 'happy']

Now your mini AI is becoming REAL AI 🔥

🎯 Why This Matters for YOUR Goal

For animal emotion detection:

Animal sound → converted to text → cleaned

Social media cruelty report → cleaned

Vet notes → cleaned

Multi-modal system → clean text before combining with image/audio features

This is exactly how professional NLP pipelines start.

🏆 You Just Learned

Lowercasing

Punctuation removal

Tokenization

Text preprocessing pipeline

This is real NLP foundation.

🧩 Mini Fun Task For You

Modify the function so it also:

Counts how many words are in the sentence

Just add 1 line inside function.

"""
#lets do it
import string #string module=We are telling Python:👉 “Give me extra text tools.”
def preprocess(user_data):
    txt=user_data.lower() ## Convert all text to lowercase (AI treats Happy & happy same)
    #REmove punctuation marks like "!,?,/" (Data Cleaning)
    for p in string.punctuation: #Go through each punctuation mark one by one.
         txt = txt.replace(p,"") ## create new cleaned string & reassign (strings are immutable)
         wrd=txt.split() #Split sentence into list of words (tokenization)
        
    return wrd   # Return clean list of words


sentencee = "I am VERY happy!!!"
clean_words = preprocess(sentencee)

print(clean_words)   # Print processed words
"""
💎 Super Important Concept You Just Learned

Strings are immutable(original is unchangable,if you cahnge it using thes methods it will be created as a copy not the original one changes )
So methods like:

.replace()

.lower()

.upper()

.strip()

Return new strings.

They do NOT modify original one.
"""
#DAY 10(5 March 2026)
"""Today’s concept is Weighted Mood Scoring.

Instead of just checking if a word exists, the AI will understand how strong the emotion is.

Example
“happy” → small positive feeling
“very happy” → stronger feeling"""
#lets do  it

import string
user_text=input("Enter input: ").lower()
#remove punctuation

user_text=user_text.translate(str.maketrans("", "", string.punctuation)) ## This line removes all punctuation (like !, ?, .) from user_text by 'mapping' them to None
#Tokenization
text_word=user_text.split()
weights = {
    "happy": 1,
    "very happy": 2,
    "sad": -1,
    "very sad": -2
}
score=0
"""for word in text_word:
    if word in weights:
       score+=weights[word]
print("Emotion Score:", score)
if score>0:
  print("Overall Mood: Positive")
elif score<0:
  print("Overall Mood: Negative")
else:
    print("Overall Mood: Neutral")"""
"""
string.punctuation: This is just a pre-made list of all standard symbols (like !, @, #, $, etc.). Think of it as a "Most Wanted" list of characters we want to remove.

str.maketrans("", "", string.punctuation): This creates a "translation map."

The first two empty quotes "" tell Python not to replace any letters with other letters.

The third part tells Python: "Whenever you see anything from the punctuation list, mark it for deletion."

.translate(...): This is the actual "action" command. It takes that map we just made and applies it to your user_text, effectively vacuuming out all the symbols.

# This line removes all punctuation (like !, ?, .) from user_text by 'mapping' them to None
user_text = user_text.translate(str.maketrans("", "", string.punctuation))
# Removes all punctuation by skipping the 'swap' parts (the first two "") 
# and using the third part to delete any character found in string.punctuation.
# Example: "Hello, World!" becomes "Hello World"
user_text = user_text.translate(str.maketrans("", "", string.punctuation))"""

#Day 11 –(6 March 2026)
#  Phrase Detection (Bi-grams)
#Detect two-word emotions like very happy etc
#for that # loop through words to check two-word phrases

for i in range(len(text_word)-1): # stop one word early to safely look at next word
    phrase=text_word[i] + " " + text_word[i+1]  # combine current word and next word
    print("Checking phrase:", phrase) #his is called debugging intermediate features.
    if phrase in weights:  # check if phrase exists in emotion dictionary
       score+=weights[phrase] # add the phrase emotion value to score

# also check single words
for word in text_word:
    if word in weights:
        score += weights[word]

# print emotion score
print("Emotion Score:", score)

# decide overall mood
if score > 0:
    print("Overall Mood: Positive")
elif score < 0:
    print("Overall Mood: Negative")
else:
    print("Overall Mood: Neutral")

   # DAY 12 (8 MARCH 2026)
# Rule-Based Sentiment Analysis for multiple sentences

import string  # gives tools for working with text like punctuation

# Emotion dictionary with single and two-word phrases
weights = {
    "happy": 1,
    "very happy": 2,
    "sad": -1,
    "very sad": -2
}

# Take paragraph input from the user
sentences = input("Enter sentences: ")

# Split paragraph into sentences using "."
ttxt = sentences.split(".")

# Loop through each sentence one by one
for sentence in ttxt:

    # Remove spaces before and after sentence
    sentence = sentence.strip()

    # Skip empty sentences (sometimes split creates "")
    if sentence != "":

        # Convert sentence to lowercase
        sentence = sentence.lower()

        # Remove punctuation
        sentence = sentence.translate(str.maketrans("", "", string.punctuation))

        # Split sentence into words
        words = sentence.split()

        # Start emotion score for this sentence
        sentence_score = 0

        # Check two-word phrases like "very happy"
        for i in range(len(words) - 1):  # stop one word early

            # Combine two words to form a phrase
            phrase = words[i] + " " + words[i+1]

            print("Checking phrase:", phrase)  # debugging line

            # Check if phrase exists in emotion dictionary
            if phrase in weights:
                sentence_score += weights[phrase]

        # Check single emotion words
        for word in words:
            if word in weights:
                sentence_score += weights[word]

        # Print sentence and its emotion score
        print("Sentence:", sentence)
        print("Sentence Score:", sentence_score)
        print()  # blank line for readability

        #DAY 13 (9 ,ARCH 2026)
        # New concept of pthon re a module of python also known as Regular Expressions 
        #It helps us search, match, or split text using patterns.
        """import re 
        user_tt=input("Enter  the text: ")
        senten=re.split(r"[.!]",user_tt)
        print (senten)
        #Lets move furthur for our emotional analysis
        #lets create a dictionary first 
        emotion_words={
            "happy":2,
            "sad":-2,
           " very happy":3,
           "very sad":-3
        }
        text=input("Enter how you are feeling: ").lower()
        sntn=re.split(r"[.!]",text) #r"[.!]"
            # Split text when . or ! appears
        scoree=0
        for word in sntn:
            if word in emotion_words:
                scoree+=emotion_words[word]
            
    #now lets detect mood
    if scoree>1:
        print("Mood is positive")
    elif scoree<1:
         print("Mood is negative")
    else:
        print("neutral mood ")
print("over all mood score : ", scoree)"""

#DAY 14(11 MARCH,2026)
"""🎯 Day 14 Goals

1️⃣ Split text into words
2️⃣ Detect emotion word by word
3️⃣ Improve emotion dictionary

This moves your project closer to real sentiment analysis used in **Artificial Intelligence systems."""

#lets start 
#for that we just need little changes in the abov code
#we will lean new concept
#1️⃣ re.findall(), This extracts words from text.
# Word-based emotion detection

import re

emotion_words = {
    "happy": 2,
    "sad": -2,
    "angry": -3,
    "excited": 3,
    "love": 3,
    "hate": -3
}

text = input("How are you feeling today? ").lower()

# Split sentence into words
words = re.findall(r"\w+", text) #findall() is a function from the re module.It searches text using a pattern and returns all matches.
#syntax: re.finall(pattern,text)
#r"\w+" is a pattern
# # \w  → means a letter or number (a-z, A-Z, 0-9)
# +   → means one or more letters together
# r   → raw string so Python reads the pattern correctly
score = 0

for word in words:
    if word in emotion_words:
        score += emotion_words[word]

# Mood detection
if score > 1:
    print("Mood is positive 😊")
elif score < -1:
    print("Mood is negative 😔")
else:
    print("Mood is neutral 😐")

print("Emotion score:", score)
#Pattern Based Emotion Detection (using re.search())
# dictionary of emotion patterns and scores
import re
emotion_patterns={
    r"extremely\s+happy": 6,
    r"very\s+happy":4, #\s means space between words.
    r"happy": 2,
    r"sad": -2

}
ttx=input("How you are feeling buddy? :").lower()
score=0

# small cleaning so commas don't break patterns
ttx = re.sub(r"[.,!?]", "",ttx) # substitute (replace)Structure:
#re.sub(pattern, replacement, text) #pattern: [.,!?]replacement: " "
for pattern in emotion_patterns:
    # search pattern in text
    if re.search(pattern, ttx):
        print("Matched:", pattern)
        score+=emotion_patterns[pattern]
        # remove matched part so it can't match again
        ttx = re.sub(pattern, "", ttx)
print("Your are feeling: ",ttx )
print("Emotion score is:  ",score)
    # mood classification
if score > 0:
    print("Overall mood: Positive")
elif score < 0:
    print("Overall mood: Negative")
else:
    print("Overall mood: Neutral")


"""whats r ?
Good question.

The r before a string means "raw string".

Example:
r"\n"
Normally:
"\n"
means new line.
But with r:
r"\n"
Python treats it literally as \n."""

"""Why we use it in regex:

Regex uses many backslashes:

\s
\d
\w

If we didn’t use r, Python would try to interpret them as escape characters.

So we write:

r"\s"

instead of

"\\s"

Much cleaners"""