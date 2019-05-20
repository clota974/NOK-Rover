# pylint: disable=import-error
import RPi.GPIO as GPIO

class Moteur :
    #marche 
    
    def __init__(self, a_IN1, a_IN2, a_PWM) :
        """
        Args:
            a_IN1 (int): Adresse BCM du 1er pin digital
            a_IN2 (int): Adresse BCM du 2ème pin digital
            a_PWM (int): Adresse BCM du pin PWM
        """

        self.vitesse = 0 # Rapport cyclique du moteur

        # Adresses des pin
        self.a_IN1 = a_IN1 # Adresse du 1er pin digital
        self.a_IN2 = a_IN2 # Adresse du 2ème pin digital
        self.a_PWM = a_PWM # Adresse du pin PWM

        # Formalités ==> Définit les pins en tant que sortie
        GPIO.setup(self.a_IN1, GPIO.OUT)
        GPIO.setup(self.a_IN2, GPIO.OUT)
        GPIO.setup(self.a_PWM, GPIO.OUT)

        self.PWM = GPIO.PWM(a_PWM, 980) # Fréquence 980 Hz qui se réfère aux pins PWM des Arduino UNO
        self.PWM.start(self.vitesse) # Eteint

    def start(self, vitesse):
        """
        Change la vitesse et le sens de rotation d'un moteur

        Args:
            vitesse (int): Rapport cyclique ==> Positif si avancer, négatif si reculer
        """
        self.vitesse = vitesse

        if(vitesse < 0): # Reculer
            GPIO.output(self.a_IN1, 0)
            GPIO.output(self.a_IN2, 1)
        elif(vitesse > 0): # Avancer
            GPIO.output(self.a_IN1, 1)
            GPIO.output(self.a_IN2, 0)
        else: # If vitesse==0
            # Freiner
            GPIO.output(self.a_IN1, 1)
            GPIO.output(self.a_IN2, 1)

        self.PWM.ChangeDutyCycle(abs(self.vitesse)) # Valeur absolue car self.vitesse correspond au rapport cyclique 


