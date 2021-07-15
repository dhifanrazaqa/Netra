import os
import tkinter as tk
import speech_recognition as sr
import pyttsx3

master = 'user'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
r= sr.Recognizer()
speech = sr.Microphone(device_index=1)

def speak(text) :
    engine.say(text)
    engine.runAndWait()


def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)




root = tk.Tk()
root.title("Object Detection")

canvas1 = tk.Canvas(root, width=480, height=760, bg='ivory2', relief='raised')
canvas1.pack()
canvas1.create_rectangle(0, 0, 500, 70, fill='OliveDrab4')
canvas1.create_oval(80, 200, 400, 520, outline='OliveDrab4', fill='OliveDrab4')


#speak("Halo, selamet daeteng")
mic_butt = tk.PhotoImage(file="b.png")


_weight = "yolov5s.pt"





def takecmd():
    speak("Halo Apa yang bisa saya bantu?")

    with speech as source :
        speak ("Mendengarkan...")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try :
            speak("Mengenali..")
            query = r.recognize_google(audio, language='id-ID')
            print('u said : '+ query)
            if "uang"in query:
                os.system("python moneyDetector.py")
                query = 'Null'
            elif "tulisan" in query:
                os.system("python letterReader.py")
            elif "depan" in query:
                os.system("python objectDetector.py")
            elif "jumpa" in query:
                return 0
        except Exception as e:
            speak("Maaf bisa anda ulang lagi?")
            query = 'Null'
        return  query


button1 = tk.Button(root, image=mic_butt, command=takecmd, borderwidth=0, width=460, height=650, activebackground="DarkOliveGreen1")


canvas1.create_window(241, 405, window=button1)

root.mainloop()