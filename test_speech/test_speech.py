import speech_recognition as sr
from tracemalloc import stop
#import speech_recognition as sr
from gtts import gTTS
import playsound
import time
from datetime import datetime
from openpyxl import load_workbook
import os #ooj

import os 





def speak(text):
    tts= gTTS(text=text, lang="en")
    # date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)






def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))

    return said.lower()





with open('speaker.txt') as f:
    contents = f.readlines() 
# print(contents[-1])     
#




book = load_workbook('dataset_recommendation_default.xlsx')
sheet = book.active
rows = sheet.rows
# print(type(rows))
# print (rows)

headers = [cell.value for cell in next(rows)]
# print(headers)
all_rows = []
for row in rows:
    data = {}
    for title, cell in zip(headers, row):
        data[title] = cell.value

    all_rows.append(data)



speak("Hello mester"+ contents[-1]) 
os.remove("voice.mp3")
e=True
while e==True:
    text = get_audio()  
    if 'hand' in text:
        speak("you want to wash your hands, one second")
        qt = all_rows[0]['debit (l/min)']
        print(qt)
        os.remove("voice.mp3")
        e=False
    elif 'face' in text:
        speak("you want to wash your face, one second")
        qt = all_rows[1]['debit (l/min)']
        print(qt)    
        os.remove("voice.mp3")
        e=False

    elif 'teeth' in text:
        speak("you want to wash your teeth, one second")
        qt = all_rows[2]['debit (l/min)']
        print(qt)    
        os.remove("voice.mp3")   
        e=False 
    else:
        e=True    