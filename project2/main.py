# To create a conversational AI assistant using Python’s core logic - string matching, functions, dictionaries, and loops. 

import datetime
import time


name = input("Welcome, Enter your name :-")
presentHour = datetime.datetime.now().hour

if 5<= presentHour <= 11:
    print("Good Morning,",name)

elif 11 <= presentHour <= 17:
    print("Good Afternoon.",name)

elif 17 <= presentHour <= 20 :
    print("Good Evening.",name)
else:
    print("Good Night.",name)


print("Welcome to your ChatBot")
print("How can i help you?",name ,"\nType 'bye' to exit from the bot.")

# chatbot memory creation 

response = {
    "hello" : "Hi, welcome: What is your question?",
    "how are you": "I am Very fine. ThankYou",
    "who are you" :"I am smart AI chatbot.",
    "what is a function": "refer chapter7",
    "what is a loop": "refer chapter6",
    "that's really helpfull": "Happy to hear that.",
    "bye":"Nice Taking with you",
    
}


# method/function to get response of chatbot

def getresponse(userquestion):
    userquestion = userquestion.lower()
    for eachkey in response:
        if eachkey in userquestion:
            time.sleep(0.5)
            return response[eachkey]
        
    return "I am not able to get the answer for your question right now! I will learn that soon!"

# take Userinput

while True:

   userInput = input("please ask your question:")
   reply = getresponse(userInput)
   print("Bot response :-",reply)

   if "bye" in userInput.lower():
       time.sleep(1)
       print("Bot response :- Bye!",name)
       break