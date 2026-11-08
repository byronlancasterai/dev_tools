import pyglet
import pyglet.shapes

class PatternWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.shapes = []
        size = 40
        spacing = 50
        
        # Create shapes once
        for x in range(0, 800, spacing):
            for y in range(0, 600, spacing):
                rect = pyglet.shapes.Rectangle(x, y, size, size, color=(255, 100, 100), batch=self.batch)
                self.shapes.append((x, y, rect))

    def on_draw(self):
        self.clear()
        import time
        t = time.time()
        
        # Update colors based on time
        for x, y, rect in self.shapes:
            phase = (x // 50 + y // 50 + int(t * 2)) % 2
            if phase == 0:
                rect.color = (255, 100, 100)
            else:
                rect.color = (100, 100, 255)
                
        self.batch.draw()
                
if __name__ == '__main__':
    win = PatternWindow(800, 600, caption='Pattern')
    pyglet.app.run()
