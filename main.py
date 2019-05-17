# pylint: disable=import-error
# pylint: disable=no-name-in-module
import os, sys, datetime, colored, json
from time import sleep
from io import FileIO
from classes.event import Event
from classes.voiture import Voiture

DEBUG = True

def logEvData(data):
    dat = json.dumps(data).replace('"',"")
    dat = json.dumps(data).replace('{',"")
    dat = json.dumps(data).replace('}',"")
    dat = json.dumps(data).replace(',',"")
    print("\r"+dat, end="")
    print()
    print()
    print()

report_fd = os.open("/dev/input/js1", os.O_RDWR | os.O_NONBLOCK)
fd = FileIO(report_fd, "rb+", closefd=False)
defBuf = bytearray(230)

voiture = Voiture()

dernierEvt = False

while True:
    sleep(0.1)

    buf = defBuf 
    r = fd.readinto(buf)
    key = []
    arr = []
    sign = buf[2]

    i = 0
    while i < len(buf):
        try:
            if(buf[i]==sign and buf[i+1]==0):
                key.append(i+2) 
                key.append(i+3) 
        except Exception as e:
            pass

        i+=1
    
    i = 0
    while i < len(buf):
        val = format(buf[i], "02x")
        arr.append(val)
        
        i+=1


    # p = ' '.join(arr)
    # p = p.replace("\r", "")
    # print("\r"+p, end="") 
    # print()
    # print()

    evt = Event(buf)
    if evt.spam:
        continue # Ne pas faire attention au spam
    
    evt.comparer(dernierEvt)

    if(DEBUG):
        logEvData(evt.changement)


    voiture.interagir(evt)

    dernierEvt = evt
    sys.stdout.flush()