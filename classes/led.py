# pylint: disable=import-error

import RPi.GPIO as GPIO

class Led :
    #marche #arret
    
    def __init__(self, a_PWM):
        self.clignotement = 0
        
        GPIO.setup(a_PWM, GPIO.OUT)
        self.PWM = GPIO.PWM(a_PWM, 1) #GPIO clignotement 
        self.PWM.start(self.clignotement)

    def marche_led(self,pourcentage):  
        self.clignotement = pourcentage
        self.PWM.ChangeDutyCycle(self.clignotement)



    def inverse(self): ## !!!
        if self.clignotement == 0:
            self.clignotement = 100
        elif self.clignotement > 0:
            self.clignotement = 0
        
        self.PWM.ChangeDutyCycle(self.clignotement)
        