import tkinter as tk
import bjbs_chart

def runMain():
    green_color = "#24b670"
    yellow_color = "#efc514"
    blue_color = "#3ebab4"

    cell_size = 60  # Adjust this value to change the size of each cell

    def create_grid_splits(root, rows, columns):
        rects = []
        labels = []

        for row in range(rows):
            for col in range(columns):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                rect = splits_canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                rects.append(rect)
                # Calculate center of the square
                center_x = x1 + (cell_size / 2)
                center_y = y1 + (cell_size / 2)
                label_text = bjbs_chart.chart_array[row][col]
                if label_text != "X":
                    label = tk.Label(root, text=label_text, font=("Arial", 20))  # Adjust font size as needed
                    label_id = splits_canvas.create_window(center_x, center_y, window=label)
                    labels.append((label, label_id))

        def change_color(row, col, color):
            index = row * columns + col
            if 0 <= index < len(rects):
                splits_canvas.itemconfig(rects[index], fill=color)

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
            change_color(1, j, green_color)
            change_color(3, j, green_color)
            change_color(3, 6, "white")
            change_color(3, 9, "white")
            change_color(3, 10, "white")
            change_color(4, j, green_color)
            change_color(5, j, green_color)
            for x in range(7, 11):
                change_color(5, x, "white")
            change_color(6, j, green_color)
            for x in range(6, 11):
                change_color(6, x, "white")
            change_color(7, j, "white")
            change_color(8, j, "white")
            for x in range(4, 6):
                change_color(8, x, green_color)
            change_color(9, j, green_color)
            change_color(10, j, green_color)
            for x in range(7, 11):
                change_color(9, x, "white")
                change_color(10, x, "white")

        for j in range(0, 10):
            change_label_color(1, j, green_color)
            change_label_color(2, j, "white")
            change_label_color(3, j, green_color)
            change_label_color(3, 5, "white")
            change_label_color(3, 8, "white")
            change_label_color(3, 9, "white")
            change_label_color(4, j, green_color)
            change_label_color(5, j, green_color)
            for x in range(6, 10):
                change_label_color(5, x, "white")
            change_label_color(6, j, green_color)
            for x in range(5, 10):
                 change_label_color(6, x, "white")
            change_label_color(7, j, "white")
            change_label_color(8, j, "white")
            for x in range(3, 5):
                change_label_color(8, x, green_color)
            change_label_color(9, j, green_color)
            change_label_color(10, j, green_color)
            for x in range(6, 10):
                change_label_color(9, x, "white")
                change_label_color(10, x, "white")

    def create_grid_softs(root, rows, columns):
        rects = []
        labels = []

        for row in range(rows):
            for col in range(columns):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                rect = softs_canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                rects.append(rect)
                # Calculate center of the square
                center_x = x1 + (cell_size / 2)
                center_y = y1 + (cell_size / 2)
                label_text = bjbs_chart.chart_array[row + 10][col]
                label = tk.Label(root, text=label_text, font=("Arial", 20))  # Adjust font size as needed
                label_id = softs_canvas.create_window(center_x, center_y, window=label)
                labels.append((label, label_id))


        def change_color(row, col, color):
            index = row * columns + col
            if 0 <= index < len(rects):
                softs_canvas.itemconfig(rects[index], fill=color)

        def change_label_color(row, col, color):
            index = row * columns + col
            if 0 <= index < len(labels):
                labels[index][0].config(bg=color)

        def change_row0_text(text_list):
            for col, text in enumerate(text_list):
                labels[col][0].config(text=text)

        change_row0_text(["", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A"])
        for j in range(0, 11):
            change_color(0, j, "lightgrey")
            change_label_color(0, j, "lightgrey")
        for i in range(1, 11):
            change_color(i, 0, "lightgrey")
            change_label_color(i, 0, "lightgrey")

        for i in range(1, 3):
            for j in range(1, 11):
                change_color(i, j, yellow_color)
                change_label_color(i, j, yellow_color)
        change_color(2, 5, blue_color)
        change_label_color(2, 5, blue_color)

        for j in range(1, 6):
            change_color(3, j, blue_color)
            change_label_color(3, j, blue_color)
        for j in range(6, 8):
            change_color(3, j, yellow_color)
            change_label_color(3, j, yellow_color)
        for j in range(8, 11):
            change_label_color(3, j, "white")
        for j in range(1, 11):
            change_color(4, j, "white")
            change_label_color(4, j, "white")
        for j in range(2, 6):
            change_color(4, j, green_color)
            change_label_color(4, j, green_color)
        for i in range(5, 7):
            for j in range(1, 11):
                change_color(i, j, "white")
                change_label_color(i, j, "white")
            for j in range(3, 6):
                change_color(i, j, green_color)
                change_label_color(i, j, green_color)
        for i in range(7, 9):
            for j in range(1, 11):
                change_color(i, j, "white")
                change_label_color(i, j, "white")
            for j in range(4, 6):
                change_color(i, j, green_color)
                change_label_color(i, j, green_color)

    def create_grid_hards(root, rows, columns):
        rects = []
        labels = []

        for row in range(rows):
            for col in range(columns):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                rect = hards_canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                rects.append(rect)
                # Calculate center of the square
                center_x = x1 + (cell_size / 2)
                center_y = y1 + (cell_size / 2)
                label_text = bjbs_chart.chart_array[row + 18][col]
                label = tk.Label(root, text=label_text, font=("Arial", 20))  # Adjust font size as needed
                label_id = hards_canvas.create_window(center_x, center_y, window=label)
                labels.append((label, label_id))

        def change_color(row, col, color):
            index = row * columns + col
            if 0 <= index < len(rects):
                hards_canvas.itemconfig(rects[index], fill=color)

        def change_label_color(row, col, color):
            index = row * columns + col
            if 0 <= index < len(labels):
                labels[index][0].config(bg=color)

        def change_row0_text(text_list):
            for col, text in enumerate(text_list):
                labels[col][0].config(text=text)

        change_row0_text(["", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A"])
        for j in range(0, 11):
            change_color(0, j, "lightgrey")
            change_label_color(0, j, "lightgrey")
        for i in range(1, 11):
            change_color(i, 0, "lightgrey")
            change_label_color(i, 0, "lightgrey")

        for j in range(1, 11):
            change_color(1, j, yellow_color)
            change_label_color(1, j, yellow_color)

        for i in range(2, 6):
            for j in range(1, 6):
                change_color(i, j, yellow_color)
                change_label_color(i, j, yellow_color)
            for j in range(6, 11):
                change_color(i, j, "white")
                change_label_color(i, j, "white")

        for j in range(1, 11):
            change_color(6, j, "white")
            change_label_color(6, j, "white")
        for j in range(3, 6):
            change_color(6, j, yellow_color)
            change_label_color(6, j, yellow_color)

        for j in range(1, 11):
            change_color(7, j, green_color)
            change_label_color(7, j, green_color)

        for j in range(1, 9):
            change_color(8, j, green_color)
            change_label_color(8, j, green_color)
        for j in range(9, 11):
            change_color(8, j, "white")
            change_label_color(8, j, "white")

        for j in range(1, 11):
            change_color(9, j, "white")
            change_label_color(9, j, "white")
        for j in range(2, 6):
            change_color(9, j, green_color)
            change_label_color(9, j, green_color)

        for j in range(1, 11):
            change_color(10, j, "white")
            change_label_color(10, j, "white")

    def change_to_splits():
        root.title("Basic Strategy Chart: Splits")
        softs_canvas.place_forget()
        hards_canvas.place_forget()
        splits_btn.config(relief=tk.SUNKEN, state=tk.DISABLED)
        softs_btn.config(relief=tk.RAISED, state=tk.NORMAL)
        hards_btn.config(relief=tk.RAISED, state=tk.NORMAL)
        splits_canvas.place(x=0, y=65)

        split_yes_key_canvas.place(x=700, y=75)
        split_yes_key_label.place(x=120 / 2, y=60 / 2, anchor="center")
        split_no_key_canvas.place(x=700, y=150)
        split_no_key_label.place(x=210 / 2, y=60 / 2, anchor="center")

        stand_key_canvas.place_forget()
        stand_key_label.place_forget()
        hit_key_label.place_forget()
        hit_key_canvas.place_forget()
        doubleHit_key_canvas.place_forget()
        doubleHit_key_label.place_forget()
        doubleStand_key_canvas.place_forget()
        doubleStand_key_label.place_forget()

    def change_to_softs():
        root.title("Basic Strategy Chart: Soft Totals")
        splits_canvas.place_forget()
        hards_canvas.place_forget()
        splits_btn.config(relief=tk.RAISED, state=tk.NORMAL)
        softs_btn.config(relief=tk.SUNKEN, state=tk.DISABLED)
        hards_btn.config(relief=tk.RAISED, state=tk.NORMAL)
        softs_canvas.place(x=0, y=75)

        split_yes_key_canvas.place_forget()
        split_yes_key_label.place_forget()
        split_no_key_canvas.place_forget()
        split_no_key_label.place_forget()

        stand_key_canvas.place(x=700, y=75)
        stand_key_label.place(x=120 / 2, y=60 / 2, anchor="center")
        hit_key_canvas.place(x=700, y=150)
        hit_key_label.place(x=120 / 2, y=60 / 2, anchor="center")
        doubleHit_key_canvas.place(x=700, y=225)
        doubleHit_key_label.place(x=240 / 2, y=60 / 2, anchor="center")
        doubleStand_key_canvas.place(x=700, y=300)
        doubleStand_key_label.place(x=270 / 2, y=60 / 2, anchor="center")

    def change_to_hards():
        root.title("Basic Strategy Chart: Hard Totals")
        splits_canvas.place_forget()
        softs_canvas.place_forget()
        splits_btn.config(relief=tk.RAISED, state=tk.NORMAL)
        softs_btn.config(relief=tk.RAISED, state=tk.NORMAL)
        hards_btn.config(relief=tk.SUNKEN, state=tk.DISABLED)
        hards_canvas.place(x=0, y=75)

        split_yes_key_canvas.place_forget()
        split_yes_key_label.place_forget()
        split_no_key_canvas.place_forget()
        split_no_key_label.place_forget()
        stand_key_canvas.place(x=700, y=75)
        stand_key_label.place(x=120 / 2, y=60 / 2, anchor="center")
        hit_key_canvas.place(x=700, y=150)
        hit_key_label.place(x=120 / 2, y=60 / 2, anchor="center")
        doubleHit_key_canvas.place(x=700, y=225)
        doubleHit_key_label.place(x=240 / 2, y=60 / 2, anchor="center")
        doubleStand_key_canvas.place_forget()
        doubleStand_key_label.place_forget()

    def close_window():
        root.destroy()

    root = tk.Tk()
    root.title("Basic Strategy Chart: Splits")
    # icon2 = tk.PhotoImage(file="bitcoin.png")
    # root.iconphoto(True, icon2)
    root.geometry("1200x900")

    splits_canvas = tk.Canvas(root, width=cell_size*11, height=cell_size*11, borderwidth=0, highlightthickness=0)
    splits_canvas.place(x=0, y=75)
    create_grid_splits(root, 11, 11)

    softs_canvas = tk.Canvas(root, width=cell_size*11, height=cell_size*9, borderwidth=0, highlightthickness=0)
    create_grid_softs(root, 9, 11)

    hards_canvas = tk.Canvas(root, width=cell_size*11, height=cell_size*11, borderwidth=0, highlightthickness=0)
    create_grid_hards(root, 11, 11)

    splits_btn = tk.Button(root, text="Splits Chart", font=("Arial", 20), command=change_to_splits)
    splits_btn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    softs_btn = tk.Button(root, text="Soft Totals Chart", font=("Arial", 20), command=change_to_softs)
    hards_btn = tk.Button(root, text="Hard Totals Chart", font=("Arial", 20), command=change_to_hards)
    close_btn = tk.Button(root, text="Close Window", font=("Arial", 20), command=close_window)
    splits_btn.place(x=20, y=15)
    softs_btn.place(x=195, y=15)
    hards_btn.place(x=430, y=15)
    close_btn.place(x=500, y=750)

    split_yes_key_canvas = tk.Canvas(root, width=120, height=60, bg=green_color)
    split_yes_key_canvas.place(x=700, y=75)
    split_yes_key_label = tk.Label(split_yes_key_canvas, text="Y = Split", font=("Arial", 20), bg=green_color)
    split_yes_key_label.place(x=120/2, y=60/2, anchor="center")

    split_no_key_canvas = tk.Canvas(root, width=210, height=60, bg="white")
    split_no_key_canvas.place(x=700, y=150)
    split_no_key_label = tk.Label(split_no_key_canvas, text="N = Do Not Split", font=("Arial", 20), bg="white")
    split_no_key_label.place(x=210/2, y=60/2, anchor="center")

    stand_key_canvas = tk.Canvas(root, width=120, height=60, bg=yellow_color)
    #stand_key_canvas.place(x=700, y=75)
    stand_key_label = tk.Label(stand_key_canvas, text="Stand", font=("Arial", 20), bg=yellow_color)
    #stand_key_label.place(x=120/2, y=60/2, anchor="center")

    hit_key_canvas = tk.Canvas(root, width=120, height=60, bg="white")
    #hit_key_canvas.place(x=700, y=150)
    hit_key_label = tk.Label(hit_key_canvas, text="Hit", font=("Arial", 20), bg="white")
    #hit_key_label.place(x=120/2, y=60/2, anchor="center")

    doubleHit_key_canvas = tk.Canvas(root, width=240, height=60, bg=green_color)
    #doubleHit_key_canvas.place(x=700, y=225)
    doubleHit_key_label = tk.Label(doubleHit_key_canvas, text="Dh = Double or Hit", font=("Arial", 20), bg=green_color)
    #doubleHit_key_label.place(x=240/2, y=60/2, anchor="center")

    doubleStand_key_canvas = tk.Canvas(root, width=270, height=60, bg=blue_color)
    #doubleStand_key_canvas.place(x=700, y=300)
    doubleStand_key_label = tk.Label(doubleStand_key_canvas, text="Ds = Double or Stand", font=("Arial", 20), bg=blue_color)
    #doubleStand_key_label.place(x=270/2, y=60/2, anchor="center")

    root.mainloop()