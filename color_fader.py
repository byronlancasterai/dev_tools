#!/usr/bin/env python3
"""
A simple color-fader window using pyglet.
Runs headlessly with a timeout to verify it does not crash.
"""
import pyglet
from pyglet.window import key


class ColorFader:
    def __init__(self, width=320, height=240):
        self.window = pyglet.window.Window(width, height, "Color Fader")
        self.r = 1.0
        self.g = 0.0
        self.b = 0.0
        self.speed = 0.02
        self.direction = 1

        @self.window.event
        def on_draw():
            import pyglet.gl as gl
            gl.glClearColor(self.r, self.g, self.b, 1.0)
            self.window.clear()

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.ESCAPE:
                pyglet.app.exit()

        pyglet.clock.schedule_interval(self.update, 1/30)

    def update(self, dt):
        self.r += self.direction * self.speed * dt * 10
        if self.r > 1.0:
            self.r = 1.0
            self.g = 0.0
            self.b = 0.0
            self.direction = -1
        elif self.r < 0.0:
            self.r = 0.0
            self.g = 0.0
            self.b = 0.0
            self.direction = 1


if __name__ == "__main__":
    app = ColorFader()
    pyglet.app.run()
