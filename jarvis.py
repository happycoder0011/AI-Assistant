import pyttsx3 
import datetime
import SpeechRecognition as sr
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)



def wishme():
    speak("welcome back madam")
    speak("the current time is")
    time()
    speak("the date today is ")
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12 :
        speak("Good Morning ma'am")
    elif hour >=12 and hour<18 :
        speak("Good Afternoon ma'am")
    elif hour>=18 and hour<24:
        speak("good evening ma'am")
    else:
        speak("It looks like you pulling a all nighter")        
    speak("i am chumlee at your service Hope you doing great and you safe and happy how can i help you!!")
wishme()
    
def takecommand():
    r = sr.recognizer()
    with sr.microphone as source:
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

takecommand()