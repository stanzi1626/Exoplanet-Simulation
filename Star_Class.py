from Constants import G, gridArea, gridScale

from Ray import Ray
import math
import matplotlib.pyplot as plt

class Star:

    def __init__(self, mass1, mass2):
        #all shared variables
        self.initial_distance = 149597870000 #distance from the Sun in metres/gridscale which remains constant with a circular orbit          
        #all star variables
        self.starMass = mass2 #mass of star in kg    should be --> 1.989e30
        self.starPosition = [gridArea[1]/2, gridArea[3]/2] #centre of the graph
        self.starRadius = 696340000 / gridScale       
        #all planet variables
        self.planetMass = mass1 #mass of planet in kg   should be --> 5.972e24
        self.planetRadius = 6371000000/gridScale
        self.planetPosition = [gridArea[1]/2 + (self.initial_distance / gridScale), gridArea[3]/2]
        #all initial velocity varioables
        self.x_velocity = 0
        self.y_velocity = -self.calculateInitialVelocity(self.initial_distance, self.starMass, self.planetMass, self.starPosition, self.planetPosition)
        #create the rays in the star class
        self.rays = []
        for i in range(0,2880,1):
            self.rays.append(Ray(self.starPosition, math.radians(i)/8))

    def calculateInitialVelocity(self, distance, starMass, planetMass, starPosition, planetPosition): #calculate the initial velocity of the planet to maintain a circular orbit (in theory this should remain constant)
        CoM_x = (1/(starMass + planetMass))*(planetMass*planetPosition[0] + starMass*starPosition[0])
        CoM_y = (1/(starMass + planetMass))*(planetMass*planetPosition[1] + starMass*starPosition[1])
        r_s = math.sqrt((CoM_x - starPosition[0])**2 + (CoM_y - starPosition[1])**2)
        initialVelocity = math.sqrt(G*planetMass*r_s*gridScale/(distance**2))
        return initialVelocity

    def calculateGravitationalForce(self, planetMass, starMass, distance): #calculating the force that the planet experiences due to the presence of the star 
        gravitationalForce = G * planetMass * starMass / distance**2
        return gravitationalForce

    def orbitingStar(self, planetPosition): #for trail purposes, the planet created will have properties that of Earth
        
        delta_t = 50000 #time between each timestep in seconds

        distance = math.sqrt(((planetPosition[0] - self.starPosition[0]) * gridScale)**2 + ((planetPosition[1] - self.starPosition[1]) * gridScale)**2) #distance = sqrt(delta x**2 + delta y**2)
        gravitationalForce = self.calculateGravitationalForce(self.planetMass, self.starMass, distance)
        acceleration = gravitationalForce / self.starMass

        #determine the angle from the horizontal plane 
        cos_angle = (-(planetPosition[0] - self.starPosition[0]) * gridScale) / distance #cos_theta = x_1 / distance
        sin_angle = (-(planetPosition[1] - self.starPosition[1]) * gridScale) / distance #sin_theta = y_1 / distance

        #calculate the x and y component of the acceleration
        x_acceleration = acceleration * cos_angle
        y_acceleration = acceleration * sin_angle

        #determine the change in velocity in the x and y direction
        self.x_velocity = self.x_velocity - x_acceleration * delta_t #v = u + a*delta_t
        self.y_velocity = self.y_velocity - y_acceleration * delta_t #v = u + a*delta_t

        #find the new position of the Earth and update the value
        self.starPosition[0] = self.starPosition[0] + (self.x_velocity * delta_t) / gridScale # x_2 = x_1 + v_x * delta_t
        self.starPosition[1] = self.starPosition[1] + (self.y_velocity * delta_t) / gridScale # y_2 = y_1 + v_y * delta_t

        return (self.starPosition[0], self.starPosition[1])
    
    #function to determine whether a ray hits a circle or a wall and then returns the point of closest intersection
    def look(self, walls, circles):
        detection_number = 0
        for i in range(0, len(self.rays)):
            point_circle = None
            point_wall = None
            closest = None
            record = math.inf
            for wall in walls:
                point_wall = self.rays[i].castWall(wall)
                if point_wall:
                    d1 = math.sqrt((point_wall[0] - self.starPosition[0]) ** 2 + (point_wall[1] - self.starPosition[1]) ** 2)
                    if d1 < record:
                        record = d1
                        closest = point_wall
            for circle in circles:
                point_circle = self.rays[i].castCircle(circle)
                if point_circle and len(point_circle) == 2:
                    d1 = math.sqrt((point_circle[0] - self.starPosition[0]) ** 2 + (point_circle[1] - self.starPosition[1]) ** 2)
                    if d1 < record:
                        record = d1
                        closest = point_circle
                if point_circle and len(point_circle) == 4:
                    d1 = math.sqrt((point_circle[0] - self.starPosition[0]) ** 2 + (point_circle[1] - self.starPosition[1]) ** 2)
                    d2 = math.sqrt((point_circle[2] - self.starPosition[0]) ** 2 + (point_circle[3] - self.starPosition[1]) ** 2)
                    if d1 < record:
                        record = d1
                        closest = [point_circle[0], point_circle[1]]
                    if d2 < record:
                        record = d2
                        closest = [point_circle[2], point_circle[3]]
            if point_wall:
                if point_wall[0] == closest[0] and point_wall[1] == closest[1]:
                    detection_number = detection_number + 1

        return detection_number
