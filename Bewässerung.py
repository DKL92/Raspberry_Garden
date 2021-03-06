#!/usr/bin/python3
import RPi.GPIO as GPIO
from feuchtigkeit_freq00 import frq_read # Signal vom Feuchtigkeitssensor 
import time
import lcddriver # für LCD Display


freq = frq_read()

lcd = lcddriver.lcd()
lcd.lcd_clear()

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
        
GPIO.setwarnings(False)
 
RELAIS_1_GPIO = 19 # Relais für Pumpe

if freq >= 6000:
    lcd.lcd_display_string('frisch gegossen', 1)
    lcd.lcd_display_string("Time: %s" %time.strftime("%H:%M"), 2)
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT, initial=GPIO.LOW)
    time.sleep(60.0)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)

elif freq <= 5999:
    lcd.lcd_display_string('Alles OK', 1)
    lcd.lcd_display_string("Time: %s" %time.strftime("%H:%M"), 2)
    

if __name__ == '__main__':
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
    
        # execute functions


    except KeyboardInterrupt:
        print("Interrupt by keyboard")
        GPIO.cleanup()
