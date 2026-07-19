# ============================================================== #

import pyttsx4 #this is an offline library for text to speech...

#installation of pyttsx4 library
engine = pyttsx4.init()

# these two lines are for change the voice from male to female...
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[1].id) # [0] for male and [1] for female ....

#this is the brain of jarvis... 
brain = { 
    "hello": "Hi boss, how can I help you today?",
    "good morning": "Good morning boss!",
    "good afternoon": "Good afternoon boss!",
    "who are you": "I am a customizable AI chatbot with voice template.",
    "what is your name": "my name is Jarvis..",
    "offline": "Okay sir, shutting down Jarvis systems. See you soon!",
    "who made you": "I am made by Sarthak.."
}

print("Jarvis is online boss....ready to go ..")
engine.say("Jarvis is online boss....ready to go ..")
engine.runAndWait()

#Core logic --------------------------
while True:
    # Taking inputs from user (without any stuff of capital letters and space)
    user_input = input("\n You : ").lower().strip()   

    if not user_input:  #when the user press 'Enter' without typing anything... 
        continue

    # command for shutting down the sysytem..
    if user_input == "offline":
        print(f"\n Jarvis : {brain['offline']}")
        engine.say(brain['offline'])
        engine.runAndWait()
        break   
    
    #finding answers in dictionary 
    if user_input in brain:
        print(f"\n Jarvis :  {brain[user_input]}")
        engine.say(brain[user_input])
        engine.runAndWait() 
    
    # if the answer did not match with the dictionary 
    else :
        print("\n Jarvis : Sorry boss i did not get it can you say it again ? ")
        engine.say(" Sorry boss i did not get it can you say it again ?")
        engine.runAndWait()

# =========================================================================  #      