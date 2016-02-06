from mcpi.minecraft import Minecraft

mc = Minecraft.create()
nyr_stadur = mc.getBlock(5, 8, 9)
undir_nyjum_stad = mc.getBlock(5, 7, 9)

if nyr_stadur in [0, 1, 3]:
    print('Þessi blokk er úr lofti og steini eða grasi')

else:
    print('Þessi blokk er hvorki úr lofti né steini né grasi')
