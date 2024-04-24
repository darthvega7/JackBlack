import tkinter as tk
import bjbs_chart

def create_grid(root, rows, columns):
    rects = []
    labels = []

    for row in range(rows):
        for col in range(columns):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            rect = canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
            rects.append(rect)
            # Calculate center of the square
            center_x = x1 + (cell_size / 2)
            center_y = y1 + (cell_size / 2)
            label_text = bjbs_chart.chart_array[row][col]
            if label_text != "X":
                label = tk.Label(root, text=label_text, font=("Arial", 20))  # Adjust font size as needed
                label_id = canvas.create_window(center_x, center_y, window=label)
                labels.append((label, label_id))

    def change_color(row, col, color):
        index = row * columns + col
        if 0 <= index < len(rects):
            canvas.itemconfig(rects[index], fill=color)
            #labels[index][0].config(bg=color)

    def change_label_color(row, col, color):
        index = row * columns + col
        if 0 <= index < len(labels):
            labels[index][0].config(bg=color)

    # Set Background Color for Dealer Card and Player Cards to LightGrey
    for j in range(0, 11):
        change_color(0, j, "lightgrey")
    for i in range(0, 11):
        change_color(i, 0, "lightgrey")

    # Always Split Aces
    for j in range(1, 11):
        change_color(1, j, "green")
        change_color(3, j, "green")
        change_color(3, 6, "white")
        change_color(3, 9, "white")
        change_color(3, 10, "white")
        change_color(4, j, "green")
        change_color(5, j, "green")
        for x in range(7, 11):
            change_color(5, x, "white")
        change_color(6, j, "green")
        for x in range(6, 11):
            change_color(6, x, "white")
        change_color(7, j, "white")
        change_color(8, j, "white")
        for x in range(4, 6):
            change_color(8, x, "green")
        change_color(9, j, "green")
        change_color(10, j, "green")
        for x in range(7, 11):
            change_color(9, x, "white")
            change_color(10, x, "white")

    for j in range(0, 10):
        change_label_color(1, j, "green")
        change_label_color(2, j, "white")
        change_label_color(3, j, "green")
        change_label_color(3, 5, "white")
        change_label_color(3, 8, "white")
        change_label_color(3, 9, "white")
        change_label_color(4, j, "green")
        change_label_color(5, j, "green")
        for x in range(6, 10):
            change_label_color(5, x, "white")
        change_label_color(6, j, "green")
        for x in range(5, 10):
             change_label_color(6, x, "white")
        change_label_color(7, j, "white")
        change_label_color(8, j, "white")
        for x in range(3, 5):
            change_label_color(8, x, "green")
        change_label_color(9, j, "green")
        change_label_color(10, j, "green")
        for x in range(6, 10):
            change_label_color(9, x, "white")
            change_label_color(10, x, "white")



root = tk.Tk()
root.title("Basic Strategy Chart: Splits")
icon = tk.PhotoImage(file="bitcoin.png")
root.iconphoto(True, icon)

cell_size = 60  # Adjust this value to change the size of each cell

canvas = tk.Canvas(root, width=cell_size*11, height=cell_size*11, borderwidth=0, highlightthickness=0)
canvas.pack()

create_grid(root, 11, 11)

root.mainloop()
