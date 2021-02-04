from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,68,0,"I love minecraft and python")