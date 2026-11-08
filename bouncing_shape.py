#!/usr/bin/env python3
"""
A simple bouncing shape using pyglet.shapes.
"""
import pyglet
from pyglet import shapes
import random

class BouncingShape:
    def __init__(self, width, height):
        self.window = pyglet.window.Window(width, height, "Bouncing Shape")
        self.width = width
        self.height = height
        
        # Create a circle
        self.radius = 20
        self.x = random.uniform(self.radius, width - self.radius)
        self.y = random.uniform(self.radius, height - self.radius)
        self.dx = random.uniform(2, 5)
        self.dy = random.uniform(2, 5)
        
        self.circle = shapes.Circle(self.x, self.y, self.radius, color=(255, 100, 100))
        
        @self.window.event
        def on_draw():
            self.window.clear()
            self.circle.draw()
            
        # Update position
        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def update(self, dt):
        self.x += self.dx
        self.y += self.dy
        
        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > self.width:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > self.height:
            self.dy *= -1
            
        self.circle.x = self.x
        self.circle.y = self.y

if __name__ == "__main__":
    app = BouncingShape(800, 600)
    pyglet.app.run()
