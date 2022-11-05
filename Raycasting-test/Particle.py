from RayTest import Ray
import matplotlib.pyplot as plt
import math

class Particle:

    def __init__(self):
        self.position = []
        self.rays = []
        xy = plt.ginput(1)
        x = [p[0] for p in xy]
        y = [p[1] for p in xy]
        a = x[0]
        b = y[0]
        self.position.append(a)
        self.position.append(b)
        for i in range(0, 360, 10):
            self.rays.append(Ray(self.position, math.radians(i)))
        
    def draw_particle(self):
        plt.plot([self.position[0]], [self.position[1]], 'bo', ms = 2)
        for i in range(0, len(self.rays)):
            self.rays[i].draw_ray()

    def look(self, walls, circles):
        for i in range(0, len(self.rays)):
            closest = None
            record = math.inf
            for wall in walls:
                point_wall = self.rays[i].castWall(wall)
                if point_wall:
                    d1 = math.sqrt((point_wall[0] - self.position[0]) ** 2 + (point_wall[1] - self.position[1]) ** 2)
                    if d1 < record:
                        record = d1
                        closest = point_wall
            for circle in circles:
                point_circle = self.rays[i].castCircle(circle)
                if point_circle and len(point_circle) == 2:
                    d1 = math.sqrt((point_circle[0] - self.position[0]) ** 2 + (point_circle[1] - self.position[1]) ** 2)
                    if d1 < record:
                        record = d1
                        closest = point_circle
                if point_circle and len(point_circle) == 4:
                    d1 = math.sqrt((point_circle[0] - self.position[0]) ** 2 + (point_circle[1] - self.position[1]) ** 2)
                    d2 = math.sqrt((point_circle[2] - self.position[0]) ** 2 + (point_circle[3] - self.position[1]) ** 2)
                    if d1 < record:
                        record = d1
                        closest = [point_circle[0], point_circle[1]]
                    if d2 < record:
                        record = d2
                        closest = [point_circle[2], point_circle[3]]
                print(closest)
            if closest:
                ax = plt.gca()
                plt.plot([self.position[0], closest[0]], [self.position[1], closest[1]], marker = ',')
                ax.figure.canvas.draw()





                    
                


 