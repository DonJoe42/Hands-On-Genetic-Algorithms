import tkinter as tk
from tkinter import ttk
import random
import data_model as d
import user_interface as ui


class Application(tk.Tk):
    """This is the main application that takes in a problem and runs the solution algorithm"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Hybrid GA Sudoku Solver')
        self.root_frame = ui.BasicForm(self, padding=10)  # TODO: replace this with a new form class
        self.root_frame.grid(sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.root_frame.bind('<<StartSolver>>', self._on_start)

    def _on_start(self, *_):
        input_grid = list()
        for i in range(9):
            input_row = list()
            for j in range(9):
                value = self.root_frame.input_variables[i][j].get()
                if value:
                    input_row.append(int(value))
                else:
                    input_row.append(0)
            input_grid.append(input_row)

        with open('input_grid.pkl', 'wb') as input_file:
            d.save_data(input_grid, input_file)

        self.root_frame.prepare_greedy()


if __name__ == "__main__":
    app = Application()
    app.mainloop()