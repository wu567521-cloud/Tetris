import random
from enum import Enum, auto
import pygame

# 1. 定義方塊類型
class BlockType(Enum):
    EMPTY = auto()   # 空格
    NORMAL = auto()  # 一般方塊
    RIVET = auto()   # 卯釘方塊（固定後不掉落）
    SAND = auto()    # 流沙方塊（下方有空位就補進去）

# 2. 七種經典方塊形狀與顏色
SHAPES = {
    'I': [(0, 1), (1, 1), (2, 1), (3, 1)],
    'O': [(1, 0), (2, 0), (1, 1), (2, 1)],
    'T': [(1, 0), (0, 1), (1, 1), (2, 1)],
    'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
    'J': [(0, 0), (0, 1), (1, 1), (2, 1)],
    'L': [(2, 0), (0, 1), (1, 1), (2, 1)],
}

COLORS = {
    'I': (0, 240, 240),
    'O': (240, 240, 0),
    'T': (160, 0, 240),
    'S': (0, 240, 0),
    'Z': (240, 0, 0),
    'J': (0, 0, 240),
    'L': (240, 160, 0),
}

# 3. 建立空白地圖（給主程式初始化用）
def create_empty_grid(rows: int = 20, cols: int = 10) -> list[list[dict]]:
    return [[{"type": BlockType.EMPTY, "color": (0, 0, 0)} for _ in range(cols)] for _ in range(rows)]

# 4. 生成新方塊函式（包含特殊屬性）
def create_tetromino(special_chance: float = 0.4) -> dict:
    shape_key = random.choice(list(SHAPES.keys()))
    coords = SHAPES[shape_key]
    base_color = COLORS[shape_key]
    
    # 預設 4 格都是一般方塊
    block_types = [BlockType.NORMAL] * len(coords)
    
    # 依機率將其中 1 格變成卯釘或流沙
    if random.random() < special_chance:
        target_index = random.randint(0, len(coords) - 1)
        block_types[target_index] = random.choice([BlockType.RIVET, BlockType.SAND])

    return {
        "x": 3,
        "y": 0,
        "shape": coords,
        "color": base_color,
        "types": block_types
    }

# 5. 將方塊鎖定寫入地圖
def lock_piece_to_grid(piece: dict, grid: list[list[dict]]):
    for i, (dx, dy) in enumerate(piece["shape"]):
        gx = piece["x"] + dx
        gy = piece["y"] + dy
        if 0 <= gy < len(grid) and 0 <= gx < len(grid[0]):
            grid[gy][gx] = {
                "type": piece["types"][i],
                "color": piece["color"]
            }

# 6. 處理消除、卯釘定住與流沙掉落
def apply_gravity_and_clear(grid: list[list[dict]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    total_cleared = 0

    while True:
        cleared_in_pass = 0
        # 由下往上檢查整排消除
        for y in range(rows - 1, -1, -1):
            if all(cell["type"] != BlockType.EMPTY for cell in grid[y]):
                cleared_in_pass += 1
                for x in range(cols):
                    grid[y][x] = {"type": BlockType.EMPTY, "color": (0, 0, 0)}
                _pull_down_above(grid, y)

        total_cleared += cleared_in_pass

        # 處理流沙方塊往下補位（由下往上掃描）
        sand_moved = False
        for y in range(rows - 2, -1, -1):
            for x in range(cols):
                if grid[y][x]["type"] == BlockType.SAND:
                    target_y = y
                    while target_y + 1 < rows and grid[target_y + 1][x]["type"] == BlockType.EMPTY:
                        target_y += 1
                    if target_y != y:
                        grid[target_y][x] = grid[y][x]
                        grid[y][x] = {"type": BlockType.EMPTY, "color": (0, 0, 0)}
                        sand_moved = True

        if cleared_in_pass == 0 and not sand_moved:
            break

    return total_cleared

def _pull_down_above(grid: list[list[dict]], cleared_y: int):
    cols = len(grid[0])
    for x in range(cols):
        for y in range(cleared_y, 0, -1):
            # 遇到卯釘方塊直接跳過，它不會往下掉
            if grid[y][x]["type"] == BlockType.RIVET:
                continue
            
            above_y = y - 1
            while above_y >= 0 and grid[above_y][x]["type"] == BlockType.RIVET:
                above_y -= 1
            
            if above_y >= 0:
                grid[y][x] = grid[above_y][x]
                grid[above_y][x] = {"type": BlockType.EMPTY, "color": (0, 0, 0)}
            else:
                grid[y][x] = {"type": BlockType.EMPTY, "color": (0, 0, 0)}

# 7. 繪製單一格子（包含卯釘與流沙的特殊圖案）
def draw_cell(surface: pygame.Surface, px: int, py: int, cell_size: int, color: tuple, b_type: BlockType):
    rect = pygame.Rect(px, py, cell_size, cell_size)
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, (30, 30, 30), rect, 1)

    if b_type == BlockType.RIVET:
        # 卯釘：四角畫灰色圓點
        r = max(2, cell_size // 10)
        m = cell_size // 5
        for cx, cy in [(px+m, py+m), (px+cell_size-m, py+m), (px+m, py+cell_size-m), (px+cell_size-m, py+cell_size-m)]:
            pygame.draw.circle(surface, (80, 80, 80), (cx, cy), r)
    elif b_type == BlockType.SAND:
        # 流沙：中間畫淺色沙粒
        r = max(2, cell_size // 12)
        cx, cy = px + cell_size // 2, py + cell_size // 2
        for dx, dy in [(-4, -3), (4, -2), (0, 3), (-3, 4)]:
            pygame.draw.circle(surface, (255, 255, 220), (cx + dx, cy + dy), r)

# 8. 繪製正在下落的方塊
def draw_piece(surface: pygame.Surface, piece: dict, cell_size: int, offset_x: int, offset_y: int):
    for i, (dx, dy) in enumerate(piece["shape"]):
        px = offset_x + (piece["x"] + dx) * cell_size
        py = offset_y + (piece["y"] + dy) * cell_size
        draw_cell(surface, px, py, cell_size, piece["color"], piece["types"][i])
