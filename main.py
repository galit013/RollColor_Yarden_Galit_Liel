import pygame
from constants import *
from App import *
from Player import *
from Block import *
from Button import *
import time
import threading


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
    loaded = 0
    game_over = False
    best_score = 0
    score = 0
    start_blocks = 0
    level = 0
    levels = [5, 30, 120, 200]
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
                # show start score
                score_font = pygame.font.SysFont(SCORE_FONT, SCORE_FONT_SIZE)
                screen.blit(score_font.render("SCORE:", True, WHITE), (X_POS_SCORE, Y_POS_SCORE))
                # build start blocks
                block_right = Block(screen, RED, X_POS_RIGHT_BLOCK, Y_POS_BLOCK, BLOCK_START_HEIGHT)
                block2_right = Block(screen, YELLOW, X_POS_RIGHT_BLOCK, Y_POS_BLOCK2, BLOCK_START_HEIGHT)
                block3_right = Block(screen, RED, X_POS_RIGHT_BLOCK, Y_POS_BLOCK3, BLOCK_START_HEIGHT)
                block_list_right = [block_right, block2_right, block3_right]
                block_left = Block(screen, YELLOW, X_POS_LEFT_BLOCK, Y_POS_BLOCK, BLOCK_START_HEIGHT)
                block2_left = Block(screen, RED, X_POS_LEFT_BLOCK, Y_POS_BLOCK2, BLOCK_START_HEIGHT)
                block3_left = Block(screen, YELLOW, X_POS_LEFT_BLOCK, Y_POS_BLOCK3, BLOCK_START_HEIGHT)
                block_list_left = [block_left, block2_left, block3_left]
                # display start blocks
                display_screen.game_screen(screen, block_list_right)
                display_screen.game_screen(screen, block_list_left)
                pygame.display.flip()

                loaded += 1

            elif loaded == 1:
                start_score = False

                direction = ""
                player_thread = threading.Thread(target=ball.move_player,
                                                 args=(screen, direction))
                player_thread.start()
                pygame.display.flip()

                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                    start_score = True
                    start_blocks += 1
                    ball.move_player(screen, "left")

                if key[pygame.K_RIGHT]:
                    start_score = True
                    start_blocks += 1
                    ball.move_player(screen, "right")

                if start_blocks == 1:
                    blocks_thread = threading.Thread(target=display_screen.move_blocks,
                                                     args=(screen, block_list_right, block_list_left, levels[level])
                                                     , daemon=True)
                    blocks_thread.start()

                # Updating the score based on the keys events
                if start_score:
                    score += SCORE_CHANGE
                    pygame.draw.line(screen, BLACK, [X_START_SCORE_REC, Y_START_SCORE_REC], [X_START_SCORE_REC, Y_END_SCORE_REC], SCORE_REC_WIDTH)
                    screen.blit(score_font.render("SCORE:" + str(score), True, WHITE), (X_POS_SCORE, Y_POS_SCORE))
                    time.sleep(0.2)
                    pygame.display.flip()
                    print(score)
                    if score > best_score:
                        best_score = score
                    if score == 50:
                        level = 1
                        print("l1")
                    if score == 100:
                        level = 2
                        print("l2")
                    if score == 150:
                        level = 3
                        print("l3")
                    if score >= 200 and score % 50 == 0:
                        level += 1
                        if level >= len(levels):
                            length = len(levels) - 1
                            levels.append(levels[length] * 3)
                            print(levels[level])


        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()
    quit()


main()
