import tkinter as tk
import data_model as d
import user_interface as ui
import greedy_sudoku as gs


# TODO: start greedy algorithm from controll.py and return greedy result
# TODO: check validity of greedy result and either close probleme or
# TODO: start GA to search for final solution


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
        self.greedy_solution = ''

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
        # Try greedy solution of sudoku puzzle first
        self.greedy_solution = self.greedy_solver()
        self.root_frame.update_output_variables(self.greedy_solution)

    @staticmethod
    def greedy_solver():
        """Get greedy solution for input data"""
        with open('input_grid.pkl', 'rb') as input_file:
            input_data = d.load_data(input_file)
        greedy_problem = gs.GreedySolver(input_data)
        greedy_problem.solve_sudoku()

        return greedy_problem.get_solution()


if __name__ == "__main__":
    app = Application()
    app.mainloop()