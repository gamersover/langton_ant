from config import Config as cfg


class Ant:
    def __init__(self, pos, direction):
        self.x = pos[0]
        self.y = pos[1]
        self.direction = direction

    def step(self):
        if self.direction == 0:
            self.step_left()
        elif self.direction == 2:
            self.step_right()
        elif self.direction == 1:
            self.step_up()
        elif self.direction == 3:
            self.step_down()

    def step_left(self):
        self.x -= 1

    def step_right(self):
        self.x += 1

    def step_up(self):
        self.y -= 1

    def step_down(self):
        self.y += 1

    def change_direction(self, how):
        if how == 0:
            self.direction = (self.direction + 1) % cfg.N_DIRECTIONS
        else:
            self.direction = (self.direction - 1 + cfg.N_DIRECTIONS) % cfg.N_DIRECTIONS
