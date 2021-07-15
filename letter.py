import pytesseract
import cv2
import pyttsx3
import numpy as np


engine = pyttsx3.init()
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

voice = engine.getProperty('voices')

engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_idID_Andika")

pytesseract.pytesseract.tesseract_cmd = 'G:\\1ADhifan\\tsr\\tesseract.exe'
img = cv2.imread("1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
result = pytesseract.image_to_string(img)
result = result.replace('©', '')
print(result)
engine.say(result)
engine.runAndWait()