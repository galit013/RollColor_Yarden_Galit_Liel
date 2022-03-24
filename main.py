import pygame
from constants import *
from App import *
from Player import *
from Block import*


def main():
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
    ball_img = ball.get_player()
    screen.blit(ball_img, (ball.x_pos, ball.y_pos))

    block = Block(screen)

    clock = pygame.time.Clock()

    # Display all drawings we have defined
    pygame.display.flip()


    running = True
    loaded = False
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # checks if the user pressed the mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(1)
                loaded = True

            elif loaded:
                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                    print(2)
                        #ball.move_player_left(ball.x_pos, ball.y_pos)
                        # for i in range(30):
                    screen.blit(ball_img, (ball.x_pos - 150, ball.y_pos))
                if key[pygame.K_RIGHT]:
                    pass





        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
