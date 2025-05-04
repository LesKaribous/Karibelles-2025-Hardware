#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_4 
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from time import sleep  

# Sound controler
sound = Sound()

# Touch sensor
tirette = TouchSensor(INPUT_4)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# Main code

while True:

    # Wait tirette inserted
    while not tirette.is_pressed:
        sleep(1)

    sound.beep()

    # Wait tirette released
    while tirette.is_pressed:
        sleep(1)

    sound.beep()

    # THE MATCH BEGIN !
    
    # drive in a turn for x rotations of the outer motor
    # the first two parameters can be unit classes or percentages.
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), 1)

    # drive in a different turn for y seconds
    tank_drive.on_for_seconds(SpeedPercent(-20), SpeedPercent(-20), 1)
