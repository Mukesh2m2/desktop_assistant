import pyttsx3
import speech_recognition as sr


class TextToSpeech_and_SpeechToText:
    """Text to speech (using speak function) uses pyttsx3 module.
       *gives voice feedback to user as output.

       Speech to text(using take_command function) uses google api. 
       *input voice recognized by microphone converted to text."""

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def speak(self, audio):
        """Text to speech conversion:-
           uses pyttsx3 which have:- 1)two voices male(David) and female(Zira)
        """
        self.engine.say(audio)
        self.engine.runAndWait()
    
    def take_command(self):
        """Speech to text conversion:-
           uses google api :- 1)can adjust input according to noisy environment
                              2)can adjust input time for speech query
           
           *send text input for further execution of command in lower string
        """
        with sr.Microphone() as source:
            self.speak("Listening...")
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing voice...")
            user_voice = self.recognizer.recognize_google(audio)
            print(f"You said: {user_voice}\n")

        except Exception as e:
            print(e)
            print("Can't recognize, try once again!")
            self.speak("Can't recognize, try once again!")
            return "None"

        return user_voice.lower()
