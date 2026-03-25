# Project: Day 12- Negation Handling in Emotion Detection
# New Concept: Negation words reverse the sentiment score

import re
emotion_patterns = {
    r"extremely\s+happy": 6,
    r"very\s+happy": 4,
    r"happy": 2,
    r"sad": -2
}
negation_words=["not","never","no"]
text = input("How are you feeling today? ").lower() #text Normalisation
#remove puntuation
text=re.sub(r"[.,!?]","",text) #re.sub(pattern, replacement, text)
words=text.split() #split the sentence into words(Tokenazation)
score=0
for i in range (len(words)): #we want to check:current word previous word,, This helps detect negation cause this will go through each word
    
     if words[i] in ["happy","sad"] :                 #Check if the current word is an emotion word.
           value=emotion_patterns[words[i]] 
     if i>0 and words[i-1] in negation_words:
           value=-value
           score+=value
print("overall score is: ",score)
if score > 0:
    print("Overall Mood: Positive")
elif score < 0:
    print("Overall Mood: Negative")
else:
    print("Overall Mood: Neutral")


