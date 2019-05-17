# pylint: disable=no-name-in-module
# pylint: disable=import-error
from classes.moteur import Moteur
from classes.buzzer import Buzzer
from classes.led import Led
import RPi.GPIO as GPIO

adresses = {
    "PWMA": 27,
    "AIN2": 18,
    "AIN1": 17,
    "BIN1": 15,
    "BIN2" : 14,
    "PWMB" : 4,
    "Buzzer" : 22,
    "Flash": 23,
    "Push button 1" : 24,
    "V0" : 10,
    "RS" : 9,
    "Push button 2" : 25,
    "Enable" : 11,
    "DB4" : 8,
    "DB5" : 7,
    "DB6" : 5,
    "DB7" : 6,
    "Red +" : 12,
    "Green +" : 13,
    "Blue +" : 19   
}

GPIO.setmode(GPIO.BCM)

class Voiture :
    led = Led(adresses["Flash"])
    moteurG = Moteur(adresses["AIN1"], adresses["AIN2"], adresses["PWMA"])
    moteurD = Moteur(adresses["BIN1"], adresses["BIN2"], adresses["PWMB"])
    buzzer = Buzzer(adresses["Buzzer"])
    gear = 1 # 1 à 3

    def __init__(self):
        # Ecran vert

        self.led.start(100)

    def bouger(self, vitesse, lacet):
        """
            vitesse_av: Vitesse avant/arrière
            lacet: déplacement droite/gauche
        """

        self.moteurG.start(vitesse)
        self.moteurD.start(vitesse)

    def interagir(self, evt):
        data = evt.data
        
        #LED
        if(evt.changement["CAR"]):
            self.led.inverse()
        
        if(evt.data["OPT"]):
            self.led.start(100)
        
        #BUZZER
        self.buzzer.start( data["CRO"] )

        ## MOTEUR
        vitesse = 0
        # -100 <= evt.data["R2"] <= 100
        if(evt.data["R2D"]): # Filtrer ==> Soit devant soit derrière, mais pas les deux. Par déf : Devant
            vitesse = int((evt.data["R2"] + 100)/2)
        elif(evt.data["L2D"]):
            vitesse = -int((evt.data["R2"] + 100)/2)

        self.bouger(vitesse, 0)


