from flask import *
from demoAI import *
from pyttsx3 import *

app = Flask(__name__)
eng = Engine('sapi5')
eng.setProperty('voice', eng.getProperty('voices')[0].id)

global nm

@app.route('/')     #default Page
def demoFun():  
    #add if-else statement to collect the username
    # speak("Please Tell Your Name")
    # nm = takeCommand()
    speak(greet("Sir"))      #greeting the user at start
    return render_template('demoFlask.html', userName = "Sir")

@app.route('/', methods = ['POST'])     #once input form gets triggered this page will be loaded...
def newdemoFun():
    # a = request.form['htmlName']  #to get input field from HTML File

    x = takeCommand().lower()   #what user said
    y = working(x)              #what Voice Assistant Said
    speak(y)
    
    return render_template('demoFlask.html', comp = y, user = x.title())


@app.route('/command', methods = ['POST'])      #to open the commands page
def commandPage():
    return render_template('demoCommands.html', commandName = "demo")

@app.route('/aboutus', methods = ['POST'])      #to open the commands page
def aboutusPage():
    return render_template('demoAboutUs.html')

if __name__ == "__main__":
    app.run(debug=True)