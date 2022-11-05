from Constants import G, gridArea, gridScale
import matplotlib.pyplot as plt
import math
import numpy as np 

class Exoplanet:

    def __init__(self, mass1, mass2):
        #all shared variables
        self.initial_distance = 149597870000 #distance from the Sun in metres/gridscale which remains constant with a circular orbit         
        #all star variables
        self.starMass = mass2 #mass of star in kg
        self.starRadius = 696340000 / gridScale
        self.starPosition = [gridArea[1]/2, gridArea[3]/2]
        #all planet variables
        self.planetMass = mass1 #mass of planet in kg  should be --> 5.972e24
        self.planetPosition = [gridArea[1]/2 + (self.initial_distance / gridScale), gridArea[3]/2] #initial planet position = (x,y) (same y coordinate as the sun)
        self.planetRadius = 6371000000/gridScale
        #all initial velocity varioables
        self.x_velocity = 0
        self.y_velocity = self.calculateInitialVelocity(self.initial_distance, self.starMass, self.planetMass, self.starPosition, self.planetPosition)

    def calculateInitialVelocity(self, distance, starMass, planetMass, starPosition, planetPosition): #calculate the initial velocity of the planet to maintain a circular orbit (in theory this should remain constant)
        CoM_x = (1/(starMass + planetMass))*(planetMass*planetPosition[0] + starMass*starPosition[0])
        CoM_y = (1/(starMass + planetMass))*(planetMass*planetPosition[1] + starMass*starPosition[1])
        r_p = math.sqrt((CoM_x - planetPosition[0])**2 + (CoM_y - planetPosition[1])**2)
        initialVelocity = math.sqrt(G*starMass*r_p*gridScale/(distance**2))
        return initialVelocity

    def calculateGravitationalForce(self, planetMass, starMass, distance): #calculating the force that the planet experiences due to the presence of the star 
        gravitationalForce = G * planetMass * starMass / distance**2
        return gravitationalForce

    def orbitingPlanet(self, starPosition): #for trail purposes, the planet created will have properties that of Earth
        
        delta_t = 50000 #time between each timestep in seconds

        distance = math.sqrt(((self.planetPosition[0]-starPosition[0]) * gridScale)**2 + ((self.planetPosition[1] - starPosition[1]) * gridScale)**2) #distance = sqrt(delta x**2 + delta y**2)
        gravitationalForce = self.calculateGravitationalForce(self.planetMass, self.starMass, distance)
        acceleration = gravitationalForce / self.planetMass

        #determine the angle from the horizontal plane 
        cos_angle = ((self.planetPosition[0] - starPosition[0]) * gridScale) / distance #cos_theta = x_1 / distance
        sin_angle = ((self.planetPosition[1] - starPosition[1]) * gridScale) / distance #sin_theta = y_1 / distance

        #calculate the x and y component of the acceleration
        x_acceleration = acceleration * cos_angle
        y_acceleration = acceleration * sin_angle

        #determine the change in velocity in the x and y direction
        self.x_velocity = self.x_velocity - x_acceleration * delta_t #v = u + a*delta_t
        self.y_velocity = self.y_velocity - y_acceleration * delta_t #v = u + a*delta_t

        #find the new position of the Earth and update the value
        self.planetPosition[0] = self.planetPosition[0] + (self.x_velocity * delta_t) / gridScale # x_2 = x_1 + v_x * delta_t
        self.planetPosition[1] = self.planetPosition[1] + (self.y_velocity * delta_t) / gridScale # y_2 = y_1 + v_y * delta_t

        return (self.planetPosition[0], self.planetPosition[1])