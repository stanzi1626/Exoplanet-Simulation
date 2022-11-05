import matplotlib.pyplot as plt
import math

class Ray:

    def __init__ (self, pos, rad):

        self.position = pos
        self.direction = [math.cos(rad), math.sin(rad)]

    def castWall(self, wall):
        x1 = wall.a[0]
        x2 = wall.a[1]
        y1 = wall.b[0]
        y2 = wall.b[1]
        x3 = self.position[0]
        y3 = self.position[1]
        x4 = self.position[0] + self.direction[0]
        y4 = self.position[1] + self.direction[1]
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) #calculation for the denominator
        if den == 0:
            return
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        if t > 0 and t < 1 and u >0:
            x = x1 + t * (x2 - x1) #the x value of the point of intersection
            y = y1 + t * (y2 - y1)
            point = [x, y]
            return point
        else:
            return
    
    def castCircle(self, circle):
        ray_x1 = self.position[0]
        ray_y1 = self.position[1]
        ray_x2 = self.position[0] + self.direction[0]
        ray_y2 = self.position[1] + self.direction[1]
        i = circle.planetPosition[0] #x coordinate of the circle
        j = circle.planetPosition[1] #y coordinate of the circle
        if ray_x1 - ray_x2 != 0:
            m = (ray_y1 - ray_y2) / (ray_x1 - ray_x2) #the gradient of the line
            #y = mx + k
            #k = y - mx
            k = ray_y1 - (m * ray_x1)
            a = (m ** 2) + 1
            b = -(2 * i) - (2 * m * j) + (2 * m * k)
            c = (i ** 2) + (j ** 2) + (k ** 2) - (circle.planetRadius ** 2) - (2 * k * j)
            discriminant = (b ** 2) - (4 * a * c)
            if discriminant == 0:
                intersect_x = -(b / (2 * a))
                intersect_y = (m * intersect_x) + k
                point = [intersect_x, intersect_y]
                #need to make sure that the point of intersection is in the direction that the ray is facing
                if ray_x1 < ray_x2 < point[0] or point[0] < ray_x2 < ray_x1:
                    return point
                else:
                    return
            elif discriminant > 0:
                intersect_x1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                intersect_y1 = (m * intersect_x1) + k
                intersect_x2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                intersect_y2 = (m * intersect_x2) + k
                points = [intersect_x1, intersect_y1, intersect_x2, intersect_y2]
                #need to make sure that the point of intersection is in the direction that the ray is facing
                if ray_x1 < ray_x2 < points[0] or points[0] < ray_x2 < ray_x1:
                    return points
                else:
                    return
            else:
                return

        else:
            k = ray_x1
            a = 1
            b = -(2 * j)
            c = (i ** 2) + (j ** 2) + (k ** 2) - (circle.planetRadius ** 2) - (2 * k * j) + (k ** 2)
            
            if b ** 2 - 4 * a * c == 0:
                intersect_x = k
                intersect_y = -(b / (2 * a))
                point = [intersect_x, intersect_y]
                #need to make sure that the point of intersection is in the direction that the ray is facing
                if ray_x1 < ray_x2 < point[0] or point[0] < ray_x2 < ray_x1:
                    return point
                else:
                    return
            elif b ** 2 - 4 * a * c > 0:
                intersect_x1 = k
                intersect_y1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                intersect_x2 = k
                intersect_y2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                points = [intersect_x1, intersect_y1, intersect_x2, intersect_y2]
                #need to make sure that the point of intersection is in the direction that the ray is facing
                if ray_x1 < ray_x2 < points[0] or points[0] < ray_x2 < ray_x1:
                    return points
                else:
                    return
            else:
                return