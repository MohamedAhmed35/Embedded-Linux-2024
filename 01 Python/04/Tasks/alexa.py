# pip insatll speachRecognition
# pin install pyaudio

import speech_recognition as sr
import os
from time import sleep
from datetime import datetime
import webbrowser
from gtts import gTTS
import vlc
import threading


class voice_assistant:

    # obtain audio from the microphone
    recognizer = sr.Recognizer()

    # record audio
    def record_audio(self):
        with sr.Microphone() as source:
            print("Listening....")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            # audio = None
            # while audio == None:
            #     print("Listening....")
            #     audio = self.recognizer.listen(source)
        return audio

    # recognize speech using Google speach Recognition
    def recognize_speech(self, audio):
        try:
            text:str = self.recognizer.recognize_google(audio, language = "ar-EG")
            print(f'You said: {text}')
            return text
            # respond(text)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, there was an error processing your request")
        return ''


    # Speak
    def speak(self, audio):
        tts = gTTS(audio, lang = 'ar', slow = False)

        # Saving the converted audio in mp3 format
        tts.save('audio.mp3')
        p = vlc.MediaPlayer('audio.mp3')
        p.play()
        sleep(10)
        os.remove('audio.mp3')


def searchWordInString(world_list, text):
    # Find words from word_list in the string
    foundWord = [word for word in world_list if word in text]
    return len(foundWord) != 0


def respond(voice_in):

    if searchWordInString(['هلا', 'اهلا', 'مرحبا', 'هاي', 'hello'], voice_in):
        alexa.speak('مرحبا بك محمد')
        # t2.join()

    if searchWordInString(['اسمي', 'انا مين', 'تعرفني'], voice_in):
        alexa.speak('المهندس محمد')
        # t2.join()

    if searchWordInString(['النهاردة', 'النهارده', 'اليوم', 'التاريخ', 'يوم'], voice_in):
        day = datetime.now().strftime("%a %b %d %Y")
        alexa.speak('اليوم' + day)
        # t2.join()
    
    if searchWordInString(['الساعة', 'الساعه', 'كام', 'الوقت', 'time'], voice_in):
        time = datetime.now().strftime("%I:%M")
        alexa.speak('الساعة الان' + time)
        # t2.join()

    if searchWordInString(['جوجل', 'google'], voice_in):
        webbrowser.open('google.com')
        

    if searchWordInString(['فيس', 'فيس بوك', 'فيسبوك', 'facebook'], voice_in):
        webbrowser.open('facebook.com')
        

    if searchWordInString(['يوتيوب', 'اليوتيوب', 'youtube'], voice_in):
        webbrowser.open('youtube.com')


    if searchWordInString(['الكود', 'كود', 'code'], voice_in):
        os.system('code')
        


alexa = voice_assistant()

if datetime.now().strftime("%H") > str(12):
    t1 = threading.Thread(target = alexa.speak, args = ('مساء الخير', ))
else:
    t1 = threading.Thread(target = alexa.speak, args = ('صباح الخير', ))

t1.start()
sleep(2)

while True:
    audio = alexa.record_audio()
    voice_in = alexa.recognize_speech(audio)
    respond(voice_in)

    # t2 = threading.Thread(target = alexa.recognize_speech, args = (audio, ))
    # t2.start()
    

