# ====================================================================
# PROJECT NAME: EASY AI CHATBOT TEMPLATE (Version 1.0)
# DEVELOPER: Sarthak
# DESCRIPTION: A clean, no-dependency text chatbot skeleton. 
# HOW TO USE: Just add your custom questions and answers in the 'brain' dictionary!
# ====================================================================

# CUSTOMIZE YOUR CHATBOT HERE:
# left side = keys (that you will say) and right side  = values (that your chatbot say)
brain = {
    "hello": "Hi sir, how can I help you today?",
    "good morning": "Good morning sir!",
    "good afternoon": "Good afternoon sir!",
    "who are you": "I am a customizable AI chatbot template.",
    "what is your name": " usually my name is Jarvis but You haven't named me yet! Edit the code to give me a name.",
    "offline": "Okay sir, shutting down Jarvis systems. See you soon!",
    "who made you": "I am made by Sarthak.."
}

# ====================================================================
# CORE LOGIC (Do not change this unless you know what you are doing)
# ====================================================================

print("CHATBOT: Systems Online. Type your command below.")

while True:
    # Taking inputs from user (without any stuff of capital letters and space)
    user_input = input("\nYou: ").lower().strip()
    
    # if user press enter without type anything 
    if not user_input:
        continue
        
    # command of off the system 
    if user_input == "offline" or user_input == "quit":
        print(f"CHATBOT: {brain['offline']}")
        break
        
    # finding answers in dictionary 
    if user_input in brain:
        reply = brain[user_input]
    else:
        # i it dos not find the answer in dictionary so the defalut system work 
        reply = f"I am sorry, I don't understand '{user_input}'. You can add this command in my 'brain' dictionary inside the code."
        
    print(f"CHATBOT: {reply}")  #chatbot reply .....