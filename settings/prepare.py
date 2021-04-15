"""
This module initializes the display and creates dictionaries of resources.
Also contained are various constants used throughout the program.
"""

import os

import pygame as pg

from . import tools
from .constants import *

pg.init()

SCREEN_RECT = pg.Rect((0, 0), SCREEN_SIZE)
BIG_FONT = pg.font.Font(FONT_PATH, 100)

# Initialization
_ICON_PATH = os.path.join("static", "images", "misc", "icon.png")
_Y_OFFSET = (pg.display.Info().current_w - SCREEN_SIZE[0]) // 2
os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(_Y_OFFSET, 25)
pg.display.set_caption(ORIGINAL_CAPTION)
pg.display.set_icon(pg.image.load(_ICON_PATH))
_screen = pg.display.set_mode(SCREEN_SIZE)

# Display until loading finishes.
_screen.fill(BACKGROUND_COLOR)
_render = BIG_FONT.render("LOADING...", 0, pg.Color("white"))
_screen.blit(_render, _render.get_rect(center=SCREEN_RECT.center))
pg.display.update()

# General constants
PLAY_RECT = pg.Rect(0, 0, 1000, 700)
DEFAULT_CONTROLS = {
    pg.K_DOWN: "front",
    pg.K_UP: "back",
    pg.K_LEFT: "left",
    pg.K_RIGHT: "right"
}

# Resource loading (Fonts and ost just contain path names).
SAVE_PATH = os.path.join("data", "save_data", "save_data.dat")
FONTS = tools.load_all_fonts(os.path.join("static", "fonts"))
MUSIC = tools.load_all_music(os.path.join("static", "ost"))
SFX = tools.load_all_sfx(os.path.join("static", "ost"))


def graphics_from_directories(directories):
    """
    Calls the tools.load_all_graphics() function for all directories passed.
    """
    base_path = os.path.join("static", "images")
    GFX = {}
    for directory in directories:
        path = os.path.join(base_path, directory)
        GFX[directory] = tools.load_all_gfx(path)
    return GFX


_SUB_DIRECTORIES = ["enemies", "equips", "mapsheets", "misc", "objects"]
GFX = graphics_from_directories(_SUB_DIRECTORIES)
