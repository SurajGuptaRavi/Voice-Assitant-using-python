import wikipedia
import jarvis as je
import pywhatkit as kit
import os
import requests

#when user says 'tell me something about' topic_name
#then wikipedia search is made and assistant search the topic and reads the respons get by the asstant from wikipedia also it prints the response in the terminal
def wiki_search(query):
    query = query.replace("tell me something about",'')
    result = wikipedia.summary(query)
    print("zenny:"+str(result))
    je.speak("According to Wikipedia")
    je.speak(str(result))
    return

#when user says starts music music_name or stop the music then this function is called this function always open the new tab of default browser
#if its already open then it forcefull closes and again start a default broswer so be carefull whie using
def open_youtube(query):
     
    try:
        query = query.replace('jarvis','')
        if "stop the music" in query.lower() or "music band karo" in query.lower():
            je.speak("Stoping the music sir")
            os.system("TASKKILL /F /IM chrome.exe")
            return
        os.system("TASKKILL /F /IM chrome.exe")
        
    except:
        pass
    query = query.replace("open youtube","").replace("drop my needle","").replace("play",'')
    je.speak("Playing "+query+" Sir")
    kit.playonyt(query)
    return

#just say 'shutdown the pc'
#and it will shutdown the pc in 10 seconnds
#you can also specify the times in seconds 
def shutdown_pc(query):
    if "shutdown" in query.lower() and "pc" in query.lower():
        je.speak("shutting Down the pc in 10 seconds")
        kit.shutdown(time=10)
        return
    
#just say 'restart the pc'
#it will restart the pc
def restart_pc(query):
    if "restart" in query.lower() and "pc" in query.lower():
        je.speak("restarting  the pc in 10 seconds")
        os.system("shutdown /r /t 1")
        return 

#now to use this feature just say weather updates it will tell u about weather for ur city
def weather_forecast(query):
    try:
        city_name = "vasai road"#replace it with your city
        api_id = 'your api id'#just enter your api id here encloded in ''
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_id}&units=metric"
        res = requests.get(url)
        data = res.json()
        
        je.speak("temperature is"+str(data['main']['temp']) +'degree celsius')
        je.speak("humidity is"+str(data['main']['humidity']) + ' percent')
        je.speak(str(data['clouds']['all']) +' percent clouds will be there')
        je.speak('wind speed is '+str(data['wind']['speed']) +'kilometer per hour')
    except:
        pass

#to do google search just say 'make search oon google' and topic
def topic_search(query):
    topic = query.lower().replace("make","").replace("search","").replace("on google","")
    je.speak("making the google search...")
    kit.search(topic)#Will perform a Google search
    return





