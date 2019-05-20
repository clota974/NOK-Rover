# pylint: disable=no-name-in-module
# pylint: disable=import-error
import sys
from time import sleep
from classes.moteur import Moteur
from classes.buzzer import Buzzer
from classes.led import Led
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD


# Adresse de tous les pins 
adresses = {
    # Moteur A
    "PWMA": 27, 
    "AIN2": 18,
    "AIN1": 17,

    # Moteur B
    "BIN1": 15,
    "BIN2" : 14,
    "PWMB" : 4,

    # Avertisseurs
    "Buzzer" : 22,
    "Flash": 23, # LED
    
    # Boutons
    "Push button 1" : 24,
    "Push button 2" : 25,

    # Ecran LCD
    "V0" : 10,
    "RS" : 9,
    "Enable" : 11,
    "DB4" : 8,
    "DB5" : 7,
    "DB6" : 5,
    "DB7" : 6,
    "Red" : 12,
    "Green" : 13,
    "Blue" : 19   
}

GPIO.setmode(GPIO.BCM) # Notation BCM des adresses

class Voiture :
    led = Led(adresses["Flash"]) 
    moteurG = Moteur(adresses["AIN1"], adresses["AIN2"], adresses["PWMA"])
    moteurD = Moteur(adresses["BIN1"], adresses["BIN2"], adresses["PWMB"])
    buzzer = Buzzer(adresses["Buzzer"])
    gear = 1 # Multiplicateur de vitesse de 1 à 3

    def __init__(self):
        # Ecran vert

        self.led.start(100) # Allume la LED pour prévenir que la voiture est prête

        # Définir les pins en sortie
        outputs = [adresses["Red"], adresses["Green"], adresses["Blue"], adresses["V0"]]
        GPIO.setup(outputs, GPIO.OUT) 

        # Contraste de l'écran LCD
        self.pwm_contrast = GPIO.PWM(adresses["V0"], 980)
        self.contrast = 30
        self.pwm_contrast.start(30)

        self.lcd = LCD.Adafruit_RGBCharLCD(adresses["RS"], adresses["Enable"], adresses["DB4"], adresses["DB5"], adresses["DB6"], adresses["DB7"],
                           16, 2, adresses["Red"], adresses["Green"], adresses["Blue"])

    def interagir(self, evt):
        """
        Analyser et classer les données reçues par la manette

        Args:
            evt (Event): Dernier Event reçu 
        """

        # Valeurs brutes reçues de la manette
        data = evt.data
        
        #
        #### LED ####
        #
        if(evt.changement["CAR"]): # Si Carré enfoncé alors alterner l'état de la LED
            self.led.inverse()
        
        if(evt.data["OPT"]): # Si Options enfoncé alors allumer la LED
            self.led.start(100)
        
        #
        #### BUZZER ####
        #
        self.buzzer.start( data["CRO"] ) # Si Croix enfoncé alors klaxonner

        #
        #### MOTEUR ####
        #
        vitesse = 0 # Vitesse par défaut
        lacet = evt.data["L_X"] # Lacet <==> Orientation latérale / Correspond à l'axe Joystick Gauche
        
        # -100 <= evt.data["R2"] <= 100
        if(evt.data["R2D"]): # Filtrer ==> Soit devant soit derrière, mais pas les deux. Par défaut : Devant
            vitesse = int((evt.data["R2"] + 100)/2)
        elif(evt.data["L2D"]):
            vitesse = -int((evt.data["L2"] + 100)/2)
        
        vitesse = vitesse/3 * self.gear # Utilisation du multiplicateur de vitesse (Gear)
        self.bouger(vitesse, lacet)

        
        #
        #### GEAR ####
        #
        if(evt.changement["DOWN"]): # Si Flèche du bas enfoncé alors décrémenter le Gear
            self.gear -= 1 if self.gear>1 else 0
        elif(evt.changement["UP"]): # Si Flèche du haut enfoncé alors incrémenter le Gear
            self.gear += 1 if self.gear<3 else 0
        
        #
        #### CONTRASTE ####
        #
        if(evt.changement["LEFT"]): # Si Flèche gauche enfoncé alors décrémenter la valeur V0 (contraste) de 5 (écran plus foncé)
            self.contrast += 5 if self.contrast<95 else 0
        elif(evt.changement["RIGHT"]): # Si Flèche gauche enfoncé alors incrémenter la valeur V0 (contraste) de 5 (écran plus clair)
            self.contrast -= 5 if self.contrast>5 else 0
        self.pwm_contrast.ChangeDutyCycle(self.contrast)

        #
        #### LCD BACKLIGHT ####
        #
        # Colore l'écran LCD selon le Gear
        if self.gear == 1:
            self.RGB(0,1,0) # Vert
        elif self.gear == 2:
            self.RGB(0,0,1) # Bleu
        elif self.gear == 3:
            self.RGB(1,0,0) # Rouge
        else:
            self.RGB(0,0,0)
        
        # Les données importantes ont été traitées, alors afficher les informations sur l'écran
        self.updateEcran()  

        #
        #### EXCTINCTION ####
        #
        if(evt.data["SHA"]): # Si Share enfoncée alors éteindre la voiture (5 secs)
            self.led.start(70) # Clignotement rapide
            print("ARRET DEMANDE : FIN DU PROGRAMME")

            self.RGB(1,0,0) # Rouge
            self.lcd.clear()
            self.lcd.message("Extinction dans\n5 secs")
            sleep(1)
           
            self.RGB(0,0,1) # Bleu
            self.lcd.clear()
            self.lcd.message("Extinction dans\n4 secs")
            sleep(1)
            
            self.RGB(1,0,0) # Rouge
            self.lcd.clear()
            self.lcd.message("Extinction dans\n3 secs")
            sleep(1)
            
            self.RGB(0,0,1) # Bleu
            self.lcd.clear()
            self.lcd.message("Extinction dans\n2 secs")
            sleep(1)
            
            self.RGB(1,0,0)
            self.lcd.clear()
            self.lcd.message("Extinction dans\n1 sec")
            sleep(1)

            GPIO.cleanup() # Eteindre les pins utilisés
            sys.exit(0) # Terminer le programme avec succès (code 0)

    def bouger(self, vitesse, lacet):
        """
            vitesse (int): Vitesse avant/arrière
            lacet (int): déplacement droite/gauche
        """

        default = 5 if vitesse>0 else -5 #  5 ou -5 plutôt que 0 pour ne pas bloquer les roues 
        if(lacet != 0): # Tourner à droite
            vD = (50+lacet/2)/100*vitesse or default # Moteur droit (voir formule sur le rapport)
            vG = (50-lacet/2)/100*vitesse or default # Moteur gauche
        else:
            vD = vG = vitesse

        print(vD,vG) # Afficher le rapport cyclique des moteurs sur le terminal
        self.vD = format(int(vD), "03") # Ecrit le nombre avec 3 chiffres (zéros initiaux)
        self.vG = format(int(vG), "03")
        self.moteurG.start(vG) # Changer la vitesse
        self.moteurD.start(vD)
    
    def RGB(self, R,G,B):  
        """
        Changer la couleur de l'écran LCD

        Args:
            R (int): Couleur rouge (1 ou 0)
            G (int): Couleur vert (1 ou 0)
            B (int): Couleur bleu (1 ou 0)
        """
        
        GPIO.output(adresses["Red"], R)
        GPIO.output(adresses["Green"], G)
        GPIO.output(adresses["Blue"], B)
    
    def updateEcran(self):
        """
        Afficher les valeurs sur l'écran LCD

        Args:
            None
        """
        self.lcd.clear() # Nettoie les caractères de l'écran LCD
        
        led_etat = 1 if self.led.clignotement > 0 else 0 # La led est-elle allumée? 0:Non / 1:Oui 

        texte = ('V%s L%s C%s\nD%s G%s' % (self.gear, led_etat, format(self.contrast, "02"), self.vD, self.vG)) # Voir l'exemple sur Rapport
        self.lcd.message(texte) # Affiche les informations
        
    



