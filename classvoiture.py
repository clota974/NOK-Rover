class Voiture :
    adresses = {
        "PWMA": 27,
        "AIN2": 18,
        "AIN1": 17,
        "BIN1": 15,
        "BIN2" : 14,
        "PWMB" : 4,
        "Buzzer +" : 22,
        "Flash (GND)": 23,
        "Push button 1 (GND)" : 24,
        "V0" : 10,
        "RS" : 9,
        "Push button 2 (GND)" : 25,
        "Enable" : 11,
        "DB4" : 8,
        "DB5" : 7,
        "DB6" : 5,
        "DB7" : 6,
        "Red +" : 12,
        "Green +" : 13,
        "Blue +" : 19   
    }

led = led (adresses.led)
moteur1 = Moteur(adresses.AIN1, adresses.AIN2, adresses.PWMA)
moteur2 = moteur1
buzzer = buzzer(adresses.buzzer)
LCD = LCD(adresses.lcd)

def bouger(self, vitesse_x, vitesse_y):
    """
    en avant : allumer les 2 moteurs dans le bon sens
    regler la vitesse (1,2 ou 3)

    en arriere : allumer les 2 moteur dans le sens inverse
    regler la vitesse (1,2 ou 3)

    a droite en avançant : allumer les 2 moteurs dans le
    bon sens et orienter les roues vers la droite + regler
    la vitesse

    a gauche en avançant : allumer les 2 moteurs dans le 
    bon sens et orienter les roues vers la gauche + regler
    la vitesse

    a droite en reculant : allumer les 2 moteurs dans le
    sens inverse et oriente les roues vers la droite + regler
    la vitesse

    a gauche en reculant : allumer les 2 moteurs dans le
    sens inverse et orienter les roues vers la gauche + regler
    la vitesse

    freiner : eteindre les moteurs
    """
def klaxonner(self, frequence):
    """
    klaxonner([])
    """
def Ecran(self, affichage)
    """
    nous afficherons la vitesse (1,2 ou 3)
    1 = bleu
    2 = vert
    3 = rouge
    """


    import classmoteur.py
    import ledclass.py
    import classLCD.py
    import buzzerclass.py