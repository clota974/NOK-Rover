# pylint: disable=import-error
# pylint: disable=no-name-in-module
import os, sys, datetime, colored, json
from time import sleep
from io import FileIO
from classes.event import Event
from classes.voiture import Voiture

DEBUG = True # Affiche les données sur le terminal

def logEvData(data):
    """
    Formate les propriétés Event en un format plus lisible. 
    Il transforme les données en JSON et le modifie légèrement.

    Args:
        data (dict): Données à formater
    """
    jsonData = json.dumps(data)
    dat = jsonData.replace('"',"") .replace('{',"") .replace('}',"") .replace(',',"")
    print("\r"+dat, end="") # \r permet de réécrire sur la dernière ligne (si la taille du terminal le permet)
    print()
    print()
    print()

report_fd = os.open("/dev/input/js1", os.O_RDWR | os.O_NONBLOCK) # Ouvre le fichier contenant les données HID en mode R/W de manière asynchrone
fd = FileIO(report_fd, "rb", closefd=False) # Ouvre un FLUX de lecture du fichier concerné. Mode lecture binaire
defBuf = bytearray(230) # Crée un bytearray de 230 octets vides

voiture = Voiture() # Initialise la classe voiture

dernierEvt = False # Dernier Event reçu (False si c'est le permier)

while True:
    sleep(0.1)

    buf = defBuf # Buf = Buffer = Bytearray
    r = fd.readinto(buf) # Remplit le bytearray vide

    evt = Event(buf) # Crée un événement depuis le bytearray
    if evt.spam:
        evt = dernierEvt # Si c'est un spam, alors garder 

    evt.comparer(dernierEvt) # Compare Event et dernierEvt

    if(DEBUG):
        logEvData(evt.changement) # Affiche des données formatées


    voiture.interagir(evt) # Envoie les données à l'objet Voiture pour interagir avec les GPIO

    dernierEvt = evt
    sys.stdout.flush() # Affiche les données sauvegardé dans un buffer et le vide