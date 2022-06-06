''' TTS software using Python'''

# Import libraries
import os
import pyttsx3
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Interface window
root = Tk()
root.geometry("800x600")
root.config(bg='ghost white')
root.title("Text-to-Speech :D")

#Heading
Label(root, text = "Text-TO-Speech", font = "calibri 20 bold", bg = "white smoke").pack()   

#Label asking for text entry, and variable for text
Label(root, text = "Enter Text", font = "calibri 20 bold", bg = "white smoke").place(x=20,y=60)
Msg = StringVar()

#Entry field
entry_field = Entry(root,textvariable = Msg, width ="70")
entry_field.place(x=20 , y=100)

#TTS function using gTTS
'''def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save("Speech.mp3")
    playsound("Speech.mp3")
    os.remove("Speech.mp3")'''

#Alternate TTS function using pyttsx3
def Text_to_speech():
      engine = pyttsx3.init()
      engine.say(entry_field.get())
      engine.runAndWait()

#Exit function
def Exit():
    root.destroy()

#Reset function
def Reset():
    Msg.set("")

#Define buttons
Button(root, text = "PLAY", font = "calibri 20 bold", command = Text_to_speech, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'calibri 20 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'RESET', font='calibri 20 bold', command = Reset).place(x=175 , y =140)

root.mainloop()