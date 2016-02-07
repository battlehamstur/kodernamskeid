from mcpi.minecraft import Minecraft

mc = Minecraft.create()
nyr_stadur = mc.getBlock(80, 20, 40)

if nyr_stadur == 1:
    mc.player.setPos(80, 20, 40)

else:
    print('Þessi blokk er úr hörðu efni og þú munt festast')
