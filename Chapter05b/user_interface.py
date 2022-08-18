import tkinter as tk
from tkinter import ttk
import random

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
        self.root_frame = ttk.Frame(self, padding=10)
        self.root_frame.pack()

        # Build input frame for Sudoku problem
        self.sudoku_frame = SudokuFrame(self.root_frame, 'input')
        self.sudoku_frame.grid(column=0, row=0)

        # Build button frame and populate with start and quit
        self.button_frame = ButtonFrame(self.root_frame)
        self.start_button = StartButton(self.button_frame)
        self.quit_button = QuitButton(self.button_frame, self)


class SudokuFrame(ttk.LabelFrame):
    """Label frame that either takes in input or displays solution"""
    def __init__(self, parent, kind, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.kind = kind
        self.build_sudoku_sub_frame()
        self.set_label_name()

    def build_sudoku_sub_frame(self):
        sub_frame = SudokuSubFrame(self, self.kind)
        sub_frame.grid(column=0, row=0, sticky='NSEW')

    def set_label_name(self):
        my_label = 'Sudoku Problem' if self.kind == 'input' else 'Sudoku Solution'
        self.configure(text=my_label)


class SudokuSubFrame(ttk.Frame):
    """A frame that constructs a 9x9 grid with input or label widgets"""
    def __init__(self, parent, kind, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.kind = kind
        self.super_frame = self.build_super_frame()
        self.variable_grid, self.widget_grid = self.build_sudoku()

    def build_sudoku(self):
        """Based on kind constructs a 9x9 list with respective input type vars or widget"""

        if self.kind == 'input':
            wdg_type, var_type = ttk.Entry, tk.StringVar
        else:
            wdg_type, var_type = ttk.Label, tk.StringVar

        var_grid = list()
        wdg_grid = list()
        for i in range(9):
            var_row = list()
            wdg_row = list()
            for j in range(9):
                # calculate address of super-frame
                super_col = j // 3
                super_row = i // 3
                sub_col = j % 3
                sub_row = i % 3

                # generate widget and var grids
                var = var_type()
                wdg = wdg_type(
                    self.super_frame[super_row][super_col],
                    textvariable=var,
                    width=3,
                    font=('consolas 30'),
                    justify='center'
                )
                wdg.grid(row=sub_row, column=sub_col)
                var_row.append(var)
                wdg_row.append(wdg)
            var_grid.append(var_row)
            wdg_grid.append(wdg_row)
        return var_grid, wdg_grid

    def build_super_frame(self):
        """Builds an array of 3x3 super-frames representing sudoku sub-arrays that are visibly separated"""
        sup_frames = list()
        for row in range(3):
            sup_row = list()
            for col in range(3):
                sup_frame = ttk.Frame(self, padding=5)
                sup_frame.grid(row=row, column=col)
                sup_row.append(sup_frame)
            sup_frames.append(sup_row)

        return sup_frames

    def get_variable_grid(self):
        return self.variable_grid

    def get_widget_grid(self):
        return self.widget_grid

    def get_super_frames(self):
        return self.super_frame


class ButtonFrame(ttk.LabelFrame):
    """Adds frame that holds various buttons depending on phase of program"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, text='Buttons', *args, **kwargs)
        self.grid(row=99, column=0, sticky="ew")


class StartButton(ttk.Button):
    """Button that launches the application and disappears"""
    def __init__(self, parent, save_input, *args, **kwargs):
        super().__init__(parent, text='Start', padding=5, command=self.on_click, *args, **kwargs)
        self.grid(row=0, column=0, sticky='w')
        self.save_input = save_input

    def on_click(self):
        # start greedy algorithm
        self.save_input()
        self.grid_forget()


class QuitButton(ttk.Button):
    """Button that quits the application at any time"""
    def __init__(self, parent, application, *args, **kwargs):
        super().__init__(parent, text='Quit', padding=5, command=self.on_click, *args, **kwargs)
        self.grid(row=0, column=99, sticky='e')
        self.application = application

    def on_click(self):
        self.application.destroy()


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