# pylint: disable=import-error

import RPi.GPIO as GPIO

class Led :
    #marche #arret
    
    def __init__(self, a_PWM):
        """
        Args:
            a_PWM (int): Adresse BCM du pin de la LED
        """
        
        self.clignotement = 0 # Rapport cyclique de la LED
        
        GPIO.setup(a_PWM, GPIO.OUT)
        self.PWM = GPIO.PWM(a_PWM, 1) # Fréquence de 1 Hz afin de créer un clignotement visible
        self.PWM.start(self.clignotement)

    def start(self, pourcentage):  
        """
        Changer la fréquence de de clignotemenet

        Args:
            pourcentage (int): Nouveau rapport cyclique
        """
        self.clignotement = pourcentage
        self.PWM.ChangeDutyCycle(self.clignotement)



    def inverse(self): ## !!!
        """
        Allume la LED si éteinte (Rapport cyclique : 100) et l'éteint si allumée
        """

        if self.clignotement == 0: # Si éteinte
            self.clignotement = 100 # Affectation du nouveau rapport cyclique ==> Allumé
        elif self.clignotement > 0: # Si allumée
            self.clignotement = 0
        
        self.PWM.ChangeDutyCycle(self.clignotement)
        