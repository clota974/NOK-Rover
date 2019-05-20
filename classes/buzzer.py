# pylint: disable=import-error
import RPi.GPIO as GPIO

class Buzzer :
    #marche #arret
    
    def __init__(self, a_PWM):
        self.allume = False # Rapport cycliqué

        """
        Args:
            a_PWM (int): Adresse BCM du pin du Buzzer
        """
        GPIO.setup(a_PWM, GPIO.OUT) # Formalités ==> Définit les pins en tant que sortie
        self.PWM = GPIO.PWM(a_PWM, 2048) # Fréquence 2048 Hz donnée par le fabricant
        self.PWM.start(0) # Eteint




    def start(self, etat):
        """
        Mise en route du buzzer

        Args:
            etat (bool): Doit-on allumé le buzzer? True/False
        """

        self.allume = etat 
        pourcentage = 50 if etat else 0 # Rapport cyclique : 50 afin d'imiter une sinusoide 
        self.PWM.ChangeDutyCycle(pourcentage)

    def inverse(self):
        """
        Allume si éteint, éteint si allumé
        """
        
        self.start(not self.allume) 
