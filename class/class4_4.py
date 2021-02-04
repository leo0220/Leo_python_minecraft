from mcpi.minecraft import Minecraft as mcs
from time import sleep
mc = mcs.create()
while True:
    time.sleep(0.5)
    mc.executeCommand("time set 0")