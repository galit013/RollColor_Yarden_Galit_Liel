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

    global running
    running = True
    loaded = 0
    game_over = False
    best_score = 0
    global score
    score = 0
    start_blocks = 0
    level = 0
    clock_tick = 60
    # levels = [5, 7, 9, 11]
    start_score = False
    while running:
        click_home_button(screen)



        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(best_score)
                running = False
            # checks if the user pressed the mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click_pos = event.pos

                img = pygame.image.load(BACKGROUND)
                img = pygame.transform.scale(img, (QUESTION_MARK_WIDTH,QUESTION_MARK_HEIGHT))
                screen.blit(img, (QUESTION_MARK_X_POS,QUESTION_MARK_Y_POS))
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
                                             args=(screen, block_list_right, block_list_left, 5, ball, score))
            blocks_thread.start()



        # Updating the score
        if start_score and not display_screen.game_over:
            score += SCORE_CHANGE
            pygame.draw.line(screen, BLACK, [X_START_SCORE_REC, Y_START_SCORE_REC], [X_START_SCORE_REC, Y_END_SCORE_REC], SCORE_REC_WIDTH)
            screen.blit(score_font.render("SCORE:" + str(score), True, WHITE), (X_POS_SCORE, Y_POS_SCORE))
            time.sleep(0.2)
            pygame.display.flip()
            # print(score)
            if score > best_score:
                 best_score = score

            # if score == 200:
            #     level = 1
            #     clock_tick = 150
            #     print("l1")
            # if score == 500:
            #     level = 2
            #     clock_tick = 200
            #     print("l2")
            # if score == 1000:
            #     level = 3
            #     clock_tick = 240
            #     print("l3")

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        pygame.display.flip()
        clock.tick(clock_tick)
    pygame.quit()
    quit()

def click_home_button(screen):
    if display_screen.game_over:
        img = pygame.image.load(GAME_OVER)
        img = pygame.transform.scale(img, (GAME_OVER_WIDTH, GAME_OVER_HEIGHT))
        screen.blit(img, (GAME_OVER_X_POS, GAME_OVER_Y_POS))

        img = pygame.image.load(HOME_BUTTON)
        img = pygame.transform.scale(img, (HOME_BUTTON_WIDTH, HOME_BUTTON_HEIGHT))
        screen.blit(img, (HOME_BUTTON_X_POS, HOME_BUTTON_Y_POS))

        img = pygame.image.load(BACKGROUND)
        img = pygame.transform.scale(img, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        screen.blit(img, (BACKGROUND_X_POS, BACKGROUND_Y_POS))

        score_font = pygame.font.SysFont(SCORE_FONT, SCORE_FONT_SIZE)
        screen.blit(score_font.render("SCORE:" + str(score), True, WHITE), (200, 400))

        home_button = Button(HOME_BUTTON_X_POS, HOME_BUTTON_Y_POS, HOME_BUTTON_HEIGHT, HOME_BUTTON_WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click_pos = event.pos
                if home_button.mouse_in_button(mouse_click_pos):
                    print(0)
                    main()


main()
