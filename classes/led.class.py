class Led :
    #marche #arret
    clignotement = 0
    def __init__(self, a_PWM):
        self.PWM = GPIO.PWM(a_PWM, 1) #GPIO clignotement #### pylint: disable=undefined-variable
        self.PWM.start(self.clignotement)

    def marche_led(pourcentage): ## Self ! 
        self.clignotement = pourcentage
        self.PWM.ChangeDutyCycle(self.clignotement)



    def inverse: ## !!! 
        if clignotement == 0:
            self.PWM.ChangeDutyCycle(self.PWM, 100)
        elif clignotement > 0:
            self.PWM.ChangeDutyCycle(self.PWM, 0)

        ## self.clignotement ?