import unittest
import controll
import data_model
import user_interface
import tkinter


class TestFrontend(unittest.TestCase):

    def test_grid_hook(self):
        app = tkinter.Tk()
        sub_frame = user_interface.SudokuSubFrame(app, 'input')
        var_grid = sub_frame.get_variable_grid()
        wdg_grid = sub_frame.get_widget_grid()

        self.assertEqual(wdg_grid[2][8].cget('textvariable'), str(var_grid[2][8]))

    def test_start(self):
        app = controll.Application()
        app.root_frame.input_variables[0][0].set('5')
        app._on_start()

        with open('input_grid.pkl', 'rb') as input_file:
            saved_list = data_model.load_data(input_file)

        check_list = [
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertEqual(saved_list, check_list)