class PushBoxGame:
    def __init__(self, game_map):
        self.map = game_map
        self.is_game_over = False
        self.player_col = 1
        self.player_row = 1
        self.targets = [(row, col) for row in range(len(game_map)) for col in range(len(game_map[0])) if game_map[row][col] == 'G']
        self.boxes = [(row, col) for row in range(len(game_map)) for col in range(len(game_map[0])) if game_map[row][col] == 'X']
        self.target_count = len(self.targets)

    def check_win(self):
        for target in self.targets:
            if target not in self.boxes:
                return False
        return True

    def move(self, direction):
        directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction not in directions:
            return False

        dx, dy = directions[direction]
        new_col = self.player_col + dx
        new_row = self.player_row + dy

        if not (0 <= new_row < len(self.map) and 0 <= new_col < len(self.map[0])):
            return False

        if self.map[new_row][new_col] == '#':
            return False

        if (new_row, new_col) in self.boxes:
            box_new_row = new_row + dx
            box_new_col = new_col + dy

            if not (0 <= box_new_row < len(self.map) and 0 <= box_new_col < len(self.map[0])):
                return False

            if self.map[box_new_row][box_new_col] == '#' or (box_new_row, box_new_col) in self.boxes:
                return False

            self.boxes.remove((new_row, new_col))
            self.boxes.append((box_new_row, box_new_col))

        self.player_row = new_row
        self.player_col = new_col

        if self.check_win():
            self.is_game_over = True

        return True
