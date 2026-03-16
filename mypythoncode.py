x=5
name="bushra"
age=20
print(name)
#print(type(x))
"""this is a multiline comment
c = 2 + 3j    # complex
print(c)
print(type(c))
print(name[0])
print (name[0:3])#string slicing(print characteroon index 0,1,2 bute exclude 3)
print(name[-1])#start frombackword "will display a of bushra"
#concatenation of string
new_name="b" + name
print(new_name)
#type conversion
num_str=input("enter a number: ")
num = float(num_str)
print(num * 2)  
name = input("Enter name: ")
age = int(input("Enter age: "))
#fstring
print(f"Hello {name}, you are {age} years old")"""
#arthematic operaters
print(10 + 5)   # 15
print(10 / 3)   # 3.3333
print(10 // 3)  # 3 (floor operater its like 10/3=3.333 ,the floor is 3(3.333 is rounded to 3)
print(2 ** 3)   # 8
#Logical Operators (and, or, not)
x = 10
print(x > 5 and x < 20)  # True
print(x < 5 or x > 0)    # True
print(not(x > 5))        # False
#ifelse
marks = 75
if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("Fail")
"""Loops: for, while
🔹 What it is

for → iterate over a sequence

while → iterate while a condition is True"""
"""Range function (range())
🔹 What it is

Generate sequence of numbers

Often used in for loops"""
for i in range(5):
    if i == 3:
        break  # stops loop
    print(i)

for i in range(5):
    if i == 3:
        continue  # skip 3
    print(i)
for i in range(1, 11):   # numbers 1 to 10
    if i > 7:
        break            # stop the loop if number > 7
    if i % 3 == 0:
        continue         # skip multiples of 3
    print(i)
#range(start, stop, step)
"""start → first number in the sequence (inclusive)

stop → stop number (exclusive) → it does not include this number

step → how much to increase each time"""
for i in range(2, 10, 2):
 print(i)#output 2,4,6,8 here in range(2, 10, 2) 2 is like start from 2,10 is like stop when  10 omes and skip it ,2 is like inrease the numberby 2 eachtime 
"""-strings & string formatting
🔹 What it is

Modern way to insert variables into strings

🔹 Facts

Python 3.6+ feature

Easier and readable than "{}{}".format()"""
name = "Bushra"
age = 20
print(f"My name is {name} and I am {age} years old")

print(f"Next year I will be {age + 1}")
#lists
nums=[1,"bushra",True,"python"]
nums[0]="no 1"#adds no 1 at 0 index in place of 1
print(nums)
nums.append(5)#add five after python
print(nums)
#Create a list with duplicates Convert it to a set Print the result
numbers=[1,2,3,4,5,6,7,7,7]
print(numbers) #numbers before removing duplication
unique_list=set(numbers)#Convert the list to a set (removes duplicates)
print(unique_list)
#A dictionary stores data in key : value form.
girl={
    "name": "bushra", #Dictionary keys must be written as strings if you want labels like "name" and "age".
    "age":24   #Keys must be unique ,Keys must be immutable ,Very fast lookup (hash table)
}
print(girl)
#lets add a new key to girl
girl["qualifiaction"]="Bachelors Graduate" 
print(girl)
#NESTED DATA STRUCTURESs
#Create a list of 2 dictionaries,Each dictionary has name & marks,Print first student’s marks
listt=[
    {
        "name":"Bushra",
        "marks":"499"

    }
    ,
    {
     
        "name":"Taiba",
        "marks":"599"
    }
]
print(listt[1]["marks"])
#List Comprehension
#[expression for item in iterable if condition]
#Create a list of even numbers from 1 to 20 using comprehension
even_numbers=[x for x in  range(1,21) if x%2==0]
print(even_numbers) #Remember:range() does NOT include the stop valueTo include 20 → we must write 21
"""| What you want                   | Use                        |
| ------------------------------- | -------------------------- |
| First N numbers starting from 0 | `range(N)`                 |
| Numbers from A to B             | `range(A, B+1)`            |
| Skip numbers (step)             | `range(start, stop, step)` |
"""
#range(2, 11, 2)
"""Three numbers → start, stop, step

start = 2 → start counting from 2

stop = 11 → stop before 11

step = 2 → increase by 2 each time"""
#DICTIONARY COMPREHENSION
#{key_expression: value_expression for item in iterable}
dict_comp={x: x for x in range(5)}
print(dict_comp)
even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_dict)  # {0:0, 2:4, 4:16, 6:36, 8:64}
#tuples(immutable unlike lists)
coords = (10, 20, "ii")
print(coords[0])   # 10
print(coords[-1])  # 30
#Example 2 — Tuples as dictionary keys
location_data = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}
t = (1, 2, 3)
#t[0] = 10  # ❌ TypeError
print(location_data[(10, 20)])  # Point A
cities=("DINGA","KHARIAN","LAHORE")
print(cities[0],cities[-1])
"""In Python, the core built-in data structures are:

List → ordered, mutable

Tuple → ordered, immutable

Set → unordered, unique values--Order is not guaranteed

my_set = {3, 1, 2}
print(my_set)  # Could print {1, 2, 3} or {2, 3, 1}

Dictionary (dict) → key–value pairs--You cannot access by index, only by key

my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict["a"])  # 1 → access by key
# print(my_dict[0])  # ❌ ERROR → cannot access by position


Iterating over keys may look ordered, but it’s not the main idea

for key in my_dict:
    print(key)

🔹 Quick Comparison Table
Type	Ordered	Mutable	Indexing	Allows Duplicates
List	Yes	Yes	Yes	Yes
Tuple	Yes	No	Yes	Yes
Set	No	Yes	No	No
Dict	No*	Yes	No	Keys: No, Values: Yes

*Dict in Python 3.7+ preserves insertion order but conceptually unordered, key-based.



Comprehensions: This is syntax/tool to create data structures easily. It doesn’t store data itself; it generates lists, dicts, or sets"""
#Functions 🔹 What it is(A function is a block of code that performs a specific task and can be reused.)

