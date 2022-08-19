import tkinter as tk
from tkinter import ttk
import data_model as d

# TODO write child class of Frame containing a structured sudoku cluster of widgets
# this should either take in problem values or display values from solution steps
# only integer values allowed
# should provide input possibility for bg and fg, e.g. as nested 9x9 array


class BasicForm(ttk.Frame):
    """This is the main application that takes in a problem and runs the solution algorithm"""
    def __init__(self, parent, kind, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.kind = kind
        self.parent = parent

        # Add header
        ttk.Label(
            self,
            text='Hybrid Greedy plus Genetic Algorithm Sudoku Solver',
            anchor='center',
            font=('arial 15'),
            padding=5
        ).grid(row=0, column=0, sticky=tk.E+tk.W)

        # Build input frame for Sudoku problem
        self.sudoku_frame = SudokuFrame(self, self.kind)
        self.sudoku_frame.grid(column=0, row=1, sticky=tk.E+tk.W)

        # Build button frame and populate with start and quit
        self.button_frame = ButtonFrame(self)
        self.start_button = StartButton(self.button_frame)
        self.quit_button = QuitButton(self.button_frame, self.parent)


class SudokuFrame(ttk.LabelFrame):
    """Label frame that either takes in input or displays solution"""
    def __init__(self, parent, kind, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.kind = kind
        self.build_sudoku_sub_frame()
        self.set_label_name()
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)

    def build_sudoku_sub_frame(self):
        sub_frame = SudokuSubFrame(self, self.kind)
        sub_frame.grid(column=0, row=0, sticky='nsew')

    def set_label_name(self):
        my_label = 'Sudoku Problem' if self.kind == 'input' else 'Sudoku Solution'
        self.configure(text=my_label)


class SudokuSubFrame(ttk.Frame):
    """A frame that constructs a 9x9 grid with input or label widgets"""
    def __init__(self, parent, kind, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.kind = kind
        self.variable_grid = d.var_array()
        self.super_frame = self.build_super_frame()
        self.widget_grid = self.build_sudoku()

    def build_sudoku(self):
        """Based on kind constructs a 9x9 list with respective input type vars or widget"""

        if self.kind == 'input':
            wdg_type = ttk.Entry
        else:
            wdg_type = ttk.Label

        wdg_grid = list()
        for i in range(9):
            wdg_row = list()
            for j in range(9):
                # calculate address of super-frame
                super_col = j // 3
                super_row = i // 3
                sub_col = j % 3
                sub_row = i % 3

                # generate widget and var grids
                wdg = wdg_type(
                    self.super_frame[super_row][super_col],
                    textvariable=self.variable_grid[i][j],
                    width=3,
                    font=('consolas 30'),
                    justify='center'
                )
                wdg.grid(row=sub_row, column=sub_col)
                wdg_row.append(wdg)
            wdg_grid.append(wdg_row)
        return wdg_grid

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
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)


class StartButton(ttk.Button):
    """Button that launches the application and disappears"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, text='Start', padding=5, command=self.on_click, *args, **kwargs)
        self.grid(row=0, column=0, sticky='w')

    def on_click(self):
        # start greedy algorithm
        self.configure(default='disabled')


class QuitButton(ttk.Button):
    """Button that quits the application at any time"""
    def __init__(self, parent, application, *args, **kwargs):
        super().__init__(parent, text='Quit', padding=5, command=self.on_click, *args, **kwargs)
        self.grid(row=0, column=99, sticky='e')
        self.application = application

    def on_click(self):
        self.application.destroy()
