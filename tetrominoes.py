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

def main():
    win = GraphWin("Tetrominoes", 200, 150)
    shape = I_shape(Point(3, 1))
    shape.draw(win)
    win.mainloop()

main()
