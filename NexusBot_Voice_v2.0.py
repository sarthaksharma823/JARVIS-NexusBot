import pyttsx4  #this library is used for text-to-speech
import speech_recognition as sr #This loads a library that captures sound from your microphone and converts it into text.

engine = pyttsx4.init() #initilization of pyttsx4 library 

recognizer = sr.Recognizer()

voice = engine.getProperty('voice')
engine.setProperty('rate',190)

def ico_mic():
    with sr.Microphone() as source:
        print("\n Jarvis : Calibrating background noise ...[Please wait]")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.energy_threshold = 300
        recognizer.pause_threshold = 0.8

def listen():
    with sr.Microphone() as source:
        print("\n Jarvis : Listening ...")

        try: 
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return None    

        try:
            print("\n Jarvis : Recognizing....")
            query = recognizer.recognize_google(audio, language= 'en-IN')
            print(f"\n You said : {query}")
            return query.lower().strip()

        except Exception:
            return None

def speak(text):
    print(f"\n Jarvis : {text}")
    engine.say(text)
    engine.runAndWait()

brain = {
    "hello jarvis": "Hi Boss, how can I help you today?",
    "good morning": "Good morning Boss!",
    "what are you doing Jarvis" : "Nothing Boss !!",
    "good afternoon": "Good afternoon Boss!",
    "what is your name": "My name is Jarvis, Boss",
    "offline": "Okay sir, shutting down Jarvis systems. See you soon!",
    "who made you": "I am made by Sarthak.."
}    

if __name__ == "__main__":
    ico_mic()
    speak("Jarvis system is online boss...")

    while True:
        user_input = listen()

        if not user_input:
            continue

        if user_input == "offline":
            speak(brain["offline"])
            break

        elif user_input in brain:
            speak(brain[user_input])

        else: 
            speak("Sorry you didnot add this in my brain yet ...")    
 