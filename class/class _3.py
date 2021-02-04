from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
while True:
    time.sleep(20)
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,46)
    mc.setBlock(x+1,y,z,152)