import tkinter
from array_of_points import create_vs

root = tkinter.Tk()

Canvas = tkinter.Canvas(root, bg="white", width="800", height="600")

ps = create_vs()[1]

DIFF = 250
for i, p in enumerate(ps):
    if i < len(ps) - 1:
        
        x = p.x + DIFF
        y = -1 * p.y + DIFF
        x1 = ps[i+1].x + DIFF
        y1 = -1 * ps[i+1].y + DIFF
        Canvas.create_line(x, y ,x1, y1)
Canvas.create_line(ps[-1].x + DIFF, -1 * ps[-1].y + DIFF, ps[0].x + DIFF, -1 * ps[0].y + DIFF)

Canvas.pack()
root.mainloop()
