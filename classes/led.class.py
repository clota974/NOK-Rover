# pylint: disable=import-error

import RPi.GPIO as GPIO

class Led :
    #marche #arret
    clignotement = 0
    def __init__(self, a_PWM):
        self.PWM = GPIO.PWM(a_PWM, 1) #GPIO clignotement #### pylint: disable=undefined-variable
        self.PWM.start(self.clignotement)

    def marche_led(self,pourcentage): ## Self ! 
        self.clignotement = pourcentage
        self.PWM.ChangeDutyCycle(self.clignotement)



    def inverse(self): ## !!!
        if self.clignotement == 0:
            self.PWM.ChangeDutyCycle(100)
        elif self.clignotement > 0:
            self.PWM.ChangeDutyCycle(0)

        ## self.clignotement ?