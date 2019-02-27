
class Event:

    INDEX_DS4 = {
        "digital": {
            "CARRE": 4,
            "CROIX": 12,
            "ROND": 20,
            "TRIANGLE": 28,
            "L1": 36,
            "R1": 44,
            "L2_DIGITAL": 52,
            "R2_DIGITAL": 60,
            "SHARE": 68,
            "OPTIONS": 76,
            "L3": 84,
            "R3": 92,
            "PS": 100,
            "TRACKPAD": 108
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
            "LEFT_RIGHT": 188,
            "UP_DOWN": 188
        }
    }

    historique = {
        "DS4": {}
    }

    def __init__(self, source, data):
        self.source = source # "DS4"
        self.data = data

        if(self.source == "DS4"):
            self.analiserDS4(self.data)


    def analiserDS4(self, data):
        buffer = data # Stocker dans un buffer pour ne pas modifier le data
        
        buffer

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

        valeur = (bit2<<2*4)+bit1 # Arrange les bits selon l'ordre correct (Little-endian --> Big-endian)
        
        if valeur & 0x8000 > 0: # Si la valeur est négative
            valeur -= 0x10000

        max16 = 0x7FFF

        pourcentage = valeur/max16*100

        return pourcentage


