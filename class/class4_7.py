from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
ID = mc.getPlayerEntityId("DrummerLeo")
mc.postToTitle(ID,"hello")