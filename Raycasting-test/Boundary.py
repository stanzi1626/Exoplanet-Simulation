import matplotlib.pyplot as plt

class Boundary:

    def __init__(self, x1, y1, x2, y2):
        self.a = [x1, x2]
        self.b = [y1, y2]
        self.xy1 = [x1, y1]
        self.r = x2
    
    def drawWall(self):
        plt.plot(self.a, self.b, marker=',')

    def drawCircle(self):
        placeCircle= plt.Circle(self.xy1, radius=self.r, fill=True, color="red")
        plt.gca().add_patch(placeCircle)
    
