from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

while True:

    hogg = len(mc.events.pollBlockHits())

    if hogg > 0:
        print('Þú slóst %d sinni í blokk' % hogg)
        mc.events.clearAll()

    sleep(0.5)
hello
