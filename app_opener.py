import subprocess
import os
import jarvis as je

def open_the_app(query):
    #query contains the text which is converted from speech to text
    #when in the jarvis.py user says 'open the' or 'close the' then control is redirected to this script
    #here o_t_a contains the app keywords and function is stored as a value
    #when any keywords matched associated operations are performed
    
    o_t_a={"jupyter notebook":jupyter_notebook,"jupyter":jupyter_notebook,"chrome":open_chrome,"sublime":open_sublime,"news reader application":news_reader,"android studio":android_studio,"notepad":notepad,"visual studio":visual_studio,
    
    
    }
    
    #suppose u want to open the chrome then say open the chrome
    #it will check weather chrome is there in the o_t_a or not
    #but chrome is there ("chrome":open_chrome) in o_t_a therefore associated function will run whuch is open_chrome
    for each_app in o_t_a:
        try:
            if each_app in query.lower():
                o_t_a[each_app](query)
                break
        except:
            pass
    else:
        je.speak("Sir I do not have the access of this app till now")
    
    return

def open_chrome(query):
    try:
        #if user says open the chrome then below if block will run for opeining the chrome
        if "open" in query.lower():
            je.speak("opening the chrome application")
            #here pecify the path of the chrome.exe of your chrome browser
            #u can get this path from properties and copy the Target path of the application
            subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            return
        elif "close the chrome" in query.lower():
            #here if close the chrome is there in the query then it will close the browser
            je.speak("Closing the chrome application")
            os.system("TASKKILL /F  /IM chrome.exe")
            return
    except:
        pass
#similarly add your own apps
def open_sublime(query):
    try:
        if "open the sublime" in query.lower():
            je.speak("opening the sublime application")
            subprocess.Popen(r"C:\Program Files\Sublime Text 3\sublime_text.exe")
            return
        elif "close the sublime" in query.lower():
            je.speak("closing the sublime application")
            os.system("TASKKILL /F /IM sublime_text.exe")
            return
    except:
        pass
def news_reader(query):
    try:
        if "open the news reader" in query.lower():
            je.speak("opening the news reader application")
            subprocess.Popen(r"C:\Users\Dell\Desktop\LearnPython\web Scrapping\news reader\dist\NewsReader.exe")
            return
        elif "close the news reader" in query.lower():
            je.speak("closing the news reader application")
            os.system("TASKKILL /F /IM NewsReader.exe")
            return
    except:
        pass

def notepad(query):
    try:
        if "open the notepad" in query.lower():
            je.speak("opening the notepad++ application")
            subprocess.Popen(r"C:\Program Files\Notepad++\notepad++.exe")
            return
        elif "close the notepad" in query.lower():
            je.speak("closing the notepad application")
            os.system("TASKKILL /F /IM notepad++.exe")
            return
    except:
        pass

def android_studio(query):
    try:
        if "open the android studio" in query.lower():
            je.speak("opening the android studio application")
            subprocess.Popen(r"C:\Program Files\Android\Android Studio\bin\studio64.exe")
            return
        elif "close the android studio" in query.lower():
            je.speak("closing the android studio application")
            os.system("TASKKILL /F /IM studio64.exe")
            return
    except:
        pass

def visual_studio(query):
    try:
        if "open the visual studio" in query.lower():
            je.speak("opening the visual studio code application")
            subprocess.Popen(r"C:\Users\Dell\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            return
        elif "close the visual studio" in query.lower():
            je.speak("closing the visual studio code application")
            os.system("TASKKILL /F /IM Code.exe")
            return
    except:
        pass
def jupyter_notebook(query):
    if 'open' in query.lower() and 'jupyter' in query.lower():
        je.speak("opening the jupyter notebook")
        os.system('cmd /k "jupyter notebook"')
        return




