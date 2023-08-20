import datetime
import webbrowser
import os
import wikipedia
import pygame
import psutil
import cv2
import pywhatkit as kit
from requests import get

class Tasks:
    """Tasks can be performed:-
       1)open web browser
       2)search queries on search engine
       3)send messages
       4)get time
       5)capture images
       6)open command prompt or other applications
       7)get ip address
    """
    def __init__(self, voice_recognition):
        self.voice_recognition = voice_recognition


    def search_wikipedia(self, user_voice):
        """search query on wikipedia
           uses wikipedia module:- 1)control the input query size
                                   2)control output feedback size
        """
        print("Searching for Wikipedia")
        search_query = user_voice[user_voice.find(' ') + 1:]
        results = wikipedia.summary(search_query, sentences=2)
        print(results)
        self.voice_recognition.speak("According to Wikipedia")
        self.voice_recognition.speak(results)


    def open_youtube(self):
        """playing videos on youtube
           uses pywhatkit module(uses playonyt function for playing input request)
        """
        print("Sir, what should I search on Youtube?")
        self.voice_recognition.speak("Sir, what should I search on Youtube?")
        self.search = self.voice_recognition.take_command()
        kit.playonyt(self.search)


    def open_google(self):
        """searching query on google
           uses webbrowser module
        """
        print("Sir, what should I search on Google?")
        self.voice_recognition.speak("Sir, what should I search on Google?")
        self.search = self.voice_recognition.take_command()
        webbrowser.open(self.search)


    def stop_media(self):
        """stop the media player
           uses psutil module:- can be used to stop requested application
        """
        def find_media_pid():
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == 'Microsoft.Media.Player.exe':
                    return proc.pid
            return None

        media_pid = find_media_pid()

        if media_pid != None:
            os.kill(media_pid, 9)


    def get_current_time(self):
        """
        give current time uses datetime module
        """
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.voice_recognition.speak(f"Sir, the time is {current_time}")


    def open_camera(self):
        """open camera and captures images
           uses cv2 module:- can control frame rate and pause time
        """
        self.cam = cv2.VideoCapture(0)
        cv2.namedWindow("Camera")
        img_counter = 0
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("Failed to grab frame")
                break
            cv2.imshow("Camera", frame)
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = f"opencv_frame_{img_counter}.png"
                cv2.imwrite(img_name, frame)
                print(f"{img_name} written!")
                img_counter += 1
        self.cam.release()
        cv2.destroyAllWindows()


    def send_whatsapp_message(self):
        """send messages on whatsapp
           uses pywhatkit module:- 1)take phone no, time, message as input
                                   2)adjust time at which message to be send
        """
        self.country_code = 91
        self.phone_number = input("Enter the phone number: ")

        user_voice = self.voice_recognition.take_command()
        self.message = user_voice if user_voice != "None" else ""

        self.time = input("Enter the time in HH:MM format (24-hour): ")

        self.full_phone_number = f"+{self.country_code}{self.phone_number}"
        kit.sendwhatmsg(self.full_phone_number, self.message, int(self.time[:2]), int(self.time[3:]))


    def open_stackoverflow(self):
        #open stackoverflow uses webrowser module
        webbrowser.open("https://stackoverflow.com/")


    def open_instagram(self):
        #open instagram uses webrowser module
        webbrowser.open("https://www.instagram.com/")


    def open_whatsapp(self):
        #open whatsapp uses webbrowser module
        webbrowser.open("https://web.whatsapp.com/")


    def open_facebook(self):
        #open facebook uses webrowser module
        webbrowser.open("https://www.facebook.com/")


    def open_notepad(self):
        #open notepad uses os module (path needed to be described)
        self.path = "C:\\Windows\\Notepad"
        os.startfile(self.path)


    def open_command_prompt(self):
        #open command prompt uses os module 
        os.system("start cmd")


    def ip_address(self):
        #get ip address
        self.ip = get("https://api.ipify.org").text
        print(self.ip)
        self.voice_recognition.speak(f"Your IP address is {self.ip}")
    


class MusicPlayer:
    """Play music (uses pygame, os module)
       os module:- 1)used to load songs
                   2)used to select songs
       pygame module:- 1)used to play, pause, unpause, stop the song
       """
    def __init__(self, voice_recognition):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_song = 0
        self.voice_recognition = voice_recognition
    
    def load_songs_from_folder(self, folder_path):
        #go to the available song folder uses os module
        songs = os.listdir(folder_path)
        self.playlist = [os.path.join(folder_path, song) for song in songs if song.endswith(".mp3")]

    def play(self):
        #play the songs uses pygame module
        pygame.mixer.music.load(self.playlist[self.current_song])
        pygame.mixer.music.play()

    def pause(self):
        #pause the songs uses pygame module
        pygame.mixer.music.pause()

    def unpause(self):
        #unpause the songs uses pygame module
        pygame.mixer.music.unpause()

    def stop(self):
        #stop the songs uses pygame module
        pygame.mixer.music.stop()

    def next_song(self):
        #play the next song
        self.stop()
        self.current_song = (self.current_song + 1) % len(self.playlist)
        self.play()

    def choose_song(self):
        #select the song among the given songs
        print("Select a song:")
        for i, song_path in enumerate(self.playlist):
            print(f"{i+1}. {os.path.basename(song_path)}")

        choice = int(input("Enter the number of the song: "))
        if choice > 0 and choice <= len(self.playlist):
            self.stop()
            self.current_song = choice - 1
            self.play()
        else:
            print("Invalid choice.")

        
    def get_user_choice(self):
        #give available features for playing music 
        print("\n1. Play\n2. Pause\n3. Unpause\n4. Stop\n5. Next Song\n6. Choose Song\n7. Exit")
        choice = input("Enter your choice: ")
        return choice

    def run(self):
        #run above functions using given voice input
        while True:
            user_voice = self.voice_recognition.take_command()

            if "play" in user_voice:
                self.play()

            elif "pause" in user_voice:
                self.pause()

            elif "unpause" in user_voice:
                self.unpause()

            elif "stop" in user_voice:
                self.stop()

            elif "next song" in user_voice:
                self.next_song()

            elif "select song" in user_voice:
                self.choose_song()

            elif "exit" in user_voice:
                break

            else:
                print("Invalid choice. Try again.")
