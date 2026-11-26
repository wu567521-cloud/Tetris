import random
import pygame
# import 引用 方塊類型

pygame.init()

CELL = 30
COLS, ROWS = 10, 20
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL


# 建立方塊與初始位置
def new_piece():
    shape_id = random.randrange(len(SHAPES))
    matrix = [[cell == "#" for cell in row] for row in SHAPES[shape_id]]
    return {"matrix": matrix, "x": 3, "y": 0, "color": COLORS[shape_id]}
# 檢查方塊能否移動
def fits(matrix, x, y, board):
    for row, line in enumerate(matrix):
        for col, filled in enumerate(line):
            if not filled:
                continue
            px, py = x + col, y + row
            if px < 0 or px >= COLS or py >= ROWS:
                return False
            if py >= 0 and board[py][px] is not None:
                return False
    return True

board = [[None for _ in range(COLS)] for _ in range(ROWS)]
score = 0
game_over = False

# 下落速度與計時初始化
piece = new_piece()
last_drop = pygame.time.get_ticks()

# 遊戲迴圈中：分數越高，下落越快
now = pygame.time.get_ticks()
drop_delay = max(100, 500 - score // 100 * 25)
# 自動下落，以及落地後固定方塊
if not game_over and now - last_drop >= drop_delay:
    if fits(piece["matrix"], piece["x"], piece["y"] + 1, board):
        piece["y"] += 1
    else:
        for row, line in enumerate(piece["matrix"]):
            for col, filled in enumerate(line):
                if filled:
                    x, y = piece["x"] + col, piece["y"] + row
                    if y < 0:
                        game_over = True
                    else:
                        board[y][x] = piece["color"]

        full_rows = [
            y for y in range(ROWS)
            if all(board[y][x] is not None for x in range(COLS))
        ]
        for y in full_rows:
            del board[y]
            board.insert(0, [None for _ in range(COLS)])

        score += len(full_rows) * 100
        piece = new_piece()
        if not fits(piece["matrix"], piece["x"], piece["y"], board):
            game_over = True

    last_drop = now