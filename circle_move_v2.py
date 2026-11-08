import pyglet
import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.batch = pyglet.graphics.Batch()
        self.circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=(0, 255, 0), batch=self.batch)
        self.t = 0

    def update(self, dt):
        self.t += dt
        # Sine wave motion
        self.x = 200 + 100 * math.cos(self.t)
        self.y = 200 + 50 * math.sin(self.t * 2)
        self.circle.x = self.x
        self.circle.y = self.y

window = pyglet.window.Window(400, 400, caption='Circle Move V2')
circle = Circle(200, 200, 20)

@window.event
def on_draw():
    window.clear()
    circle.batch.draw()

def update(dt):
    circle.update(dt)

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()