import sys
import pygame
from tile import Tile
from config import Config as cfg

pygame.init()
screen = pygame.display.set_mode(cfg.SCREEN_SIZE, 0, 32)


def run(tile):
    cmd = 'start'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    cmd = "start"
                if event.key == pygame.K_r:
                    cmd = "restart"
                if event.key == pygame.K_p:
                    cmd = "pause"
                if event.key == pygame.K_q:
                    sys.exit(0)

        tile.draw_tiles()
        if cmd == "restart":
            tile.init_tiles_ants()
            cmd = "start"
        elif cmd == "start":
            tile.step()
        pygame.display.update()


if __name__ == "__main__":
    t = Tile(screen, cfg.ANT_START_POS, init_tiles=cfg.INIT_TILES, show_grid=cfg.SHOW_GRID)
    run(t)
