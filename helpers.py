import pygame
from constants import *
from Player import *


def check_game_over(block_right, block_left, player_x_pos, player_y_pos, players_color):
    if player_x_pos == X_POS_RIGHTEST and ((block_right.get_y_pos() + block_right.get_height()) >= player_y_pos >= block_right.get_y_pos()):
        if players_color != block_right.get_color():
            return True
        else:
            return False
    if player_x_pos == X_POS_LEFTEST and ((block_left.get_y_pos() + block_left.get_height()) >= player_y_pos >= block_left.get_y_pos()):
        if players_color != block_left.get_color():
            return True
        else:
            return False
    else:
        return False