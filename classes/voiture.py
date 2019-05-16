from moteur import Moteur
from buzzer import Buzzer
from led import Led

adresses = {
    "PWMA": 27,
    "AIN2": 18,
    "AIN1": 17,
    "BIN1": 15,
    "BIN2" : 14,
    "PWMB" : 4,
    "Buzzer +" : 22,
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

class Voiture :
    led = Led(adresses.Flash)
    moteurG = Moteur(adresses.AIN1, adresses.AIN2, adresses.PWMA)
    moteurD = Moteur(adresses.BIN1, adresses.BIN2, adresses.PWMB)
    buzzer = Buzzer(adresses.buzzer)

    def __init__(self):
        # Ecran vert

        self.led.marche_led(100)

   
