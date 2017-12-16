import random


class Graph:
    def __init__(self):
        self.m_data = [[]]

    def create_matrix(self, rows, cols):
        # Create 2D matrix
        self.m_data = [[random.randint(1, 15) for _ in range(cols)] for _ in range(rows)]

    def create_array(self, size):
        self.m_data = [random.randint(1, 5) for _ in range(size)]

    def __repr__(self):

        # Convert data into 2d literal string
        line = [[str(_) for _ in row] for row in self.m_data]

        # Get column-wise max integer digit counts
        max_col_lens = [max(map(len, col)) for col in zip(*line)]

        # Format string by setting unit space per number
        # "{" [field_name] ["!" conversion] [":" format_spec] "}"
        fmt = '\t'.join('{{:{}}}'.format(_) for _ in max_col_lens)

        # Re-format table
        table = [fmt.format(*row) for row in line]

        return '\n'.join(table)
