import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

class Detector:

    def __init__(self, x1, y1, x2, y2):

        self.a = [x1, x2]
        self.b = [y1, y2]
    
    def placeDetector(self):
        return Line2D(self.a, self.b, color = 'lightcoral', linewidth=3)
        