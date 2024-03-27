class MinesweeperGame:
    def __init__(self, rows, mines):
        self.rows = rows
        self.cols = rows
        self.mines = mines
        self.score = 0
        self.minesweeper_map = self.generate_mine_sweeper_map()
        self.player_map = self.generate_playerMap()

    def generate_mine_sweeper_map(self):
        import random
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        mine_map = [['0' for _ in range(self.cols)] for _ in range(self.rows)]
        for pos in mine_positions:
            row = pos // self.cols
            col = pos % self.cols
            mine_map[row][col] = 'X'
        return mine_map

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
        self.player_map[row][col] = str(self.get_adjacent_mines(row, col))
        self.score += 1
        return self.player_map

    def get_adjacent_mines(self, row, col):
        count = 0
        for i in range(max(0, row-1), min(row+2, self.rows)):
            for j in range(max(0, col-1), min(col+2, self.cols)):
                if self.minesweeper_map[i][j] == 'X':
                    count += 1
        return count
