import unittest
import user_interface
import tkinter


class TestFrontend(unittest.TestCase):

    def test_grid_hook(self):
        app = tkinter.Tk()
        sub_frame = user_interface.SudokuSubFrame(app, 'input')
        var_grid = sub_frame.get_variable_grid()
        wdg_grid = sub_frame.get_widget_grid()

        self.assertEqual(wdg_grid[2][8].cget('textvariable'), str(var_grid[2][8]))