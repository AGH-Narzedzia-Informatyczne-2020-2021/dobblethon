
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Mów :')
    audio = r.listen(source)

try:
    text = r.recognize_google(audio,None, "pl-PL")
    print("Powiedziałeś : {}". format(text))
except:
    print("Nie zrozumiałem")

