import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''it wishes me every time i start this function, according to the time'''
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=11:
        speak("Good morning Sir")
    elif hour>11 and hour<=18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis sir. Please tell me how may I help you!")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print('user said:- {}'.format(query))
    
    except:
        #print(e)
        print("sorry say that again please..")
        return "none"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file2=open('D:\\MOVIES\\hollywood\\MARVEL\\Doctor Strange (2016) [1080p] [YTS.AG]\\pass.txt','r')
    a=file2.read()
    server.login('210gaurav@gmail.com', a)
    server.sendmail('210gaurav@gmail.com',to,content)
    server.close()
def remove(string):
    return string.replace(" ","")

        

if __name__ == "__main__":
    wishMe()
    #speak("my name is Gaurav. i am a product of Mr.Gaurav")
    while True:
        query=takecommand().lower()
        '''logic to execute the tasks said'''
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace('wikipedia', "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube.")
            webbrowser.open("youtube.com")
        elif 'how are you' in query:
            speak("i am fine sir, and hope that you are also fine")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("web.whatsapp.com")
        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            webbrowser.open("stackoverflow.com")
        elif 'show movies' in query:
            speak("playing movies")
            movies_dir='D:\\MOVIES'
            types=os.listdir(movies_dir)
            print(types)
            speak("please say the type of movie you want to watch")
            mov_type_query=takecommand().lower()
            if 'hollywood' in mov_type_query:
                speak("here is the list of hollywood movies")
                holly_dir='D:\\MOVIES\\hollywood'
                holly_list=os.listdir(holly_dir)
                print(holly_list)
                os.startfile(os.path.join(holly_dir, holly_list[random.randrange(0,len(holly_list))]))
            elif 'bollywood' in mov_type_query:
                speak("hesre is the list of bollywood movies")
                bolly_dir='D:\\MOVIES\\bollywood'
                bolly_list=os.listdir(bolly_dir)
                print(bolly_list)
                os.startfile(os.path.join(bolly_dir, bolly_list[random.randrange(0,len(bolly_list))]))
            else:
                speak("hesre is the list of tollywood movies")
                tolly_dir='D:\\MOVIES\\tollywood'
                tolly_list=os.listdir(tolly_dir)
                print(tolly_list)
                os.startfile(os.path.join(tolly_dir, tolly_list[random.randrange(0,len(tolly_list))]))
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is {}".format(strtime))
        elif 'open code' in query:
            code_path="C:\\Users\\Gaurav Ghosh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("searching the path for you..")
            os.startfile(code_path)
        elif 'send mail' in query:
            try:
                mail='@gmail.com'
                speak("what should i say to him...")
                content=takecommand()
                speak("what is the username")
                to_sps = takecommand()
                to1=remove(to_sps)
                to=to1+mail
                sendEmail(to,content)
                speak("email has been sent..")
            except:
                speak("sorry email was not been sent.")    
        elif 'jarvis close' in query:
            speak("closing my system")
            sys.exit("bye")

                 


