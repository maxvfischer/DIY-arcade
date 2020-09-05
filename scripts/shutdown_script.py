import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

old_button_state = True

while True:
    button_state = GPIO.input(5)

    if button_state != old_button_state and button_state == False:
        subprocess.call("shutdown -h now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        old_state_button = button_state

        time.sleep(1)
