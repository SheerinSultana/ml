import speech_recognition as sr
import webbrowser

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    
#search on google    
try:
    text=r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " +text )
    url='https://www.google.co.in/search?q='
    webbrowser.open(url+text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
