import sys
import time
import pygame
import numpy as np
from ant import Ant
from config import Config as cfg

fpsclock = pygame.time.Clock()


class Tile:
    def __init__(self, screen, ant_init_pos, ant_init_direction=0, init_tiles=None, show_grid=True):
        self.screen = screen
        self._save_init_state(ant_init_pos, ant_init_direction, init_tiles)
        self.init_tiles_ants()
        self.line_width = 1 if show_grid else 0

    def _save_init_state(self, ant_init_pos, ant_init_direction, init_tiles):
        self.ant_init_pos = ant_init_pos
        self.ant_init_direction = ant_init_direction
        self.init_tiles = init_tiles

    def init_tiles_ants(self):
        self.screen_size = self.screen.get_size()[0]
        self.tile_size = self.screen_size // cfg.N_TILES
        if self.init_tiles is not None:
            self.tiles = self.init_tiles
        else:
            self.tiles = np.zeros((cfg.N_TILES, cfg.N_TILES))

        self.ant = Ant(self.ant_init_pos, self.ant_init_direction)
        self.total_step = 0

    def draw_tiles(self):
        self.screen.fill(cfg.WHITE)

        for i in range(cfg.N_TILES):
            pygame.draw.line(self.screen, cfg.BLACK, (self.tile_size*(i+1), 0), (self.tile_size*(i+1), self.screen_size), self.line_width)
            pygame.draw.line(self.screen, cfg.BLACK, (0, self.tile_size*(i+1)), (self.screen_size, self.tile_size*(i+1)), self.line_width)

        for i in range(cfg.N_TILES):
            for j in range(cfg.N_TILES):
                if self.tiles[i][j] == 1:
                    pygame.draw.rect(self.screen, cfg.BLACK, (i*self.tile_size, j*self.tile_size, self.tile_size, self.tile_size), 0)

        c_dot = self.get_circle()
        pygame.draw.circle(self.screen, cfg.RED, c_dot, self.tile_size//4, 0)
        fpsclock.tick(cfg.FPS)

    def get_circle(self):
        x = self.ant.x * self.tile_size + self.tile_size // 2
        y = self.ant.y * self.tile_size + self.tile_size // 2
        return x, y

    def step(self):
        try:
            m = self.tiles[self.ant.x][self.ant.y]
            self.tiles[self.ant.x][self.ant.y] = 1 - m
            self.ant.change_direction(m)
            self.ant.step()
            self.total_step += 1

        except IndexError as e:
            print("final steps:", self.total_step)
            print("WARNING: Ant position is out of boundary, progrome will shut down in five seconds!")
            print("Or you can push q/esc button to quit!")
            time.sleep(5)
            sys.exit(0)

