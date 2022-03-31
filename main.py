import pygame
from constants import *
from App import *
from Player import *
from Block import*
import time


def main():
    score = 0
    # Set up the game display, clock and headline
    pygame.init()
    # Create the screen and show it
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    # Change the title of the window
    pygame.display.set_caption('RollColor')

    ball = Player(screen)
    global display_screen
    display_screen = App(screen)
    # ball_img = ball.get_player()
    # screen.blit(ball_img, (ball.x_pos, ball.y_pos))

    #Block(screen, YELLOW, 480, 0, 20, 250)
   # block = Block(screen, RED, 0, 0, 20, 300)
    #block = Block(screen, RED, 480, 250, 20, 250)
   # Block(screen, YELLOW,  0, 300, 20, 200


    clock = pygame.time.Clock()

    # Display all drawings we have defined
    pygame.display.flip()

    running = True
    loaded = False
    global game_over
    game_over = False
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # checks if the user pressed the mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                loaded = True

            elif loaded:
                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                    ball.move_player_left(screen)

                if key[pygame.K_RIGHT]:
                    ball.move_player_right(screen)

                while key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
                    score += 10
                    time.sleep(0.2)
                    print(score)
                    game_over = True
                    break
                best_score = score


            # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
