from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
mc.setblock(x+1,y,z,46)
mc.setblock(x-1,y,z,46)  
mc.setblock(x,y,z+1,46)
mc.setblock(x,y,z-1,46)
mc.setblock(x-1,y,z+1,46)
mc.setblock(x-1,y,z-1,46)
mc.setblock(x+1,y,z-1,46)
mc.setblock(x-1,y,z+1,46)