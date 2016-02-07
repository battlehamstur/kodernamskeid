from mcpi.minecraft import Minecraft
import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
import time
from time import sleep

mc = Minecraft.create()
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

TORCH = 50
FIRE  = 51
LAVA_FLOWING = 10
    
while True:
    player_pos = mc.player.getTilePos()
    sleep(0.2)
    if mc.player.getTilePos() is not player_pos:
        mc.setBlock(player_pos, TORCH)
        print("LED is on")
    
    GPIO.output(21, GPIO.HIGH)
    time.sleep(0.5)
    print("LED is off")
    GPIO.output(21, GPIO.LOW)



