class EightPuzzle:
    def __init__(self, state):
        self.state = state

    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return None

    def move(self, state, direction):
        blank_row, blank_col = self.find_blank(state)
        new_state = [row[:] for row in state]
        if direction == 'up' and blank_row > 0:
            new_state[blank_row][blank_col], new_state[blank_row - 1][blank_col] = new_state[blank_row - 1][blank_col], new_state[blank_row][blank_col]
        elif direction == 'down' and blank_row < 2:
            new_state[blank_row][blank_col], new_state[blank_row + 1][blank_col] = new_state[blank_row + 1][blank_col], new_state[blank_row][blank_col]
        elif direction == 'left' and blank_col > 0:
            new_state[blank_row][blank_col], new_state[blank_row][blank_col - 1] = new_state[blank_row][blank_col - 1], new_state[blank_row][blank_col]
        elif direction == 'right' and blank_col < 2:
            new_state[blank_row][blank_col], new_state[blank_row][blank_col + 1] = new_state[blank_row][blank_col + 1], new_state[blank_row][blank_col]
        return new_state

    def get_possible_moves(self, state):
        possible_moves = []
        directions = ['up', 'down', 'left', 'right']
        blank_row, blank_col = self.find_blank(state)
        if blank_row > 0:
            possible_moves.append('up')
        if blank_row < 2:
            possible_moves.append('down')
        if blank_col > 0:
            possible_moves.append('left')
        if blank_col < 2:
            possible_moves.append('right')
        return possible_moves

    def solve(self):
        # Implement your solve logic here
        pass
