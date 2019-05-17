# pylint: disable=no-name-in-module
# pylint: disable=import-error
import sys
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
    "Red" : 12,
    "Green" : 13,
    "Blue" : 19   
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

        LED = [adresses["Red"], adresses["Green"], adresses["Blue"]]
        GPIO.setup(LED, GPIO.OUT)

    def interagir(self, evt):
        data = evt.data
        
        #
        #### LED ####
        #
        if(evt.changement["CAR"]):
            self.led.inverse()
        
        if(evt.data["OPT"]):
            self.led.start(100)
        
        #
        #### BUZZER ####
        #
        self.buzzer.start( data["CRO"] )

        #
        #### MOTEUR ####
        #
        vitesse = 0
        lacet = evt.data["L_X"]
        # -100 <= evt.data["R2"] <= 100
        if(evt.data["R2D"]): # Filtrer ==> Soit devant soit derrière, mais pas les deux. Par déf : Devant
            vitesse = int((evt.data["R2"] + 100)/2)
        elif(evt.data["L2D"]):
            vitesse = -int((evt.data["L2"] + 100)/2)
        
        vitesse = vitesse/3 * self.gear
        self.bouger(vitesse, lacet)

        
        #
        #### GEAR ####
        #
        if(evt.changement["DOWN"]):
            self.gear -= 1 if self.gear>1 else 0
        elif(evt.changement["UP"]):
            self.gear += 1 if self.gear<3 else 0

        #
        #### LCD BACKLIGHT ####
        #
        if self.gear == 1:
            self.RGB(0,1,0) # Vert
        elif self.gear == 2:
            self.RGB(0,0,1) # Bleu
        elif self.gear == 3:
            self.RGB(1,0,0) # Rouge
        else:
            self.RGB(0,0,0)
        
        #
        #### EXCTINCTION ####
        #
        if(evt.data["SHA"]):
            self.RGB(1,1,1)
            self.led.start(70)
            sleep(2)
            GPIO.cleanup()
            sys.exit(0)

    def bouger(self, vitesse, lacet):
        """
            vitesse_av: Vitesse avant/arrière
            lacet: déplacement droite/gauche
        """

        if(lacet != 0): # Tourner à droite
            vD = (50+lacet/2)/100*vitesse or 5
            vG = (50-lacet/2)/100*vitesse or 5
        else:
            vD = vG = vitesse

        print(vD,vG)
        self.moteurG.start(vG)
        self.moteurD.start(vD)
    
    def RGB(self, R,G,B):  
        GPIO.output(adresses["Red"], R)
        GPIO.output(adresses["Green"], G)
        GPIO.output(adresses["Blue"], B)
    



