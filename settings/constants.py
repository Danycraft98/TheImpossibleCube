import os

__all__ = [
    'SCREEN_SIZE', 'ORIGINAL_CAPTION', 'COLOR_KEY', 'BACKGROUND_COLOR', 'FONT_PATH', 'CELL_SIZE',
    'MAX_HEALTH', 'MAX_MONEY', 'DIRECTIONS', 'DIRECT_DICT', 'OPPOSITE_DICT', 'DEFAULT_PLAYER', 'Z_ORDER'
]

SCREEN_SIZE = (1200, 700)
ORIGINAL_CAPTION = "Impossible Cube"
COLOR_KEY = (255, 0, 255)
BACKGROUND_COLOR = (30, 40, 50)
FONT_PATH = os.path.join("static", "fonts", "Fixedsys500c.ttf")

CELL_SIZE = (50, 50)
MAX_HEALTH = 28
MAX_MONEY = 9999

DIRECTIONS = ["front", "back", "left", "right"]

DIRECT_DICT = {
    "front": (0, 1),
    "back": (0, -1),
    "left": (-1, 0),
    "right": (1, 0)
}

OPPOSITE_DICT = {
    "front": "back",
    "back": "front",
    "left": "right",
    "right": "left"
}

DEFAULT_PLAYER = {
    "name": None,
    "world": "overworld.wrl",
    "save_world_coords": (5, 5),
    "start_coord": (12, 4),
    "start_direction": "right",
    "identifiers": {},
    "money": 0,
    "keys": 0,
    "gear": "body"
}

# Draw layer order for all types of items.
Z_ORDER = {
    "BG Tiles": -4,
    "Water": -3,
    "Shadows": -2,
    "Solid": -1,
    "Solid/Fore": 750,
    "Foreground": 800,
    "Projectiles": 850
}
