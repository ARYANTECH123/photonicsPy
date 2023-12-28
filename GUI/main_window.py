import tkinter as tk

def draw_grid(canvas):
    # Set background color to gray
    canvas.create_rectangle(0, 0, 1000, 1000, fill="gray")

    # Draw white squares with a side length of 20 pixels
    side_length = 20
    for i in range(0, 1000, side_length):
        for j in range(0, 1000, side_length):
            canvas.create_rectangle(i, j, i + side_length, j + side_length, fill="white")

def draw_line(canvas, x0, y0, x1, y1):
    # Bresenham's line algorithm
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while True:
        canvas.create_rectangle(x0, y0, x0 + 20, y0 + 20, fill="blue")
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

def on_click(event, canvas, clicked_points):
    # Get the coordinates of the clicked point
    x = event.x
    y = event.y

    # Calculate the grid coordinates
    grid_x = (x // 20) * 20
    grid_y = (y // 20) * 20

    # Change the color of the clicked square to blue
    canvas.create_rectangle(grid_x, grid_y, grid_x + 20, grid_y + 20, fill="blue")

    # Add the clicked point to the list
    clicked_points.append((grid_x, grid_y))

    # If two points are clicked, draw a line and reset the list
    if len(clicked_points) == 2:
        x0, y0 = clicked_points[0]
        x1, y1 = clicked_points[1]
        draw_line(canvas, x0, y0, x1, y1)
        length = calculate_line_length(x0, y0, x1, y1)
        print(f"Line length: {length}")
        clicked_points.clear()

def calculate_line_length(x0, y0, x1, y1):
    # Calculate the length of the line using the distance formula
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Line Drawing")

    # Create a canvas widget
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()

    # Draw the grid on the canvas
    draw_grid(canvas)

    # List to keep track of clicked points
    clicked_points = []

    # Bind the click event to the canvas
    canvas.bind("<Button-1>", lambda event: on_click(event, canvas, clicked_points))

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
