
#You will build a mini AI text analyzer 😎
#lets do something fun with string concepts 
#DAY 2 (24 feb ,2026)
comment = input("Give a reason Why you love AI:")
print("Total charaters are :", len(comment))    

print("machine " in comment)

print(comment.strip()) #removes space from start and end
print(comment.lower()) #converts  to lowercase
print(comment.replace("AI","Artificial Intelligence")) #Replaces AI with Artificial Intelligence
print(comment.lower().count("ai"), "times") #count how many times AI is repeated used comment.lower() to make it cae insensitive
print(f"I love AI cause {comment} ") #fstring
#AI emotion List
emotions=["happy","sad","angry","scared","excited"]
print(emotions)#prints a list of emotions
#if we want to access one emotion index wise we will use indexing
print(emotions[-1]) #Output: "excited" prints the emotion eritten on end
#lets do some twist let ai detect and print emotion
#create first nlp model

#########-----Rule-based NLP emotion detector-----#########
user_mood=input("How you are feeling today: ").lower().strip()
if "happy" in user_mood:
    print("hurrah! you are feeling happy")

elif "sad" in user_mood:
    print("ohhh! you are feeling Sad")

elif "angry" in user_mood:
    print("uffo! you are feeling angry")

elif "scared" in user_mood:
    print("Oh NO! you are feeling scared")

elif "excited" in user_mood:
   print('Yayyy!!! You are excited')

else:
    print("No feeling !!")
    #lets make it more intersting
    #system_name = "rule_based_emotion_detector_v1"
    #lets create it

systemname ="rule_based_emotion_detector_v1"
detected_emotion="neutral" # AI emotion placeholder variable
for emotion in emotions:
    if emotion==user_mood:
        detected_emotion=emotion
        break

print("System Used: ", systemname)
print("Emotion is: ", detected_emotion)

#DAY3(25 feb ,2026)
text = "i love ai"
print(text.title())      # "I Love Ai" → capitalize first letter of each word
print(text.capitalize()) # "I love ai" → only first letter of first word
print(text.split()) #text = "i love ai"
print(text.upper())      # "I LOVE AI" → all uppercase
textt = "I love AI and Python"
words = textt.split()        # split into words
new_text = "-".join(words)  # join words with "-" :I-love-AI-and-Python
print(new_text)
"""important note:Your confusion: You were joining the whole string directly, so "-".join(text) added - between every character, not words.

What to remember: Always split the text into words first with .split() before using .join() to combine them.

Rule of thumb: .join() joins elements of a list, not raw strings."""

"""find() – Search inside a string 🔍
What it does:
Returns the index of the first occurrence of a substring.
Returns -1 if the substring is not found."""
print(textt.find("AI")) #7 returns tehindxe number of where AI  is located
#another way to do it is 
final_search=textt.find("Python")
print("found at index: ", final_search)
#Mini AI Example
user_input="I am  feeling excited today"
if user_input.find("excited") != -1: # if excited exist in what user typed
    print("Detected Emotion is: ",user_input)
    #This is how AI can detect keywords in text without scanning manually.
    """startswith() & endswith() – Pattern detection 🏷️

What it does:

startswith(substring) → Checks if the string begins with the given substring.

endswith(substring) → Checks if the string ends with the given substring.

Returns True or False."""
print(textt.startswith("I")) #True
print(textt.startswith("You")) #False
print(textt.endswith("Python")) #True
print(textt.endswith("AI")) #False
#Mini AI usage of it 
user_command="run the data"
if user_command.startswith("run"):
   print("command is Excecuting.....")
#what if user says dont run in that case we willd o thsi
command = input("Enter command: ").lower().strip()

if "dont run" in command:
    print("Okay, I will not run.")

elif command.startswith("run"):
    print("Running the system...")

else:
    print("Command not recognized.")
##Dictionary Matters (easy)
##❌ Without dictionary (your old way)

##Many elif blocks:
"""
if mood == "happy":
    print("Hurrah!")
elif mood == "sad":
    print("Oh no!")"""

 #Problem: code becomes LONG and messy.

#✅ With dictionary (smart AI way)
emotion_responses = {
    "happy": "Hurrah!",
    "sad": "Oh no!"
}

print(emotion_responses["happy"])
#AI Example task
Animals_sounds={
"cat":"Meaow!!",
"dog":"wowwow!!",
"armadillo":"grunt",
"ape":"moo",
"ant":"cry",
"alligator"	:"hiss"


}
user_tell=input("Tell me animal Name: ").lower()
if user_tell in Animals_sounds:
    print(Animals_sounds[user_tell])
else:
    print("Animal not found")
    #lets loop through dictionary
    for animal in Animals_sounds:
     print(animal)
#.items():"a built-in dictionary method" gives you BOTH key and value together from a dictionary.
for animal, sound in Animals_sounds.items():
    print(animal, ":", sound)






 #DAY 4 (26b Feb 2026)
 #MINI AI Emotion Word counter



#Scan a sentence and count emotion words using a dictionary
      

"""
sentence=input("Enter the sentence : ").lower()
emotion_words={
          "happy": 0,
          "sad": 0,
          "angry": 0,
          "fear": 0
      }
words=sentence.split()
for word in words:
         if  word in emotion_words:
            emotion_words[word] += 1
            print("Emotion count:", emotion_words)"""

          
          

