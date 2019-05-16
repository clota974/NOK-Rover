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
        self.PWM = GPIO.PWM(a_PWM, 1024)
        self.PWM.start(self.allume)




    def marche_buzzer(self, etat):
        """
        Mise en route du buzzer

        Args:
            self
            etat (bool): la frequence est invariable
        """
        self.allume = etat
        pourcentage = 100 if etat else 0
        self.PWM.ChangeDutyCycle(pourcentage)
