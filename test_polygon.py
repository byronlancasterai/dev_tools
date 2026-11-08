import pyglet
from pyglet import shapes

window = pyglet.window.Window(640, 480)
batch = pyglet.graphics.Batch()

# Polygon expects an iterable of (x, y) tuples
triangle_verts = [(200, 100), (300, 100), (250, 200)]
triangle = shapes.Polygon(*triangle_verts, color=(255, 0, 0), batch=batch)

square_verts = [(400, 100), (500, 100), (500, 200), (400, 200)]
square = shapes.Polygon(*square_verts, color=(0, 0, 255), batch=batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()