def greet_morning():
    print("good morning!")
greet_morning()  # good morning!

#Developer memory 🧠

#Always name functions descriptively (calculate_area, get_user_input)

#Keep functions small & focused → 1 task per function
    #Functions can take inputs (parameters) and return results.

def greet_person(name):
    print(f"Hello, {name}!")
    
greet_person("Bushra")  # Hello, Bushra!
"""
note:
def greet():
    print("good morning!")

# greet now points to this function

def greet(name):
    print(f"Hello, {name}!")

# greet now points to this new function
# The old function is gone
"""
#Functions can send a value back using return.
def square(x):
    return x * x

print(square(5))  # 25
"""kwargs means:

Keyword Arguments (arguments passed with a name)

It lets a function accept any number of named arguments.
def show_info(**kwargs):
    print(kwargs)

show_info(name="Bushra", age=20, city="Lahore")
"""
"""**kwargs is used when you want to pass dictionary-like data as function parameters,
but you do NOT pass a dictionary directly.
Instead, you pass key=value pairs, and Python converts them into a dictionary inside the function.
Correct way to think (Developer mindset 🧠)

**kwargs allows a function to accept any number of named arguments, which become a dictionary inside the function.

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(a=1, b=2)
"""
#Lambda Functions🔹 What it is --Anonymous function (no name), usually short and one-line

square = lambda x: x * x
print(square(5))  # 25
"""Common with map(), filter(), sorted()
Can take multiple arguments but one expression only
simple version
def square(x):
    return x * x
Lambda version 👇
lambda x: x * x

def func(x, y):
return x+y
   Same as:
     lambda x, y: x + y
     Be used inside map, filter, sorted


     First: What are these 3 things?
1️⃣ map

👉 Changes every item in a list
👉 “Take each value → modify it”

Think: Apply something to all items
filter

👉 Keeps some items, removes others
👉 Based on a condition (True / False)

Think: Select only what you want
sorted

👉 Arranges items in order
👉 Can sort using custom logic

Think: Arrange data properly
"""
#Example list (we’ll use one list everywhere)
num = [1, 2, 3, 4, 5]
result=list (map(lambda x:x * 2, num))
print(result)
"""
def double(x):
    return x * 2

    result = list(map(double, nums))
print(result)
 Ah! Got it 😅 You want it **really simple**, like “explain it in one line in normal words” for a beginner. Let’s do that.

---

### What `map()` is:

> **“Map takes a list and does something to every item in it, and gives a new list.”**

---

### Example — super simple:

```python
numbers = [1, 2, 3, 4]

# Multiply each number by 2
new_numbers = map(lambda x: x*2, numbers)

print(list(new_numbers))  # [2, 4, 6, 8]
```

* Think of it as: **“take each number, multiply by 2, give me the new list”**
* You **don’t need to write a loop**, map does it automatically.

---

### Another simple one — words:

```python
words = ["hi", "hello", "hey"]
new_words = map(str.upper, words)
print(list(new_words))  # ['HI', 'HELLO', 'HEY']
```

* **Take each word → make it uppercase → new list**

---

💡 **Remember:**

`map()` = **apply something to every item in a list, automatically**

map(lambda x: <do something>, my_list)

"""
numb=[1,2,3,5,88]
#def square(x):
    #return x*x

