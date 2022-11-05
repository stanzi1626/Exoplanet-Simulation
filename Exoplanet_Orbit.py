#2D simulation of the orbit of the Earth around the Sun using simple Newtonion Gravitational Mechanics
from Constants import gridScale
from Exoplanet_Class import Exoplanet
from Star_Class import Star
from Detector_Class import Detector
import matplotlib.pyplot as plt
import math
import numpy as np 
from matplotlib import animation
from matplotlib.lines import Line2D

fig, (ax1, ax2) = plt.subplots(2)

ax1.set_xlim([0, 1000])
ax1.set_ylim([0, 1000])

ax2.set_xlim([0,1000])
ax2.set_ylim([0,600])

plt.grid(b="on")  # place grid

######################################################################################################################

exoplanet_mass = float(input('What is the mass of the exoplanet in sun masses: ')) * 1.989e30
star_mass = float(input('What is the mass of the Star in sun masses: ')) * 1.989e30

exoplanet = Exoplanet(exoplanet_mass, star_mass)
star = Star(exoplanet_mass, star_mass)
detector = Detector(100, 400, 100, 600)

patch1 = plt.Circle((0, 0), radius=(6371000000/gridScale), fill=True, color='green')
patch2 = plt.Circle((0, 0), radius=(6955000000/gridScale), fill=True, color='red')

walls = []
circles = []

walls.append(detector)
circles.append(exoplanet)

place_detector = detector.placeDetector()

ax1.add_line(place_detector)

xdata = []
ydata = []
ln, = ax2.plot([], [], 'ro', markersize=2)

######################################################################################################################

def init():
    patch1.center = (0, 0)
    patch2.center = (0, 0)
    ax1.add_patch(patch1)
    ax1.add_patch(patch2)
    
    return patch1, patch2, ln,

def animate(i):
    a, b = patch1.center
    x, y = patch2.center
    global exoplanet
    global star
    (a, b) = exoplanet.orbitingPlanet(star.starPosition)
    (x, y) = star.orbitingStar(exoplanet.planetPosition)
    detection_number = star.look(walls, circles)
    patch1.center = (a, b)
    patch2.center = (x, y)

    xdata.append(i)
    ydata.append(detection_number)
    ln.set_data(xdata, ydata)

    return patch1, patch2, ln
    
    

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=4000, interval=1, blit=True)

######################################################################################################################

plt.show(block = True)