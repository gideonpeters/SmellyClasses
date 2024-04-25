class MahjongConnect:
    def __init__(self, board_size, icons):
        self.BOARD_SIZE = board_size
        self.ICONS = icons
        self.board = [[icons[0] for _ in range(board_size[1])] for _ in range(board_size[0])]

    def is_valid_move(self, start_pos, end_pos):
        if not (0 <= start_pos[0] < self.BOARD_SIZE[0] and 0 <= start_pos[1] < self.BOARD_SIZE[1] and
                0 <= end_pos[0] < self.BOARD_SIZE[0] and 0 <= end_pos[1] < self.BOARD_SIZE[1]):
            return False
        if start_pos == end_pos or self.board[start_pos[0]][start_pos[1]] != self.board[end_pos[0]][end_pos[1]]:
            return False
        return True

    def has_path(self, start_pos, end_pos):
        if not self.is_valid_move(start_pos, end_pos):
            return False
        return True

    def remove_icons(self, pos1, pos2):
        if self.is_valid_move(pos1, pos2):
            self.board[pos1[0]][pos1[1]] = ' '
            self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True
