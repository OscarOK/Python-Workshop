class Cell(object):
    def __init__(self, x, y, is_alive, cell_size):
        self.dead = color(0, 0, 0)
        self.live = color(255, 255, 255)
        self.cell_size = cell_size
        self.x = x
        self.y = y
        self.is_alive = is_alive

    def set_color(self):
        if self.is_alive:
            return self.live
        return self.dead

    def update(self):
        stroke(0)
        fill(self.set_color())
        rect(self.x, self.y, self.cell_size, self.cell_size)
