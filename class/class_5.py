from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
while True: 
    x,y,z = mc.player.getTilePos()
    mc.postToChat('You are located on X:'+str(x)+\
                 "Y:"+str(y)+"Z:"+str(z))

    
  