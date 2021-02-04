from mcpi.minecraft import Minecraft as mcs
import random
mc = mcs.create()
Blen = 4
for j in range(4):
    for i in range(4):
        num = random.randint(1,4)
        if num == 1:
            mc.setBlocks(x,y,z,x+Blen,y,z,1)
            x = x + Blen
        elif num == 2:
            mc.setBlocks(x,y,z,x-Blen,y,z,1)
            x = x - Blen
        elif num == 3:
            mc.setBlocks(x,y,z,x,y,z+Blen,1)
            z = z + Blen
        elif num == 4:
            mc.setBlocks(x,y,z,x,y,z-Blen,1)
            z = z - Blen
        elif num == 5:
            mc.setBlocks(x,y,z,x,y+Blen,z,1)
            y = y + Blen 
        else :
            mc.setBlocks(x,y,z,x,y-Blen,z,1)
            y = y - Blen