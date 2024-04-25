class MinesweeperGame:
    def __init__(self, rows, mines):
        self.rows = rows
        self.cols = rows
        self.mines = mines
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()
        self.score = 0

    def generate_mine_sweeper_map(self):
        import random
        minesweeper_map = [['0' for _ in range(self.cols)] for _ in range(self.rows)]
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in mine_positions:
            row = pos // self.cols
            col = pos % self.cols
            minesweeper_map[row][col] = 'X'
        return minesweeper_map

    def generate_playerMap(self):
        return [['-' for _ in range(self.cols)] for _ in range(self.rows)]

    def check_won(self, player_map):
        for i in range(self.rows):
            for j in range(self.cols):
                if player_map[i][j] == '-' and self.minesweeper_map[i][j] != 'X':
                    return False
        return True

    def sweep(self, row, col):
        if self.minesweeper_map[row][col] == 'X':
            return False
        self.player_map[row][col] = self.minesweeper_map[row][col]
        self.score += 1
        return self.player_map
