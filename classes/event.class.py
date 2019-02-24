
class Event:

    INDEX_DS4 = {
        "carre": 4,
        "croix": 12,
        "rond": 20,
        "triangle": 28,
        "L1": 36,
        "R1": 44,
        "L2_digital": 52,
        "R2_digital": 60,
        "share": 68,
        "options": 76,
        "L3": 84,
        "R3": 92,
        "PS": 100,
        "trackpad": 108,
        "L_X": 116,
        "L_Y": 124,
        "R_X": 132,
        "R_Y": 140

    }

    def __init__(self, data):
        self.data = data


    def analiserDS4(self):
        buffer = self.data


