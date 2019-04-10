class Moteur :
    #marche #arret
    vitesse = 0
    def __init__(self, a_PWM) :
        self.PWM = GPIO.PWM(a_PWM, 1)
        self.PWM.start(self.vitesse)

    def marche_moteur(self,multiplicateur):
        self.vitesse = multiplicateur
    

    def inverse(self):
        self.vitesse = 0


