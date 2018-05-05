from graphics import Rectangle, Point, GraphWin

#4.3.1. Block
class Block(Rectangle):
    PIXEL_TO_SQUARE_CONVERTING = 30
    WIDTH_OF_SQUARE = 30

    def __init__(self, point, color):
        top_left_corner = Point(point.x * Block.PIXEL_TO_SQUARE_CONVERTING, point.y * Block.PIXEL_TO_SQUARE_CONVERTING)
        bottom_right_corner = Point(top_left_corner.x + Block.WIDTH_OF_SQUARE, top_left_corner.y + Block.WIDTH_OF_SQUARE)

        Rectangle.__init__(self, top_left_corner, bottom_right_corner)

        self.setFill(color)

    def raw(self, win):
        self.draw(win)

#4.3.2. Tetromino
class Shape():
    def __init__(self, coords, color):
        tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
        x = 3
        for tetromino in tetrominoes:
            shape = tetromino(Point(x, 1))
            shape.draw(win)
            x += 4

    def raw(self, win):
        self.draw(win)

class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "blue")



def main():
    win = GraphWin("Tetrominoes", 200, 150)
    #block = Block(Point(1, 1), 'red')
    #block.draw(win)
    #shape = I_shape(Point(3, 1))
    shape = Shape([1,2], 'red')
    shape.draw(win)
    win.mainloop()

main()

