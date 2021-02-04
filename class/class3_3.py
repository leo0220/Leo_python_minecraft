
from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0 :
        hit = hits[0]
        x,y,z = hit.pos.x , hit.pos.y , hit.pos.z
        mc.player.setPos(x,y,z)
     #0mc.setBlocks(x+1,y+1,z+1,x-1,y-1,z-1,46)
       # mc.setBlock(x,y+2,z,152)
        mc.createExplosion(x,y,z,50)
        
        