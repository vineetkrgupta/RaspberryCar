from flask import Flask
#, render_template,request,redirect,url_for
import RPi.GPIO as GPIO
from time import sleep
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#motor A
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

#motor B
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

en = 25 #//orange
enb=  22  #//yellow

GPIO.setup(en,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
p=GPIO.PWM(en,1000)

pb=GPIO.PWM(enb,1000)


p.start(100)
pb.start(100)



app = Flask(__name__)
last =0
@app.route("/f")
def forward():
    threading.Thread(target=do_forward).start()
    return ("", 204)
def do_forward():
    global last
    last =1
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
#    sleep(0.8)
#    GPIO.output(17, GPIO.LOW)
#    GPIO.output(27, GPIO.LOW)
#    GPIO.output(23, GPIO.LOW)
#    GPIO.output(24, GPIO.LOW)
    return ('', 204)
    
@app.route("/s")
def stop():
    threading.Thread(target=do_stop).start()
    return ('', 204)
def do_stop():
    global last
    last =0
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    return ('', 204)
#@app.route("/backwards")
    
@app.route("/speed/<spd>")
def speed():
    threading.Thread(target=do_speed).start()
    return ('', 204)
def do_speed(spd):
    global p
    global pb
    if spd=="1":
        p.ChangeDutyCycle(50)
        pb.ChangeDutyCycle(50)
    elif spd=="2":
        p.ChangeDutyCycle(75)
        pb.ChangeDutyCycle(75)
    elif spd=="3":
        p.ChangeDutyCycle(75)
        pb.ChangeDutyCycle(75)
    return ('', 204)

@app.route("/b")
def backward():
    threading.Thread(target=do_backward).start()
    return ('', 204)
def do_backward():
    global last
    last =-1
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
#   sleep(0.8)
#   GPIO.output(17, GPIO.LOW)
#   GPIO.output(27, GPIO.LOW)
#   GPIO.output(23, GPIO.LOW)
#   GPIO.output(24, GPIO.LOW)
    return ('', 204)

@app.route("/l")
def left():
    threading.Thread(target=do_left).start()
    return ('', 204)
def do_left(): 
    global last

    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    sleep(0.06)
    #sleep(60)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    if(last == 1):
        #p.ChangeDutyCycle(70)
        #pb.ChangeDutyCycle(70)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        #p.ChangeDutyCycle(100)
        #pb.ChangeDutyCycle(100)
    elif(last == -1):
        #p.ChangeDutyCycle(70)
        #pb.ChangeDutyCycle(70)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        #p.ChangeDutyCycle(100)
        #pb.ChangeDutyCycle(100)
    return ('', 204)
    
@app.route("/r")
def right():
    threading.Thread(target=do_right).start()
    return ('', 204)
def do_right():
    global last

    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    sleep(0.06)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    if(last == 1):
#        p.ChangeDutyCycle(70)
#        pb.ChangeDutyCycle(70)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
#        p.ChangeDutyCycle(100)
#        pb.ChangeDutyCycle(100)
    elif(last == -1):
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
#        p.ChangeDutyCycle(100)
#        pb.ChangeDutyCycle(100)
    return ('', 204)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
