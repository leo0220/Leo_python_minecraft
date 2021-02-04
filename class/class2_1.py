from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
h = 10
w = 10
mc.setBlocks(x+1,y+1,z+1,x
mc.setBlocks(x,y,z,x+w,y+h,z+w,1)+w-1,y+h-1,z+w-1,0)