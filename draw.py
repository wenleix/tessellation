import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import RegularPolygon

LINE_WIDTH=0.5

def draw_hexagon(ax, center, size, color="black"):
    """Draw a regular hexagon centered at `center` with the given `size`."""
    x, y = center
    angles = np.linspace(0, 2 * np.pi, 7)
    xs = x + size * np.cos(angles)
    ys = y + size * np.sin(angles)
    ax.fill(xs, ys, color=color, edgecolor="black", linewidth=LINE_WIDTH)


def draw_triangle(ax, bottom_vertex, size, orientation="up", color="black"):
    """Draw an equilateral triangle with one vertex at `bottom_vertex`."""
    x, y = bottom_vertex
    if orientation == "up":
        vertices = [(x, y), (x + size / 2, y + np.sqrt(3) / 2 * size), (x - size / 2, y + np.sqrt(3) / 2 * size)]
    elif orientation == "down":
        vertices = [(x, y), (x + size / 2, y - np.sqrt(3) / 2 * size), (x - size / 2, y - np.sqrt(3) / 2 * size)]
    triangle = plt.Polygon(vertices, closed=True, facecolor=color, edgecolor="black", linewidth=LINE_WIDTH)
    ax.add_patch(triangle)

def draw_pattern(ax, center, size, num_layers):
    """Draw the full pattern with a hexagon center, squares, and triangles."""
    # Draw the central hexagon
    draw_hexagon(ax, center, size, color="lightgray")

    rect_rotate_anti_clock_deg = [30, 90, 150]

    # Draw sqaures
    for layer in range(1, num_layers + 1):
        for idx in range(6):
            angle_deg = 60 * idx + 30
            # Calculate positions for rectangles
            center_xy = (
                center[0] + size * (np.sqrt(3) / 2 + (layer - 0.5)) * np.cos(angle_deg * np.pi / 180),
                center[1] + size * (np.sqrt(3) / 2 + (layer - 0.5)) * np.sin(angle_deg * np.pi / 180),
            )
            # Well, this is over-complicated to compute and there are much easier way. but whatever
            rect_xy = (
                center_xy[0] + size * np.sqrt(2) / 2 * np.cos((180 + angle_deg + 45) * np.pi / 180),
                center_xy[1] + size * np.sqrt(2) / 2 * np.sin((180 + angle_deg + 45) * np.pi / 180),
            )

            # square = plt.Rectangle(rect_xy, width=size, height=size, facecolor='red', angle=angle_deg, edgecolor="black", linewidth=LINE_WIDTH)
            square = RegularPolygon(center_xy, 4, radius=np.sqrt(2) / 2, orientation=(75 - 30 * idx) * np.pi / 180, facecolor='red', edgecolor="black", linewidth=LINE_WIDTH)
            ax.add_patch(square)
            
            
            tri_center = (
                rect_xy[0] + size / np.sqrt(3) * np.cos(60 * idx * np.pi / 180),
                rect_xy[1] + size / np.sqrt(3) * np.sin(60 * idx * np.pi / 180),
            )
            triangle = RegularPolygon(tri_center, 3, radius=1 / np.sqrt(3), orientation=(60 * idx - 30) * np.pi / 180, facecolor='blue', edgecolor="black", linewidth=LINE_WIDTH)
            ax.add_patch(triangle) 


    
#            continue
#            # Calculate positions for triangles
#            tri_center = (
#                center[0] + (layer + 0.5) * dx * hex_size * 1.5,
#                center[1] + (layer + 0.5) * dy * hex_size * 1.5
#            )
#            draw_triangle(ax, tri_center, hex_size, color="blue")



# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis("equal")
ax.axis("off")

# Draw the pattern
draw_pattern(ax, center=(0, 0), size=1, num_layers=3)

# Show the plot
plt.show()

