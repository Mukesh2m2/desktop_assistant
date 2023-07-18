import datetime
from tasks import Tasks
from speech import TextToSpeech_and_SpeechToText
from tasks import MusicPlayer

class Jarvis:
    """Main class which act as interlink between various files
       it uses datetime module for greet function
       it uses imported tasks and speech file for understanding and execution of command
    """
    def __init__(self):
        self.voice_recognition = TextToSpeech_and_SpeechToText()
        self.tasks = Tasks(self.voice_recognition)
        self.music = MusicPlayer(self.voice_recognition)

    def greet(self):
        """greet the user in beggining based on time
           uses datetime module
        """
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.voice_recognition.speak("Good Morning Sir, I am Jarvis. How may I help you?")
        elif 12 <= hour < 17:
            self.voice_recognition.speak("Good Afternoon Sir, I am Jarvis. How may I help you?")
        else:
            self.voice_recognition.speak("Good Evening Sir, I am Jarvis. How may I help you?")

    def run(self):
        """connect the input text query converted by speech to text conversion function to various
           tasks"""
        self.greet()

        while True:
            user_voice = self.voice_recognition.take_command()

            if "wikipedia" in user_voice:
                self.tasks.search_wikipedia(user_voice)

            elif "youtube" in user_voice:
                self.tasks.open_youtube()

            elif "google" in user_voice:
                self.tasks.open_google()

            elif "notepad" in user_voice:
                self.tasks.open_notepad()

            elif "command prompt" in user_voice:
                self.tasks.open_command_prompt()

            elif "open camera" in user_voice:
                self.tasks.open_camera()

            elif "play music" in user_voice:
                folder_path = "C:\\Songs"  
                self.music.load_songs_from_folder(folder_path)
                self.music.run()

            elif "stop media player" in user_voice:
                self.tasks.stop_music()

            elif "time" in user_voice:
                self.tasks.get_current_time()

            elif "send message" in user_voice:
                self.tasks.send_whatsapp_message()

            elif "instagram" in user_voice:
                self.tasks.open_instagram()

            elif "whatsapp" in user_voice:
                self.tasks.open_whatsapp()

            elif "facebook" in user_voice:
                self.tasks.open_facebook()

            elif "ip address" in user_voice:
                self.tasks.ip_address()

            elif "stop jarvis" in user_voice:
                break


if __name__ == "__main__":
    #Here execution of code start which calls Jarvis class
    execution = Jarvis()
    execution.run()