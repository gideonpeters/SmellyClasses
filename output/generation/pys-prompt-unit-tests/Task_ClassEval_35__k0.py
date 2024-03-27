import unittest

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
        i, j = self.find_blank(state)
        if direction == 'up' and i > 0:
            state[i][j], state[i-1][j] = state[i-1][j], state[i][j]
        elif direction == 'down' and i < 2:
            state[i][j], state[i+1][j] = state[i+1][j], state[i][j]
        elif direction == 'left' and j > 0:
            state[i][j], state[i][j-1] = state[i][j-1], state[i][j]
        elif direction == 'right' and j < 2:
            state[i][j], state[i][j+1] = state[i][j+1], state[i][j]
        return state

    def get_possible_moves(self, state):
        moves = []
        i, j = self.find_blank(state)
        if i > 0:
            moves.append('up')
        if i < 2:
            moves.append('down')
        if j > 0:
            moves.append('left')
        if j < 2:
            moves.append('right')
        return moves

    def solve(self):
        # Implement puzzle solving algorithm here
        return None

if __name__ == '__main__':
    unittest.main()
