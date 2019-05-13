sample = "66 4b 08 00 00 00 81 00 66 4b 08 00 00 00 81 01 66 4b 08 00 00 00 81 02 66 4b 08 00 00 00 81 03 66 4b 08 00 00 00 81 04 66 4b 08 00 00 00 81 05 66 4b 08 00 00 00 81 06 66 4b 08 00 00 00 81 07 66 4b 08 00 00 00 81 08 66 4b 08 00 00 00 81 09 66 4b 08 00 00 00 81 0a 66 4b 08 00 00 00 81 0b 66 4b 08 00 00 00 81 0c 66 4b 08 00 00 00 81 0d 66 4b 08 00 00 00 82 00 66 4b 08 00 00 00 82 01 66 4b 08 00 b7 fc 82 02 66 4b 08 00 01 80 82 03 66 4b 08 00 01 80 82 04 66 4b 08 00 00 00 82 05 66 4b 08 00 30 fc 82 06 66 4b 08 00 aa 0d 82 07 66 4b 08 00 8e 3f 82 08 66 4b 08 00 00 00 82 09 66 4b 08 00 00 00 82 0a 66 4b 08 00 00 00 82 0b 66 4b 08 00 00 00 82 0c 66 4b 08 00 00 00 82 0d 00 00 00 00 00 00"
sample = sample.split(" ")

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

    def __init__(self, raw):
        self.raw = raw

        self.analyserDS4(self.raw)


    def analyserDS4(self, raw):
        buffer = {} # Stocker dans un buffer pour ne pas modifier le raw
        
        for key in self.INDEX_DS4["digital"]:
            index = list(self.INDEX_DS4["digital"].keys()).index(key)
            buffer[key] = True if raw[index]==1 else False # Stocker True ou False 

        for key in self.INDEX_DS4["analogue"]:
            index = list(self.INDEX_DS4["analogue"].keys()).index(key)
            bit1 = int(raw[index], 16)
            bit2 = int(raw[index+1], 16)
            buffer[key] = Event.base16_vers_pourcent(bit1, bit2) # Base 16 vers pourcentage

        print(buffer)

        buffer["LEFT"] = (raw[self.INDEX_DS4["autre"]["LEFT_RIGHT"]] == 0x01)
        buffer["RIGHT"] = (raw[self.INDEX_DS4["autre"]["LEFT_RIGHT"]] == 0xFF)
        buffer["UP"] = (raw[self.INDEX_DS4["autre"]["LEFT_RIGHT"]] == 0x01)
        buffer["DOWN"] = (raw[self.INDEX_DS4["autre"]["LEFT_RIGHT"]] == 0xFF)

        self.data = buffer

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


ev = Event(sample)
print(ev.data)