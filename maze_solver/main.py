from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    p1 = Point(100,100)
    p2 = Point(200,200)
    cell = Cell(win)
    cell.draw(p1.x, p2.x, p1.y, p2.y)
    win.wait_for_close()

main()