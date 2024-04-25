class Snake:
    def __init__(self, screen_width, screen_height, block_size, start_position):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.positions = [start_position]
        self.length = 1
        self.score = 0
        self.food_position = start_position

    def move(self, direction):
        x, y = self.positions[0]
        new_x = x + direction[0]
        new_y = y + direction[1]
        self.positions.insert(0, (new_x, new_y))
        if (new_x, new_y) == self.food_position:
            self.eat_food()
        else:
            self.positions.pop()
        self.score += 100

    def random_food_position(self):
        import random
        while True:
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            if (x, y) not in self.positions:
                self.food_position = (x, y)
                break

    def reset(self):
        self.positions = [(50, 50)]
        self.length = 1
        self.score = 0

    def eat_food(self):
        self.length += 1
        self.score += self.length * 100