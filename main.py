import sys

import getPos
import renderBodies
import fileHandler

import sim.solarSystem
import sim.earthMoonSystem
import sim.plutoCharonSystem

CYCLES = 1024
BODIES = sim.solarSystem.bodies

VID_ID = sim.solarSystem.video_name

load = True
file = sys.argv

if __name__ == '__main__':
    if load != True:
        getPos.getPos(BODIES, CYCLES)
    else:
        fileHandler.fileLoad()


