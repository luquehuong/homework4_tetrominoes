from graphics import Rectangle, Point, GraphWin

#4.3.1. Block
class Block(Rectangle):
    BLOCK_SIZE = 30

    def __init__(self, point, color):
        top_left_corner = Point(point.x * Block.BLOCK_SIZE, point.y * Block.BLOCK_SIZE)
        bottom_right_corner = Point(top_left_corner.x + Block.BLOCK_SIZE, top_left_corner.y + Block.BLOCK_SIZE)

        Rectangle.__init__(self, top_left_corner, bottom_right_corner)

        self.setFill(color)

#4.3.2. Tetromino
class Shape():
    def __init__(self, list_of_points, color):
        self.list_of_blocks = list_of_points
        self.color = color

    def draw(self, win):
        for point in self.list_of_blocks:
            block = Block(point, self.color)
            block.draw(win)

class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "blue")

class J_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, "orange1")

class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "pink")

class O_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x - 1, center.y + 1),
                  Point(center.x    , center.y + 1),
                  Point(center.x    , center.y)]
        Shape.__init__(self, coords, "cyan")

class S_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x    , center.y + 1),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "GreenYellow")

class T_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x    , center.y + 1)]
        Shape.__init__(self, coords, "red")

class Z_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, "yellow")

def main():
    win = GraphWin("Tetrominoes", 900, 150)
    tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
    x = 3
    for tetromino in tetrominoes:
        shape = tetromino(Point(x, 1))
        shape.draw(win)
        x += 4
    win.mainloop()
    win.mainloop()

main()
