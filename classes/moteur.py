# pylint: disable=import-error
import RPi.GPIO as GPIO

class Moteur :
    #marche 
    
    def __init__(self, a_IN1, a_IN2, a_PWM) :
        self.vitesse = 0
        self.a_IN1 = a_IN1
        self.a_IN2 = a_IN2
        self.a_PWM = a_PWM

        GPIO.setup(self.a_IN1, GPIO.OUT)
        GPIO.setup(self.a_IN2, GPIO.OUT)
        GPIO.setup(self.a_PWM, GPIO.OUT)

        self.PWM = GPIO.PWM(a_PWM, 980)
        self.PWM.start(self.vitesse)

    def start(self, vitesse):
        self.vitesse = vitesse

        if(vitesse < 0):
            GPIO.output(self.a_IN1, 0)
            GPIO.output(self.a_IN2, 1)
        elif(vitesse > 0):
            GPIO.output(self.a_IN1, 1)
            GPIO.output(self.a_IN2, 0)
        else: # If vitesse==0
            GPIO.output(self.a_IN1, 1)
            GPIO.output(self.a_IN2, 1)

        self.PWM.ChangeDutyCycle(abs(self.vitesse))


