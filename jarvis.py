                                                                                #created by Suraj Rajesh Gupta
                                                                                #github https://github.com/MaiHuJarvis
                                                                                #you can modify and use this scripts
                                                                                #but dont forget to give credits

import pyttsx3
import speech_recognition as sr
import mathematics
import internet_task
import app_opener
import datetime
import base64
def speak(audio):
    engine = pyttsx3.init()
       
    voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('voice', voice_id)
    engine.say(audio)
    engine.runAndWait()
    

def time():
    
    speak("Time is "+str(datetime.datetime.now())[11:16])
    print("Jarvis:"+str(datetime.datetime.now())[11:16])
    return str(datetime.datetime.now())[11:13]

def zenny():
    print("Jarvis:"+"For you Always sir")
    speak("for you always sir")
#this function is for wishing
def wishme():
    
    current_time = int(time())
    if current_time < 12:
        speak('Good Morning Sir')
    elif current_time < 16:
        speak("Good Afternoon Sir")
    elif current_time <= 19:
        speak("Good Evening Sir")  
    elif current_time >=20:
        speak("Good Night Sir")
    internet_task.weather_forecast("nothing")
def me():
    speak("My Name is Jarvis And I am your Assistant Sir")

def hey():
    speak("hello Sir")
    speak("how can i help you")
def listen_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       
        
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        
        query = r.recognize_google(audio,language='en-in')
        print("Recognizing.....")
        print("user:"+query)
        
    except:
        
        return 

    return query

if __name__ == "__main__":
    wishme()
    #commands dictionary contains the key and value pair
    #where key's are keywords when it is said by the user then associated functions are fired and operations are performed
    commands={'restart pc':internet_task.restart_pc,'restart the pc':internet_task.restart_pc,'shutdown the pc':internet_task.shutdown_pc,"search on google":internet_task.topic_search,"make search on google":internet_task.topic_search,'weather updates':internet_task.weather_forecast,'close the':app_opener.open_the_app,'open the':app_opener.open_the_app,'start music':internet_task.open_youtube,'music band':internet_task.open_youtube,'stop music':internet_task.open_youtube,'shutdown pc':internet_task.shutdown_pc,'play':internet_task.open_youtube,'youtube music':internet_task.open_youtube,'play songs':internet_task.open_youtube,'gaane sunao':internet_task.open_youtube,'bhakti gaane':internet_task.open_youtube,'have some music':internet_task.open_youtube,'bhakti song':internet_task.open_youtube,'geet':internet_task.open_youtube,'songs':internet_task.open_youtube,'something about':internet_task.wiki_search,'are you there':zenny,'subtract':mathematics.sub,'subtraction':mathematics.sub,'your name':me,'wish me':wishme,'divide':mathematics.div,'division':mathematics.div,'multiply':mathematics.mult,'time':time,'what is the time':time,'time kya hua jarvis':time,'addition':mathematics.add,'add':mathematics.add,'multiplication':mathematics.mult,'divide':mathematics.div}
    while True:
        #speak(base64.a85decode(b'FD,B0+DGm>@rc-hFCeu*@X0);F`Lo*+ECn*ATMN-B6A08@/').decode())
        

        dt = str(datetime.datetime.now())[11:19]
       
        if  str(dt[3:5]) =='00'  and str(dt[6:7]) =='0':#int(dt[0:2])%3 ==0 and 
            print(dt)
            wishme()
            
        try:
            query =str(listen_command()).lower()
            
            #if exit is there in the query then this program will end 
            if 'exit' in query:
                
                speak("Bye sir... ThankYou For using me")
                break
            
            for each_command in commands:
                try:    
                    if each_command in query:
                        commands[each_command]()
                        break
                except:
                    pass
                try:    
                    if str(each_command) in query:
                        commands[str(each_command)](query)
                        break
                except Exception as e:
                    print(e)
                
                    
                   
        except Exception as e:
           print(e)
           break


