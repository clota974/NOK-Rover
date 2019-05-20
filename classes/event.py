class Event:
    # Index des valeurs du bytearray reçu (HID)
    INDEX_DS4 = {
        "digital": {
            "CAR": 4,
            "CRO": 12,
            "RON": 20,
            "TRI": 28,
            "L1": 36,
            "R1": 44,
            "L2D": 52,
            "R2D": 60,
            "SHA": 68,
            "OPT": 76,
            "L3": 84,
            "R3": 92,
            "PS": 100,
            "TRA": 108
        },
        "analogue": {
            "R_X": 116,
            "R_Y": 124,
            "L_X": 132,
            "L2": 140,
            "R2": 148,
            "L_Y": 156
        },
        "autre": {
            "L_R": 188,
            "U_D": 196
        }
    }

    def __init__(self, raw):
        """
        Args:
            raw (bytearray): Données HID brutes reçues
        """
        self.raw = raw # Correspond au bytearray brut reçu

        self.spam = True # Voir spam dans le rapport
        if(raw[5] == 0):
            self.spam = False
            self.analyserDS4()
        else:
            print("SPAM") # Judicieux car cela permet de voir le ralentissement de la réaction de la voiture
            


    def analyserDS4(self):
        """
        Analyse et classe les données brutes reçues
        
        Args:
            None
        """

        raw = self.raw
        buffer = {} # Objet (temporaire) qui stocke la valeur des différentes touches de la manettes

        # Voir les différents types de données dans le rapport
        for key in self.INDEX_DS4["digital"]:
            index = self.INDEX_DS4["digital"][key]
            buffer[key] =  (raw[index]==1) # Stocker True ou False 

        for key in self.INDEX_DS4["analogue"]:
            index = self.INDEX_DS4["analogue"][key]
            
            # Les données analogues sont stockés dans deux octets en base 16
            try:
                byte1 = raw[index]
                byte2 = raw[index+1]
            except:
                print(raw[index])
                print(type(raw[index]))
            buffer[key] = Event.base16_vers_pourcent(byte1, byte2) # Base 16 vers pourcentage

        # Données des flèches
        buffer["LEFT"] = (raw[self.INDEX_DS4["autre"]["L_R"]] == 0x01) 
        buffer["RIGHT"] = (raw[self.INDEX_DS4["autre"]["L_R"]] == 0xFF)
        buffer["UP"] = (raw[self.INDEX_DS4["autre"]["U_D"]] == 0x01)
        buffer["DOWN"] = (raw[self.INDEX_DS4["autre"]["U_D"]] == 0xFF)

        self.data = buffer # Stocke le buffer (temporaire) dans la propriété `data` (permanent)

    def comparer(self, dernierEvt):
        """
        Compare deux objets Event

        Args:
            dernierEvt (Event): Objet Event précédemment reçu
        """
        self.changement = {} 

        # Voir les différents types de données dans le rapport
        for key in self.INDEX_DS4["digital"]:
            val = self.data[key]
            if(dernierEvt != False):
                self.changement[key] = (val is True) and (val != dernierEvt.data[key])
            else:
                self.changement[key] = val
        
        for key in self.INDEX_DS4["analogue"]:
            val = self.data[key]
            if(dernierEvt != False):
                self.changement[key] = (val != dernierEvt.data[key])
            else:
                self.changement[key] = True
        
        for key in ["UP", "DOWN", "LEFT", "RIGHT"]:
            val = self.data[key]
            if(dernierEvt != False):
                self.changement[key] = (val is True) and (val != dernierEvt.data[key])
            else:
                self.changement[key] = True

    @staticmethod
    def base16_vers_pourcent(bit1, bit2):
        """
        Transforme deux bits signe en base 16 en un pourcentage.

        Exemple : 01;80 --> 0x8001 = -32767 = -100

        Args:
            bit1 (int)
            bit2 (int)

        Returns:
            int: Le pourcentage
        """

        valeur = (bit2<<2*4)+bit1 # Arrange les bits selon l'ordre correct (Petit-boutiste --> Grand-boutiste)
        
        if valeur & 0x8000 > 0: # Si la valeur est négative
            valeur -= 0x10000

        max16 = 0x7FFF

        pourcentage = valeur/max16*100

        return int(pourcentage)