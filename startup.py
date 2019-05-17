# pylint: disable=import-error
import RPi.GPIO as GPIO
import subprocess, sys, time, os

try:
    while True:
        def launch_program(arg):
            print("Starting NOK-Rover")
            ds4drv = subprocess.Popen(["sudo", "ds4drv", "--hidraw"], shell=False)
            time.sleep(1)
            py = subprocess.Popen(["python3", "/home/pi/NOK-Rover/main.py"])
            py.wait()
            ds4drv.kill()


        pin = 24

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(pin, GPIO.RISING, callback=launch_program)

        GPIO.setup(23, GPIO.OUT)
        pwm = GPIO.PWM(23, 1)
        pwm.start(50)

        time.sleep(0.1)

except Exception as e:
    print(e)

os.startfile("/home/pi/NOK-Rover/startup.py")

