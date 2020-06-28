import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import os

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    speak("the date today is ")
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)



def wishme():
    speak("welcome back madam")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12 :
        speak("Good Morning ma'am")
    elif hour >=12 and hour<18 :
        speak("Good Afternoon ma'am")
    elif hour>=18 and hour<24:
        speak("good evening ma'am")
    else:
        speak("It looks like you pulling a all nighter")        
    speak("i am jarvis at your service Hope you doing great and you safe and happy how can i help you!!")

def sendemail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sheetalsinghssr','sheetal@123')
    server.sendmail('sheetalsinghssr@gmail.com',to,content)
    server.close()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try :
        print("recognised")
        query = r.recognize_google(audio, language = "en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please")
        return "none"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'how are you' in query:
            speak("Not so good , wishing for this COVID-19 to end soon")
        elif "search" in query:
            speak("Searching    hold on")
            query = query.replace("search about","")
            result = wikipedia.summary(query,sentences=2)
            speak(result)
        elif "thanks" in query:
            speak("no sweat boss , anything else you want to know")
        elif "send mail" in query:
            try:
                speak("what should i send in mail")
                content = takecommand()
                to = 'sheetalsinghnew@gmail.com'
                sendemail(to,content)
                speak("email has been sent successfully")
            except Exception as e :
                print(e)
                speak("unable to sent email due to some error")
        elif 'play song' in query:
            songs_dir = 'C:\\Users\\user\\Desktop\\folder\\music\\new songs\\highway'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'ok bye' in query:
            speak("It was nice talking to you !! tata tata")
            quit()
            