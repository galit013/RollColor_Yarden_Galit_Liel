import pygame
from constants import *
from App import *
from Player import *
from Block import *
from Button import *
import time


def main():
    # Set up the game display, clock and headline
    pygame.init()
    # Create the screen and show it
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    # Change the title of the window
    pygame.display.set_caption('RollColor')

    img = pygame.image.load(QUESTION_MARK)
    img = pygame.transform.scale(img, (QUESTION_MARK_WIDTH,QUESTION_MARK_HEIGHT))
    screen.blit(img, (QUESTION_MARK_X_POS,QUESTION_MARK_Y_POS))

    question_mark=Button(QUESTION_MARK_X_POS,QUESTION_MARK_Y_POS,QUESTION_MARK_HEIGHT,QUESTION_MARK_WIDTH)



    ball = Player(screen)
    global display_screen
    display_screen = App(screen)
    # ball_img = ball.get_player()
    # screen.blit(ball_img, (ball.x_pos, ball.y_pos))

    # block = Block(screen)

    clock = pygame.time.Clock()

    # Display all drawings we have defined
    pygame.display.flip()

    running = True
    loaded = False
    game_over = False
    best_score = 0
    score = 0
    while running:

        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(best_score)
                running = False
            # checks if the user pressed the mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click_pos = event.pos
                if question_mark.mouse_in_button(mouse_click_pos):
                    print(6)
                print(1)
                block_right = Block(screen, RED, 419, 340, 250)
                block2_right = Block(screen, YELLOW, 419, 340 - 250, 250)
                block3_right = Block(screen, RED, 419, 340 - 500, 250)
                block_list_right = [block_right, block2_right, block3_right]
                block_left = Block(screen, YELLOW, 79, 340, 250)
                block2_left = Block(screen, RED, 79, 340 - 250, 250)
                block3_left = Block(screen, YELLOW, 79, 340 - 500, 250)
                block_list_left = [block_left, block2_left, block3_left]
                display_screen.game_screen(screen, block_list_right)
                display_screen.game_screen(screen, block_list_left)
                pygame.display.flip()

                loaded = True

            elif loaded:
                start_score = False
                # block.move_block(screen)
                display_screen.move_block_list_right(screen, block_list_right)
                display_screen.move_block_list_left(screen, block_list_left)
                pygame.display.flip()
                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                    ball.move_player_left(screen)
                    start_score = True

                if key[pygame.K_RIGHT]:
                    ball.move_player_right(screen)
                    start_score = True
                # Updating the score based on the keys events
                if start_score:
                    score += 10
                    time.sleep(0.2)
                    print(score)
                    if score > best_score:
                        best_score = score
                    # while running:
                    #     score += 10
                    #     time.sleep(0.2)
                    #     game_over = True
                    #     break
                        # print(score)
                # # Saving the last score as the best

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    quit()


main()
