class GomokuGame:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.moves = []

    def make_move(self, row, col):
        if (row, col) in self.moves:
            return False
        self.moves.append((row, col))
        self.board[row][col] = 'X' if len(self.moves) % 2 == 1 else 'O'
        return True

    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                for d in directions:
                    if self._check_five_in_a_row(row, col, d):
                        return self.board[row][col]
        return None

    def _check_five_in_a_row(self, row, col, direction):
        player = self.board[row][col]
        if player == ' ':
            return False
        for _ in range(4):
            row += direction[0]
            col += direction[1]
            if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size or self.board[row][col] != player:
                return False
        return True
