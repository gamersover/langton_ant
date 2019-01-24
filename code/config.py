import numpy as np


class Config:
    SCREEN_SIZE = (400, 400) # 画布大小
    N_TILES = 10  # 网格行数
    FPS = 10    # FPS
    ANT_INIT_POS = (5, 5)  # 蚂蚁起始位置
    ANT_INIT_DIRECTION = 0
    INIT_TILES = 'random' # 初始网格布置
    SHOW_GRID = True # 是否显示网格线

    # do not recommend edit this params
    WHITE = [255, 255, 255] # 白色
    BLACK = [0, 0, 0]  # 黑色
    RED = [255, 0, 0]  # 红色
    N_DIRECTIONS = 4  # 方向个数


