# pylint: disable=import-error
import RPi.GPIO as GPIO
import subprocess

def launch_program(arg):
    ds4drv = subprocess.Popen(["sudo", "ds4drv", "--hidraw"])
    py = subprocess.Popen("python3", "~/NOK-Rover/main.py")
    py.wait()
    ds4drv.kill()


pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(pin, GPIO.RISING, callback=launch_program)

GPIO.setup(23, GPIO.OUT)
GPIO.PWM(23, 1).start(50)
