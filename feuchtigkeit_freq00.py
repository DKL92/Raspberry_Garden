#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#Define GPIO Pin to listen

GPIO_SENSOR_1 = 17

#Define direction of the GPIO Pin
GPIO.setup(GPIO_SENSOR_1, GPIO.IN)

#Samplerate
SAMPLE_RATE = 5000

#Refresh-rate in ms
REFRESH_RATE = 500.0

def frq_read():
        start = time.time()
        for impuls_count in range(SAMPLE_RATE):
            GPIO.wait_for_edge(GPIO_SENSOR_1, GPIO.FALLING)
        duration = time.time() - start      #seconds to run for loop
        frequency = SAMPLE_RATE / duration   #in Hz
        return frequency

if __name__ == '__main__':
    try:
        while True:
            freq = frq_read()
            print (" %.0f " % freq)
            time.sleep(REFRESH_RATE / 2000.0)

        #Reset on CTRL+C
    except KeyboardInterrupt:
        print("Interrupt by keyboard")
        GPIO.cleanup()