#result=list(map(square,numb))
#we can also write this 
result=list(map(lambda x: x * 2 ,numb))
print(result)
# for filter
numbers = [1, 2, 3, 4, 5, 6,10,12,444]

evens = filter(lambda x: x > 15 ,numbers) #filter out odd numbers like 3,5
print(list(evens)) #display even numbers list [2, 4, 6, 10, 12, 444]
# now sorted
numbers = [4, 1, 3, 2]

result = sorted(numbers)
print(result)
fruits=["banana", "apple", "cherry"]
res=sorted(fruits,reverse=True)
print(res)
li_num=[1,2,3,4,5,6]
#keep only odd numbers
odds=filter(lambda x:x % 2 !=0 ,li_num)
#cube odd numbers
cubed=map(lambda x: x ** 3 ,odds)
#sort  odd numbers 
res=sorted(cubed)
print(res)
"""
#COMBINED EXAMPLE (Real-world style)#Nested code — how Python evaluates 🤖(python first evaluates teh innermost function tats why its written in reverse)
digits=[22,33,44,55,66,666777]
#filter even numbers
ress=sorted(
     map(lambda x:x ** 2,
         filter(lambda x: x %2==0,digits
                   
                        )))"""
#the above code is not a good practice for beginner so wecan write thsi in simple manner(what human evaluates in sequqntial order)
digits=[22,33,44,55,66,666777]
even_numbers=filter(lambda x: x %2==0,digits)
even_sq=map(lambda x:x ** 2,even_numbers)
print(sorted(even_sq))
#lets write the ocmprehension of this list
result=[x*x for x in digits] #we are creating a new list name result(contains squares) out of list didgts 9contains numbesr whose squared list is to be craeted
print(result)
"""
Classes & Objects
💡 What it is

Class = blueprint / template

Object = real thing created from blueprint
| Blueprint (Class) | Real Object (Instance) |
| ----------------- | ---------------------- |
| Car blueprint     | My Toyota Corolla      |
| Dog blueprint     | Your dog “Rex”         |
"""
class dog:
    def bark(self):
        print("woof!")



my_dog = dog()
my_dog.bark()
#inheritance

class animal:
    def makesound(self): 
      print("Aniamls make sound")


class cat(animal): #cat inherits animal
       def meow(self):
          print("meow!")



my_cat = cat()
my_cat.meow()
class person:
    def __init__(self,name):
       self.name=name
       print(name)
       
       
       
person_name=person("bushra") #Object creation
person_name.name="Taiba" #Modify existing object
person_name=person("Taiba") #Object creation that store sname taib now

class Student:
    def __init__(self, name, marks):   # Constructor sets data
        self.name = name
        self.marks = marks

    def show(self):                     # Method just prints stored data
        print(f"Name: {self.name}, Marks: {self.marks}")

# Create object
new_student = Student("Bushra", 80)

# Show data
new_student.show()   # Name: Bushra, Marks: 80

# Modify marks
new_student.marks = 90
new_student.show()   # Name: Bushra, Marks: 90
class AIModel:
    def __init__(self,name):
        self.name=name  # this model's name
    def describe(self):
     print(f"This is an AI model named {self.name}")



model1 = AIModel("Base AI")
model1.describe()
class AIModel:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"This is an AI model named {self.name}")


class ImageModel(AIModel):
    def __init__(self, name, accuracy):
        super().__init__(name)      # call parent constructor
        self.accuracy = accuracy

    def predict(self):
        print(f"Image model {self.name} is predicting with {self.accuracy}% accuracy")


model1 = AIModel("Base AI")
model1.describe()

model2 = ImageModel("ImageNet", 92)
model2.describe()   # inherited
model2.predict()    # child method
class car:
    def set_speed(self,speed):
     self.speed=speed  # store speed in this car object
    def show_speed(self):
      print(f"Car speed: {self.speed}")


car1 = car()
car2 = car()

car1.set_speed(60)
car2.set_speed(100)

car1.show_speed()   # Car speed: 60
car2.show_speed()   # Car speed: 100

