import os
from array_of_points import create_vs

def to_svg(list_of_vectors, filename = "output.svg", file_location = ".\\", color = "black", width = 1):
    with open(file_location + filename, "w") as svg_file:
        svg_file.write("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">""")
        svg_file.write("\n<svg>")
        for i, v in enumerate(list_of_vectors):
            if i == len(list_of_vectors) - 1:
                break
            x = v[0]
            y = v[1]
            x1 = list_of_vectors[i-1][0]
            y1 = list_of_vectors[i-1][1]
            svg_file.write(f"\n\t<line x1=\"{x}\" y1=\"{y}\" x2=\"{x1}\" y2=\"{y1}\" stroke=\"{color}\" stroke-width=\"{width}\"/>")
        svg_file.write("\n</svg>")
    return "Done!"

if __name__ == "__main__":
    print(to_svg(create_vs()))