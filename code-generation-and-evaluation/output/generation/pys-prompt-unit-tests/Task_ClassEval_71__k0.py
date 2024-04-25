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
        return all(box in self.targets for box in self.boxes)

    def move(self, direction):
        directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction not in directions:
            return False

        dx, dy = directions[direction]
        new_col = self.player_col + dy
        new_row = self.player_row + dx

        if not (0 <= new_row < len(self.map) and 0 <= new_col < len(self.map[0])):
            return False

        if self.map[new_row][new_col] == '#':
            return False

        if (new_row, new_col) in self.boxes:
            new_box_col = new_col + dy
            new_box_row = new_row + dx

            if not (0 <= new_box_row < len(self.map) and 0 <= new_box_col < len(self.map[0])):
                return False

            if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
                return False

            self.boxes.remove((new_row, new_col))
            self.boxes.append((new_box_row, new_box_col))

        self.player_col = new_col
        self.player_row = new_row
        self.is_game_over = self.check_win()

        return True
