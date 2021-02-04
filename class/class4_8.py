from mcpi.minecraft import Minecraft as mcs
from time import sleep
import random
mc = mcs.create()
ID = mc.getPlayerEntityId("DrummerLeo")
while True:
    sleep(1)
    x,y,z = mc.entity.getTilePos(ID)
    mineral=[14,15,16,56,73,129]
    style = random.choice(mineral)
    mc.setBlocks(x+1,y+3,z+1,x-1,y-2,z-1,style)