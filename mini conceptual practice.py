

#Task 1: Tokenization (20 mins)
import nltk
from nltk.tokenize import word_tokenize
text="I am sad@2@@" #@2@@ will be removed due to isalpha
words=word_tokenize(text)
words= [w for w in words if w.isalpha()]
print(words)
#Phrase Detection
phrase_dict={
   " very happy": 4,
   "very sad":-4
}
detected=[]
for phrase in phrase_dict:
    if phrase in text:
        detected.append(phrase) #add detected word to phrase
print(detected)
#used_words Logic
used_words = set()   # plural + correct type,# correct: empty set created
used_words.add("happy")# # correct: adding a word

print(used_words)

"""Perfect — we’ll learn this with tiny examples only. No theory overload. 💀👇

🔹 1. for w in words (basic loop)
words = ["happy", "sad", "angry"]

for w in words:
    print(w)

👉 Output:

happy
sad
angry

👉 Meaning:
Go through each word one by one

🔹 2. w for w (same thing but shorter)
words = ["happy", "sad", "angry"]

new_list = [w for w in words]

print(new_list)

👉 Output:

['happy', 'sad', 'angry']

👉 Meaning:
Take each word and store it

🔹 3. w.isalpha() (check letters only)
print("happy".isalpha())   # True
print("sad!".isalpha())    # False
note: isalpha() is a string method that checks if all characters are letters. It doesn’t remove anything by itself,
 but when we use it inside a list comprehension like [w for w in words if w.isalpha()], it filters out punctuation/numbers.

👉 Meaning:
Only accept clean words (no !, ., numbers)

🔹 4. Combine them (REAL use)
words = ["happy", "sad!", "123", "angry"]

clean_words = [w for w in words if w.isalpha()]

print(clean_words)

👉 Output:

['happy', 'angry']

👉 Meaning:
Go word by word → keep only clean words

🔹 5. phrase.split() (break sentence)
phrase = "very happy"

print(phrase.split())

👉 Output:

['very', 'happy']

👉 Meaning:
Break sentence into words

🔹 6. Combine with loop (your project logic)
phrase = "very happy"

for w in phrase.split():
    print(w)

👉 Output:

very
happy

👉 Meaning:
Break phrase → check each word

🧠 Final Simple Memory

for w in words → go one by one

w for w → take each item

w.isalpha() → keep only clean words

split() → break sentence into words

💀 Mini Practice (DO THIS)

Try:

words = ["I", "am", "happy!", "today"]

clean = [w for w in words if w.isalpha()]

print(clean)

👉 Predict output before running

If you want next, I’ll give you a tiny test like your exam to check if you really understood 💀


Similar string methods you might use in NLP / your project
Method	What it does	Example
isalpha()	Checks if all letters	"happy".isalpha() → True, "sad!".isalpha() → False
isdigit()	Checks if all numbers	"123".isdigit() → True, "abc".isdigit() → False
islower()	Checks if all letters are lowercase	"hello".islower() → True, "Hello".islower() → False
isupper()	Checks if all letters are uppercase	"HELLO".isupper() → True
strip()	Removes whitespace or specific chars from start/end	" hello ".strip() → "hello"
lower()	Converts to lowercase	"Happy".lower() → "happy"
replace()	Replaces substring with another	"I am happy!".replace('!', '') → "I am happy"
split()	Splits string into a list	"very happy".split() → ['very', 'happy']
💀 Quick memory trick for your project:

isalpha() → remove punctuation/numbers

lower() → unify all text

split() → break sentences/phrases into words

strip() / replace() → clean extra spaces or symbols

These are the main ones you will use in your emotion detection program."""