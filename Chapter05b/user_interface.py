import tkinter as tk
from tkinter import ttk
import random
from copy import deepcopy

random.seed(42)

window = tk.Tk()
window.title('Sudoku GA Solver')
root = ttk.Frame(window)
root.grid(row=0, column=0)

input_array = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]  # TODO write as nested loop or list comprehension


# TODO write child class of Frame containing a structured sudoku cluster of widgets
# this should either take in problem values or display values from solution steps
# only integer values allowed
# should keep values in IntVars within addressable 9x9 array
# should keep widgets in addressable 9x9 array
# should provide input possibility for bg and fg, e.g. as nested 9x9 array
class SudokuFrame(tk.Frame):
    """A frame that constructs a 9x9 grid with input or label widgets"""
    def __init__(self, parent, widget_type, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.widget_type = widget_type
        self.variable_grid, self.widget_grid = self.build_sudoku('input')

    def build_sudoku(self, kind):
        """Based on kind constructs a 9x9 list with respective input type vars or widget"""

        if kind == 'input':
            wdg_type, var_type = tk.ttk.Entry, tk.IntVar
        else:
            wdg_type, var_type = tk.ttk.Label, tk.StringVar

        var_grid = list()
        wdg_grid = list()
        for i in range(9):
            var_row = list()
            wdg_row = list()
            for j in range(9):
                var = tk.IntVar()
                wdg = tk.ttk.Entry(textvariable=var)
                var_row.append(var)
                wdg_row.append(wdg)
            var_grid.append(var_row)
            wdg_grid.append(wdg_row)
        return var_grid, wdg_grid



fields = deepcopy(input_array)

for row in range(9):
    for col in range(9):
        fields[row][col] = tk.StringVar()

prob_label = ttk.Label(root, text='Gib ein Sudoku-Problem ein', font=('arial 40'), justify='center')
prob_label.grid(row=0, column=0, columnspan=3)

quit_button = ttk.Button(root, text='Quit', command=window.destroy, padding=5)
quit_button.grid(row=2, column=2)
fr = ttk.Frame(root)
fr.grid(row=1, column=0, columnspan=3)



superframes = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

for row in range(3):
    for col in range(3):
        superframes[row][col] = ttk.Frame(fr, padding=5)
        superframes[row][col].grid(row=row, column=col)

for row in range(9):
    for column in range(9):
        # fields[row][column] = ttk.Label(fr, text=f'[{row}, {column}]', font=('consolas', 20), anchor='center')
        super_col = column // 3
        super_row = row // 3
        sub_col = column % 3
        sub_row = row % 3

        ttk.Entry(superframes[super_row][super_col], width=3, textvariable=fields[row][column],
                  font=('consolas 30'), justify='center').grid(row=sub_row, column=sub_col)


def show_content():
    for row in range(9):
        for col in range(9):
            value = fields[row][col].get()
            if value != '':
                input_array[row][col] = int(value)


def retrieve(widget):
    print('retrieve')
    widget.grid(row=2, column=0)


def remove(widget1, widget2):
    print('remove')
    widget1.grid_forget()
    retrieve(widget2)


show_button = ttk.Button(root, text='Show', command=show_content, padding=5)
start_button = ttk.Button(root, text='Start', command=lambda: remove(start_button, show_button), padding=5)
start_button.grid(row=2, column=0)



window.mainloop()

print(input_array)