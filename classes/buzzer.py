# pylint: disable=import-error
import RPi.GPIO as GPIO

class Buzzer :
    #marche #arret
    
    def __init__(self, a_PWM):
        self.allume = 0
        """
        Args:
            self
            a_PWM (int): 
        """
        GPIO.setup(a_PWM, GPIO.OUT)
        self.PWM = GPIO.PWM(a_PWM, 2048)
        self.PWM.start(self.allume)




    def start(self, etat):
        """
        Mise en route du buzzer

        Args:
            self
            etat (bool): la frequence est invariable
        """
        self.allume = etat
        pourcentage = 50 if etat else 0 # 50 afin d'imiter une sinusoide
        self.PWM.ChangeDutyCycle(pourcentage)

    def inverse(self):
        self.start(not self.allume)
