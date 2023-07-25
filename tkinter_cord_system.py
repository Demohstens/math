import tkinter
import array_of_points as ap

root = tkinter.Tk()

Canvas = tkinter.Canvas(root, bg="white", width="800", height="600")

DIFF = 250
for i, p in enumerate(ap.ps):
    if i < len(ap.ps) - 1:
        
        x = p.x + DIFF
        y = -1 * p.y + DIFF
        x1 = ap.ps[i+1].x + DIFF
        y1 = -1 * ap.ps[i+1].y + DIFF
        Canvas.create_line(x, y ,x1, y1)
Canvas.create_line(ap.ps[-1].x + DIFF, -1 * ap.ps[-1].y + DIFF, ap.ps[0].x + DIFF, -1 * ap.ps[0].y + DIFF)

Canvas.pack()
root.mainloop()
