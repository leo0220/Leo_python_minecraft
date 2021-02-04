from mcpi.minecraft import Minecraft as mcs
from random import randint
mc = mcs.create()
x,y,z = mc.player.getTilePos()
com = randint(0,15)
for i in range(16):
    for j in range(16):
        color = randint(0,15)
        mc.setBlock(x+i,y-1,z+j,35,color)
        
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if com == data:
            mc.postToChat("you are win")
            break
        elif com > data :
            mc.postToChat("this is big number")
        else:
            mc.postToChat("this is small number")
