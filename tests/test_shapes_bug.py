#!/usr/bin/env python3
"""Document the pyglet 2.x shapes.Circle buffer error."""
import sys
import traceback

# Import pyglet first so the GL context is initialized.
import pyglet
from pyglet import shapes

# Create a window so we have a valid context.
window = pyglet.window.Window(320, 240, "shapes test")

# Try to create a Circle with the parameters that fail on this machine.
# The error is: pyglet.lib.glu.glGenVertexArrays raises a buffer error
# when shapes.Circle is instantiated.
try:
    c = shapes.Circle(100, 100, 20, color=(255, 100, 100))
    print("OK: shapes.Circle created without error.")
    print(f"  x={c.x}, y={c.y}, radius={c.radius}")
    print(f"  vertex_count={c.vertex_count if hasattr(c, 'vertex_count') else 'no attr'}")
except Exception as e:
    print(f"FAIL: {type(e).__name__}: {e}")
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)

window.close()
sys.exit(0)
