import matplotlib.pyplot as plt

plt.axes(xlim=(0, 12), ylim=(0, 12))

class LineDrawer(object):
    #lines = []
    def draw_line(self):
        ax = plt.gca()
        xy = plt.ginput(1)

        x = [p[0] for p in xy]
        y = [p[1] for p in xy]
        line = plt.plot(x,y)
        ax.figure.canvas.draw()

        #self.lines.append(line)
    
ld = LineDrawer()
ld.draw_line()


plt.show()