import math

class W:
    def __init__(self):
        self.width = 400
        self.height = 400
        self.x = self.width // 2
        self.y = self.height // 2
        self.radius = 20
        self.angle = 0
        self.speed = 0.05

    def update(self, dt):
        self.angle += self.speed
        self.x = int(self.width / 2 + 100 * math.cos(self.angle))
        self.y = int(self.height / 2 + 100 * math.sin(self.angle))

w = W()
assert (w.x, w.y) == (200, 200), f"start expected (200,200) got {(w.x, w.y)}"
for _ in range(10):
    w.update(1/60)
assert (w.x, w.y) == (287, 247), f"after 10 frames expected (287,247) got {(w.x, w.y)}"
print('start:', w.x, w.y)
print('after 10 frames:', w.x, w.y)
