"""name="Bushra"
age= input("eneter your age")
print(name)
print ("age is", age)
cgpa=3.56
print ("cgpa is ",cgpa  )
answer = input("Are you a student? (yes/no): ")
is_student=answer.lower()=="yes"   ### converts input to lowercase and checks if user typed "yes" (True/False)
print(is_student)
#operators
a=3
b=5
print(a*b)
##similarly for +,-,%,/
##here isthe new conccept floor donated as "//" only gives the quotient ignoring the remainder 
print(b//a) ## gives 1 it quotient the remainder 2vi s ignored"""
"""user_age=int(input("Enter your age(in numbers)  "))
future_age=user_age + 5
if future_age%2==0:
    print(future_age," is even")
else:
    print(future_age," is odd") """
 """ 
#strings(any text inside quotes ,Can be single ' ' or double " ")
print("its AI World")
user_mressage=input("say something : ")
print(user_mressage)
girl_name="bushra"
girl_age="is 23"
#lets concatenate (combine these strings)
print(girl_name+girl_age) #output: bushrais 23
# what if i wnat space between these two 
print(girl_name+" "+girl_age)  #output: bushra is 23

#f string
print(f"{girl_name} {girl_age}")
#String Indexing

#Each character has a position starting at 0

#You can pick a single character using [index]

n = "Artificial  Intelligence"
print(n[0])  # A
print(n[3])  # i
#negative indexing display the elemts from end often string word
print(n[-1])  # e
#String Slicing(taking a part of the string instead of the whole string excluding the end word)
print(n[1:4]) #output :rti  the value on  index 4 will not be displayed
Shortcut Slicing

From start to index: word[:5] → same as word[0:5]

From index to end: word[5:] → from 5 to last letter

Full string copy: word[:]
print(n[5:])#output : "icial  Intelligence "From start to index: word[:5] → same as word[0:5]
print(n[:]) #output: Artificial  Intelligence (copies the whole string)
print(n[2:]) #output: "tificial  Intelligence" prints  from 2 to last letter 
#string functions
#len() to see the length(no of charscters in string)
print(len(n))
#String Repetition (*)
#Repeats the string multiple times
laugh="ha"
print(laugh *  5)
#if i want space i will do this
print((laugh + " ") *5 )

#.upper() – Convert to Uppercase (Changes all letters in a string to uppercase).

print(n.upper())
#..strip() – Remove Extra Spaces ,Removes spaces (or other characters) from the start and end of a string.
# Does not remove spaces in the middle.
text=" i love AI "
print(text.strip())
#.split() – Separate Words,Breaks a string into a list of words. ,Default separator = space " "(Python automatically splits the string wherever there is a space.)
print(text.split())

#If you want to split by something else, like a comma , or a dash -, you can tell it explicitly:

data = "AI,ML,Python"
print(data.split(","))  # splits at comma
#.replace() – Replace Text , string.replace(old, new)
print(n.replace("Artificial","Human")) #output:  "Human Intelligent" Replaces Artificial with Human 
#in Keyword – Search Inside String 🔍
#Checks whether something exists inside a string.
#Returns True or False (boolean).
print("Artificial" in n)
#.count() – Count Occurrences(Counts how many times a character or word appears in a string.)
print(n.count("In")) # 1
#It is case-sensitive
text = "ai AI Ai"
print(text.count("AI")) # output 1 It is case-sensitive
#f-Strings — Clean & Smart Printing (A modern way to insert variables inside text.,,
 #Makes output clean and readable.)
n_name = "Bushra"
n_age = 23

print(f"My name is {n_name} and I am {n_age} years old.")
#let understand this concept in more interesting way
user_name=input("Enter your name: ")
field=input("Enter your favourite AI field: ")
print(f"i am {user_name} and my Fvorite field of AI is {field}.")
#What Is a List?
#A list is a container that stores multiple values in one variable.
# numbers = [1, 2, 3, 4]
# print(numbers)
# text = "i love ai"
print(text.title())      # "I Love Ai" → capitalize first letter of each word
 print(text.capitalize()) # "I love ai" → only first letter of first word
 print(text.split()) #text = "i love ai"
 print(text.upper())      # "I LOVE AI" → all uppercase
 print(text.join()) #  ["I", "love", "AI"] splits each word
 textt = "I love AI and Python"
words = textt.split()        # split into words
new_text = "-".join(words)  # join words with "-" :I-love-AI-and-Python
print(new_text)
 important note:Your confusion: You were joining the whole string directly, so "-".join(text) added - between every character, not words.

What to remember: Always split the text into words first with .split() before using .join() to combine them.

Rule of thumb: .join() joins elements of a list, not raw strings.
find() – Search inside a string 🔍

What it does:

Returns the index of the first occurrence of a substring.

Returns -1 if the substring is not found.
user_typed = "I love Artificial Intelligence"
index =user_typed.find("Artificial")
print("Found at index:", index)  # Output: 7

not_found = text.find("Python")
print(not_found)  # Output: -1"""
"""
print(textt.find("AI")) #7 returns tehindxe number of where AI  is located
#another way to do it is 
final_search=textt.find("Python")
print("found at index: ", final_search)
startswith() & endswith() – Pattern detection 🏷️

What it does:

startswith(substring) → Checks if the string begins with the given substring.

endswith(substring) → Checks if the string ends with the given substring.

Returns True or False.
print(textt.startswith("I")) #True
print(textt.startswith("You")) #False
print(textt.endswith("Python")) #True
print(textt.endswith("AI")) #False
Dictionary Matters (easy)
❌ Without dictionary (your old way)

Many elif blocks:

if mood == "happy":
    print("Hurrah!")
elif mood == "sad":
    print("Oh no!")

👉 Problem: code becomes LONG and messy.

✅ With dictionary (smart AI way)
emotion_responses = {
    "happy": "Hurrah!",
    "sad": "Oh no!"
}

print(emotion_responses["happy"])
What .items() does (in one line)

👉 .items() gives you BOTH key and value together from a dictionary.
for animal, sound in animal_sounds.items():
    print(animal, ":", sound)
    A function is a reusable block of code that performs a specific task.
    def greet():
    print("Hello Bushra!")
    
    Perfect — this is the right mindset, Bushra 👍
We fix the foundation first. Short + crystal clear.

---

# ✅ Q1 — What does a function return if we don’t write `return`?

### Rule:

If no return → Python returns **`None` automatically**

### Example

```python
def greet():
    print("Hello")

x = greet()
print(x)
```

### Dry run:

1. `greet()` runs → prints **Hello**
2. No `return` written
3. Python secretly does:

```python
return None
```

✅ So `x` becomes **None**

**Developer memory tip:**

> Every function returns something — even if you don’t see it.

---

# ✅ Q2 — Why is `.get(key, 0)` safer than `dict[key]`?

### ❌ Dangerous way

```python
data = {"happy": 2}
print(data["sad"])
```

💥 ERROR → KeyError (program crashes)

Because `"sad"` does not exist.

---

### ✅ Safe way

```python
data = {"happy": 2}
print(data.get("sad", 0))
```

Output:

```
0
```

### Why?

`.get(key, default)` means:

> "If key exists → give value
> If not → give default"

---

### 🧠 Developer Brain Rule

Use:

* `dict[key]` → when you are **100% sure** key exists
* `.get()` → when key **might be missing** (AI code uses this A LOT)

---

# ✅ Q3 — Nested Loop Understanding (VERY IMPORTANT)

Code:

```python
for mood, words in moods.items():
    for word in words:
```

Suppose:

```python
moods = {
    "happy": ["happy", "joy"],
    "sad": ["sad", "cry"]
}
```

---

## 🔍 First Loop Iteration

Python takes:

```
mood  = "happy"
words = ["happy", "joy"]
```

👉 **words holds the LIST**

---

## 🔍 Second Loop Runs

```python
for word in words:
```

Now Python goes inside the list:

Iteration 1:

```
word = "happy"
```

Iteration 2:

```
word = "joy"
```

---

# 🧠 Memory Trick (SUPER IMPORTANT)

Think:

```
.items() → gives (key, value)
```

So:

* `mood` = key (string)
* `words` = value (list)

✅ **The list is always in the second variable**

---

# 🚨 Where Beginners Get Confused

They think:

❌ mood is the list
❌ words is single word

NO.

Hierarchy is:

```
dictionary
  ↓
key → list
        ↓
       word
```

---

# ✅ Quick Confidence Check (answer me)

In this code:

```python
for emotion, word_list in moods.items():
```

Which variable holds the list?

A) emotion
B) word_list

Reply with just **A or B**.
for k, v in dictionary.items():
k → key (label/name)

v → value (data/list/number/etc.)
Good — this is the **exact place developers grow**. Let’s fix it simply. 🚀

## 🧠 Big Picture (1 line)

**Nested loop = loop inside loop to check many things inside many groups**

---

## 🎯 Your AI Mood Case — Visual Thinking

Your data:

```python
moods = {
    "happy": ["happy", "joy", "excited"],
    "sad": ["sad", "cry", "upset"]
}
```

Think like this:

👉 You have **groups (moods)**
👉 Inside each group you have **words**

So you must check:

> For each mood → check each word → see if it exists in sentence

That’s why we need **two loops**.

---

## 🔁 Step-by-Step Mental Movie

Code:

```python
for mood, words in moods.items():      # OUTER LOOP
    for word in words:                 # INNER LOOP
        if word in sentence:
            return mood
```

---

## 🎬 Dry Run (VERY EASY)

Suppose:

```python
sentence = "i am very happy today"
```

### Step 1 — Outer loop starts

First round:

```
mood = "happy"
words = ["happy", "joy", "excited"]
```

---

### Step 2 — Inner loop runs

Now Python checks **each word inside happy list**

#### Round 1 inner:

```
word = "happy"
```

Check:

```
"happy" in sentence → ✅ YES
```

So function returns:

```
"happy"
```

✅ Done.

---

## 🧠 Why Nested Loop is Needed (IMPORTANT)

Ask yourself:

❌ Can one loop check ALL words in ALL moods?
👉 **No**

Because structure is:

```
moods
 ├── happy → many words
 ├── sad → many words
 └── angry → many words
```

So logic must be:

```
for each mood:
    for each word inside that mood:
        check it
```

🔥 **Rule to remember forever:**

> If data is list inside dictionary → you almost always need nested loop.

---

## 🧩 Super Simple Analogy

Think:

* moods = folders
* words = files inside folders

To find a file:

```
open each folder
    check each file inside
```

That is nested loop.

---

## 🎯 Your Quick Answer (don’t overthink)

Inside this line:

```python
for word in words:
```

**What is `words`?**

A) single word
B) list of words

Just answer A or B.
💯 **Correct — B.**

Because:

👉 The dictionary values are **lists**
👉 So we must loop twice:

1️⃣ First loop → go through each mood
2️⃣ Second loop → go through each word inside that mood

---

### 🧠 Developer Brain Summary

Structure in memory:

```python
moods = {
    "happy": ["happy", "joy", "excited"]
}
```

So you have:

* Level 1 → dictionary
* Level 2 → list inside each key

✅ **Rule:** Nested structure → nested loops

---

# 🔥 Your Brain Upgrade (remember this forever)

If data looks like:

* dict of strings → 1 loop
* list of strings → 1 loop
* dict of lists → ✅ **2 loops**
* list of dicts → ✅ **2 loops**

---

You are actually doing very well — this confusion is exactly where real developers grow.

---

## ⚡ Final Quick Check (very sharp)

Inside this loop:

```python
for mood, words in moods.items():
```

What is `words`?

A) A single word
B) A list of words

Answer fast.
GOOD. 🔥
Today we stop being “confused learner” and become **structured developer**.

Day 7 starts NOW.

---

# 🔹 PART 1 — Quick Review (Developer Mode, Not Student Mode)

Answer in your head while reading.

---

## 1️⃣ Functions — What You Must Remember Forever

### Structure:

```python
def function_name(parameters):
    # logic
    return value
```

### 🧠 Important Truths

* `def` → creates function
* parameters → receive input
* `return` → sends value back
* without `return` → function returns `None`
* function stops immediately after `return`

---

### 🔎 Mental Model

When you call:

```python
result = catch_emotion("I am happy")
```

Python:

1. Jumps into function
2. Runs code
3. Hits `return`
4. Comes back with value

---

## 2️⃣ Dictionaries — What Developer Brain Must Know

Example:

```python
moods = {
    "happy": ["joy", "smile"],
    "sad": ["cry", "upset"]
}
```

### Important operations:

| Method           | What it does      |
| ---------------- | ----------------- |
| `.items()`       | gives key + value |
| `.get(key)`      | safely gets value |
| `dict[key]`      | direct access     |
| `dict[key] += 1` | update            |
| `key in dict`    | check existence   |

---

## 3️⃣ Nested Loop Mental Formula

If structure is:

```python
dict → list → string
```

You need:

```python
loop → loop → check
```

Nested loops are just:

> “Loop inside something that itself contains multiple things.”

That’s it. No magic.

---

# 🔥 PART 2 — Advanced Function Usage

Now we level up.

---

## ✅ 1. Passing Dictionary As Parameter

Instead of defining dictionary inside function:

```python
def detect(text, moods):
```

Now the function becomes reusable.

This is how real AI systems work.

---

## ✅ 2. Returning Multiple Values (VERY IMPORTANT)

Example:

```python
def calculate():
    return 5, 10
```

Python automatically returns a **tuple**.

You can unpack:

```python
a, b = calculate()
```

Now:

* `a = 5`
* `b = 10`

---

### 🧠 Why This Matters for AI?

You might return:

* detected mood
* mood score
* confidence level

All from one function.

---

# 🚀 PART 3 — Mini AI Project (Real One Now)

We will build:

## Mood Counter with Scores

---

### Step 1 — Structure

```python
def analyze_text(text, moods_dict):
    
    text = text.lower()
    results = {}  # empty dictionary to store counts
    
    # outer loop → mood
    for mood, words in moods_dict.items():
        
        count = 0  # reset counter for each mood
        
        # inner loop → words
        for word in words:
            
            if word in text:
                count += 1
        
        results[mood] = count  # store count in dictionary
    
    return results
```

---

### Example Usage

```python
moods = {
    "happy": ["happy", "joy", "excited"],
    "sad": ["sad", "cry", "upset"]
}

sentence = "I am happy and excited but also a little sad"

report = analyze_text(sentence, moods)

print(report)
```

---

### Output:

```python
{
    "happy": 2,
    "sad": 1
}
```

---

# 🧠 What Just Happened (IMPORTANT)

You just built:

✔ Text preprocessing
✔ Feature extraction
✔ Structured scoring
✔ Dictionary-based NLP logic

This is literally how beginner NLP systems work before ML models.

You are touching AI now. Not joking.

---

# 🔥 PART 4 — Brain Upgrade Question

Inside this line:

```python
results[mood] = count
```

What is happening?

A) New dictionary created
B) Updating dictionary with key and value
C) Loop restarting

Answer carefully. This checks real understanding.
GOOD. 🔥
Today we stop being “confused learner” and become **structured developer**.

Day 7 starts NOW.

---

# 🔹 PART 1 — Quick Review (Developer Mode, Not Student Mode)

Answer in your head while reading.

---

## 1️⃣ Functions — What You Must Remember Forever

### Structure:

```python
def function_name(parameters):
    # logic
    return value
```

### 🧠 Important Truths

* `def` → creates function
* parameters → receive input
* `return` → sends value back
* without `return` → function returns `None`
* function stops immediately after `return`

---

### 🔎 Mental Model

When you call:

```python
result = catch_emotion("I am happy")
```

Python:

1. Jumps into function
2. Runs code
3. Hits `return`
4. Comes back with value

---

## 2️⃣ Dictionaries — What Developer Brain Must Know

Example:

```python
moods = {
    "happy": ["joy", "smile"],
    "sad": ["cry", "upset"]
}
```

### Important operations:

| Method           | What it does      |
| ---------------- | ----------------- |
| `.items()`       | gives key + value |
| `.get(key)`      | safely gets value |
| `dict[key]`      | direct access     |
| `dict[key] += 1` | update            |
| `key in dict`    | check existence   |

---

## 3️⃣ Nested Loop Mental Formula

If structure is:

```python
dict → list → string
```

You need:

```python
loop → loop → check
```

Nested loops are just:

> “Loop inside something that itself contains multiple things.”

That’s it. No magic.

---

# 🔥 PART 2 — Advanced Function Usage

Now we level up.

---

## ✅ 1. Passing Dictionary As Parameter

Instead of defining dictionary inside function:

```python
def detect(text, moods):
```

Now the function becomes reusable.

This is how real AI systems work.

---

## ✅ 2. Returning Multiple Values (VERY IMPORTANT)

Example:

```python
def calculate():
    return 5, 10
```

Python automatically returns a **tuple**.

You can unpack:

```python
a, b = calculate()
```

Now:

* `a = 5`
* `b = 10`

---

### 🧠 Why This Matters for AI?

You might return:

* detected mood
* mood score
* confidence level

All from one function.

---

# 🚀 PART 3 — Mini AI Project (Real One Now)

We will build:

## Mood Counter with Scores

---

### Step 1 — Structure

```python
def analyze_text(text, moods_dict):
    
    text = text.lower()
    results = {}  # empty dictionary to store counts
    
    # outer loop → mood
    for mood, words in moods_dict.items():
        
        count = 0  # reset counter for each mood
        
        # inner loop → words
        for word in words:
            
            if word in text:
                count += 1
        
        results[mood] = count  # store count in dictionary
    
    return results
```

---

### Example Usage

```python
moods = {
    "happy": ["happy", "joy", "excited"],
    "sad": ["sad", "cry", "upset"]
}

sentence = "I am happy and excited but also a little sad"

report = analyze_text(sentence, moods)

print(report)
```

---

### Output:

```python
{
    "happy": 2,
    "sad": 1
}
```

---

# 🧠 What Just Happened (IMPORTANT)

You just built:

✔ Text preprocessing
✔ Feature extraction
✔ Structured scoring
✔ Dictionary-based NLP logic

This is literally how beginner NLP systems work before ML models.

You are touching AI now. Not joking.

---

# 🔥 PART 4 — Brain Upgrade Question

Inside this line:

```python
results[mood] = count
```

What is happening?

A) New dictionary created
B) Updating dictionary with key and value
C) Loop restarting

Answer carefully. This checks real understanding.

YESSSS 👏🔥
See? You didn’t lose concentration — you just needed clarity.

Now we move to the **LAST core concept of Day 7** in a clean way.

No mixing. No overload.

---

# ✅ Final Concept of Day 7

# 🔹 Returning Multiple Values from a Function

This is VERY important in AI systems.

---

## 🌱 Step 1 — Basic Example

```python
def add_and_multiply(a, b):
    sum_result = a + b
    multiply_result = a * b
    return sum_result, multiply_result
```

Now call it:

```python
x, y = add_and_multiply(3, 4)

print(x)  # 7
print(y)  # 12
```

---

## 🧠 What Just Happened?

When we wrote:

```python
return sum_result, multiply_result
```

Python automatically packed them into a **tuple**:

```python
(7, 12)
```

Then this line:

```python
x, y = add_and_multiply(3, 4)
```

Unpacked them.

---

# 🔥 Why This Matters in AI

In AI/NLP systems you often return:

* prediction
* confidence score
* feature counts
* probability

Example structure:

```python
return mood, score
```

This is VERY common in ML pipelines.

---

# 🌱 Small AI-Style Example

```python
def detect_mood(text):
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
    else:
        return "sad", sad_count
```

Call it:

```python
mood, score = detect_mood("I am happy and full of joy")

print(mood)   # happy
print(score)  # 2
```

---

# 🧠 Concept You Just Learned

✔ Tuple return
✔ Unpacking
✔ Multiple outputs from function
✔ Basic scoring logic

This is REAL beginner AI pipeline logic.

---

# 🎯 Day 7 Concepts Covered

Here is what we used in AI context:

### ✅ Core Python

* Functions
* Parameters
* Return
* Default return (None)
* Returning multiple values
* Tuple unpacking

### ✅ Data Structures

* Dictionaries
* Lists
* Dictionary methods (`.items()`)
* Updating dictionary values

### ✅ Logic

* Loops
* Nested loops
* Conditionals
* Counting logic
* Feature extraction idea

---

# 🧠 What AI Concepts Are Still Left (Important)

Before moving to advanced AI, you still need:

1. 🔹 String methods (split, replace, strip)
2. 🔹 List comprehensions
3. 🔹 Sets (for unique words)
4. 🔹 Basic file handling (reading text files)
5. 🔹 Exception handling
6. 🔹 Basic OOP (classes — very important later)
7. 🔹 Modules & imports
8. 🔹 Basic NumPy (foundation for ML)
9. 🔹 Understanding how ML models consume features

We will cover these step-by-step.

---

# 🔥 Now As Promised — 2 Option Questions Mode

Let’s test everything calmly.

---

## Question 1

If a function has no `return` statement, what does it return?

A) 0
B) None

Answer only A or B.

"""