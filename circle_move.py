import pyglet
import math

class CircleWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = self.width // 2
        self.y = self.height // 2
        self.radius = 20
        self.angle = 0
        self.speed = 0.05
        self.label = pyglet.text.Label(
            'Circle moving',
            font_size=14,
            x=10, y=10,
            color=(255, 255, 255, 255)
        )

    def update(self, dt):
        self.angle += self.speed
        self.x = int(self.width / 2 + 100 * math.cos(self.angle))
        self.y = int(self.height / 2 + 100 * math.sin(self.angle))

    def on_draw(self):
        self.clear()
        pyglet.shapes.Circle(self.x, self.y, self.radius, color=(0, 255, 0, 255))
        self.label.draw()

if __name__ == '__main__':
    win = CircleWindow(400, 400, caption='Circle Move')
    pyglet.clock.schedule_interval(win.update, 1/60)
    pyglet.app.run()
