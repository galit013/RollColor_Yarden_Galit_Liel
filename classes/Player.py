import pygame
from constants import *


class Player:
    def __init__(self):
        self.x_pos = X_POS_START
        self.y_pos = Y_POS_START
        self.color = RED

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def change_x_pos(self, change_x):
        self.x_pos += change_x

    def move_player(self, screen, direction):
        """
            The function is moving the player based on the direction
            <direction> - string
            :return: None
        """
        clock = pygame.time.Clock()
        loop_times = 0
        x_pos_change = 0
        # check current direction
        if direction == "left":
            # set x_pos_change
            x_pos_change = X_POS_CHANGE_LEFT
            # set loop_times based on players position
            if self.get_x_pos() == X_POS_LEFTEST:
                loop_times = CANT_MOVE_LOOP_TIMES
            elif self.get_x_pos() == X_POS_START:
                loop_times = START_MOVE_LEFT_LOOP_TIMES
            else:
                loop_times = MOVE_LOOP_TIMES
        elif direction == "right":
            # set x_pos_change
            x_pos_change = X_POS_CHANGE_RIGHT
            # set loop_times based on players position
            if self.get_x_pos() == X_POS_RIGHTEST:
                loop_times = CANT_MOVE_LOOP_TIMES
            elif self.get_x_pos() == X_POS_START:
                loop_times = START_MOVE_RIGHT_LOOP_TIMES
            else:
                loop_times = MOVE_LOOP_TIMES

        # move the player
        for i in range(loop_times):
            # hide this ball
            pygame.draw.circle(screen, BLACK, (self.get_x_pos(), self.get_y_pos()), RADIUS)
            # change ball's position
            self.change_x_pos(x_pos_change)
            # draw a new ball in the new position
            pygame.draw.circle(screen, self.get_color(), (self.get_x_pos(), self.get_y_pos()), RADIUS)
            # update the screen
            pygame.display.flip()
            clock.tick(120)



