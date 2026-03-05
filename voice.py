from gtts import gTTS
import playsound as pl
import os
import serial
import time
import speech_recognition as sr

s=serial.Serial('COM3',9600,timeout=1)

time.sleep(2)

r=sr.Recognizer()
exit=["exit"]

def speak(a):
    tts=gTTS(text=a , lang="en") 
    tts.save("tem.mp3")
    pl.playsound("tem.mp3")
    os.remove("tem.mp3")
    print(a)
   
speak("system is activating checking all the sensors and ensuring a secure mission")
while True:
    with sr.Microphone() as source:
        print("speak now")
        audio=r.listen(source)

    time.sleep(0.3)
    try:
        t=(r.recognize_google(audio).lower())
        print(t)
        s.write((t+"\n").encode())
        if t in exit:
            speak("shutting down the system and i hope you have a nice day")
            break  
        elif "jarvis" in t:
        
            print("At your service how may i help you")
            speak("At your service how may i help you")
        
        elif "ahe" in t:
            speak("moving ahead")
            s.write(('ty').encode()) 
            print(s.read())
        elif "librarian" in t:
            speak("our librarian is sir kapil natrjewan")
        elif "move back" in t:
            speak("move back")
        elif 'dont' in t or "don't" in t:
             s.write(('stop').encode()) 
             print(s.read())
        elif "introduce" in t:
            speak(" hello i am iron man developed by the students of class 9")
        elif "abilities" in t:
            speak("I am a simple chatbot havinmg abilities to answert to your basic questions, i could not answer for your arathmatic questions and answer to your advanced questions as i am not trained for that yet, i can move according to your command ,detect obsticles on my way and take movement decisions by my self")   
        elif "you" in t and "do" in t  : 
            speak("I am a simple chatbot havinmg abilities to answert to your basic questions, i could not answer for your arathmatic questions and answer to your advanced questions as i am not trained for that yet, i can move according to your command ,detect obsticles on my way and take movement decisions by my self")              
        elif "hello" in t or "hi" in t:
            s.write(('hi').encode())
            speak("hello there whats up!")
        elif ("who" in t and "developed" in t and "you" in t) :
            speak("I am developed by three studets of class 9 they are.. laboni Roy,Rituraj Mitra and, Rajdeep Dey")
        elif ("vice" in t and "principal" in t):
            speak("our vice principle is Mr.nellikunnel john george sir")
        elif "principal" in t:
            speak("our principle is Sumita Rai")
        elif "about" in t and "your" in t and "school" in t:
            speak("OUR MOTTO : CHASE THE DESIRE To fulfill the vision, North Point Residential School provides an environment in which every student discovers and realizes his full potential. The school attracts the best talented - students, teachers and facilitators - from all parts of India. North Point Residential School, as a residential school, maintains a sharp focus on the pursuit of knowledge and skill. In addition, drawing on its traditions and rich history, the school aims at the broader development of the complete personality of its students")
        elif "can" in t and "learn" in t:
            speak("yes i can improvise my knowledge with updates and training")
        elif "prime minister" in t and "india" in t:
            speak("the prime minister of india is Sri narendra damo das modi")
        elif "how" in t and "are" in t and "you" in t:
            speak("i am functioning well and ready to help you, what about you")
        elif "i" in t and "fine" in t:
            speak("that is great to here")
        elif "what" in t and "time" in t:
            tm=time.localtime()
            crt=(time.strftime("%H:%M:%S"))
            speak('the time is '+crt)
        elif "your" in t and "name" in t:
            speak("My name is jarvis")
        elif "fun fact" in t or 'funfact' in t:
            speak("the sky is blue because of the scatering of sunlight")
        elif "turn left" or "left" in t:
            s.write(('ll').encode())
        elif "turn right" or "right" in t:
            s.write(('lr').encode())
        else:
            speak("sorry i didnt understand your command or maybe i am not yet developed for that yet")
    except sr.UnknownValueError:
        speak("sorry i didnt understand your command")
    except sr.RequestError:
        speak("request error")    