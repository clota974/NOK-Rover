# pylint: disable=import-error
import RPi.GPIO as GPIO

class Buzzer :
    #marche #arret
    allume = 1
    def __init__(self, a_PWM):
        """
        Args:
            self
            a_PWM (int): 
        """
        self.PWM = GPIO.PWM(a_PWM, 1024)
        self.PWM.start(self.allume)




    def marche_buzzer(self, etat):
        """
        mise en route du buzzer

        Args:
            self
            etat (int): la frequence est invariable
        """
        self.allume = etat
        pourcentage = 100 if etat else 0
        self.PWM.ChangeDutyCycle(pourcentage)
