import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


class Body:
    G = 6.67428e-11
    AU = 149.6e6
    TIMESTEP = 3600 * 24
    SCALE = 2.5*10**-120

    def __init__(self, x, y, radius, mass, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.colour = colour

        self.trail = []

        self.xv = 0
        self.yv = 0

    def force(self, obj):
        obj_x = obj.x
        obj_y = obj.y
        obj_dist_x = obj_x - self.x
        obj_dist_y = obj_y - self.y

        dist = math.sqrt(obj_dist_x ** 2 + obj_dist_y ** 2)
        force = self.G * self.mass * obj.mass / dist ** 2

        angle = math.atan2(obj_dist_y, obj_dist_x)

        force_x = math.cos(angle) * force
        force_y = math.sin(angle) * force

        return force_x, force_y

    def position(self, bodies):
        total_force_x = total_force_y = 0

        for body in bodies:
            if self == body:
                continue

            force_x, force_y = self.force(body)
            total_force_x += force_x
            total_force_y += force_y

            self.xv = total_force_x / self.mass * self.TIMESTEP
            self.yv = total_force_y / self.mass * self.TIMESTEP

            self.x += self.xv * self.TIMESTEP
            self.y += self.yv * self.TIMESTEP

            self.trail.append((self.x, self.y))

    def plot(self, ax):
        x = self.x * self.SCALE
        y = self.y * self.SCALE
        print(x)
        print(y)

        ax.add_artist(Circle(xy=(x, y), radius=self.radius,color=self.colour))
        ax.margins(1000, 1000)



def run():
    BODY_1 = Body(0, 0, 30, 1.98892 * 10 ** 30, (1,0,0))
    BODY_2 = Body(-1 * 6.67428e-11, 0, 16, 5.9742 * 10 ** 24,(0,1,0))
    bodies = [BODY_1, BODY_2]
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    for body in bodies:
        body.position(bodies)
        body.plot(ax)
    plt.show()


run()
