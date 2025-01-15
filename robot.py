from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, True)

@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/controle')
def controle():
   data1="CTRL"
   GPIO.output(2 , False)
   time.sleep(2)
   GPIO.output(2, True)
   return 'true'

if __name__ == "__main__":
 print("Start")
 app.run(host='0.0.0.0',port=80) 
