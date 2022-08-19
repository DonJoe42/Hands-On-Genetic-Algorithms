import tkinter as tk
from tkinter import ttk
import random
import data_model as d
import user_interface as ui

random.seed(42)

# TODO write child class of Frame containing a structured sudoku cluster of widgets
# this should either take in problem values or display values from solution steps
# only integer values allowed
# should provide input possibility for bg and fg, e.g. as nested 9x9 array


class Application(tk.Tk):
    """This is the main application that takes in a problem and runs the solution algorithm"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Hybrid GA Sudoku Solver')
        self.root_frame = ui.BasicForm(self, 'input')  # TODO: replace this with a new form class
        self.root_frame.grid()


if __name__ == "__main__":
    app = Application()
    app.mainloop()

# fields = deepcopy(input_array)
#
# for row in range(9):
#     for col in range(9):
#         fields[row][col] = tk.StringVar()
#
# prob_label = ttk.Label(root, text='Gib ein Sudoku-Problem ein', font=('arial 40'), justify='center')
# prob_label.grid(row=0, column=0, columnspan=3)
#
# quit_button = ttk.Button(root, text='Quit', command=window.destroy, padding=5)
# quit_button.grid(row=2, column=2)
# fr = ttk.Frame(root)
# fr.grid(row=1, column=0, columnspan=3)
#
#
#
#
#
# def show_content():
#     for row in range(9):
#         for col in range(9):
#             value = fields[row][col].get()
#             if value != '':
#                 input_array[row][col] = int(value)
#
#
# def retrieve(widget):
#     print('retrieve')
#     widget.grid(row=2, column=0)
#
#
# def remove(widget1, widget2):
#     print('remove')
#     widget1.grid_forget()
#     retrieve(widget2)
#
#
# show_button = ttk.Button(root, text='Show', command=show_content, padding=5)
# start_button = ttk.Button(root, text='Start', command=lambda: remove(start_button, show_button), padding=5)
# start_button.grid(row=2, column=0)