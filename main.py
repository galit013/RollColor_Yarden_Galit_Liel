from classes.App import *
from classes.Block import *
from classes.Button import *
from helpers import *
import time
import threading
from os import path


def main():
    """
        The function checks when the game will end.
        In addition, the function checks the mouse click events and key events
        :return: None
    """
    # Set up the game display, clock and headline
    pygame.init()
    # Create the screen and show it
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    # Change the title of the window
    pygame.display.set_caption('RollColor')

    global score
    score = 0
    start_score = False

    # create player
    ball = Player()
    # create display screen
    global display_screen
    display_screen = App(screen, ball, score)

    show_img(screen, GARFIELD, GARFIELD_WIDTH, GARFIELD_HEIGHT, GARFIELD_X_POS, GARFIELD_Y_POS)

    # clock


    clock = pygame.time.Clock()

    # Display all drawings we have defined
    pygame.display.flip()

    # define score font
    global score_font
    score_font = pygame.font.SysFont(SCORE_FONT, SCORE_FONT_SIZE)

    # main loop variables
    running = True

    loaded = 0
    best_score = 0
    start_blocks = 0
    change = False



    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            # checks if the user quited the game
            if event.type == pygame.QUIT:
                running = False
            # checks if the user pressed the mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # show start score
                show_img(screen, "images/blackBackground.png", GARFIELD_WIDTH, GARFIELD_HEIGHT, GARFIELD_X_POS, GARFIELD_Y_POS)
                show_text(screen, score_font, "SCORE: 0", WHITE, X_POS_SCORE, Y_POS_SCORE)

                # build start blocks
                block_right = Block(RED, X_POS_RIGHT_BLOCK, Y_POS_BLOCK, BLOCK_START_HEIGHT)
                block2_right = Block(YELLOW, X_POS_RIGHT_BLOCK, Y_POS_BLOCK2, BLOCK_START_HEIGHT)
                block3_right = Block(RED, X_POS_RIGHT_BLOCK, Y_POS_BLOCK3, BLOCK_START_HEIGHT)
                block_list_right = [block_right, block2_right, block3_right]
                block_left = Block(YELLOW, X_POS_LEFT_BLOCK, Y_POS_BLOCK, BLOCK_START_HEIGHT)
                block2_left = Block(RED, X_POS_LEFT_BLOCK, Y_POS_BLOCK2, BLOCK_START_HEIGHT)
                block3_left = Block(YELLOW, X_POS_LEFT_BLOCK, Y_POS_BLOCK3, BLOCK_START_HEIGHT)
                block_list_left = [block_left, block2_left, block3_left]
                # display start blocks
                display_screen.game_screen(screen, block_list_right)
                display_screen.game_screen(screen, block_list_left)
                # update screen
                pygame.display.flip()
                # change var - loaded to start player movements by key events
                loaded += 1

            # checks if the player can start moving
            elif loaded == 1:
                # create move player thread
                direction = ""
                player_thread = threading.Thread(target=ball.move_player,
                                                 args=(screen, direction))
                # start player thread
                player_thread.start()

                # checks key events
                key = pygame.key.get_pressed()
                # checks if left arrow key was pressed
                if key[pygame.K_LEFT]:
                    # start score and blocks movement
                    start_score = True
                    start_blocks += 1
                    # move the ball to the left
                    ball.move_player(screen, "left")
                    if change:
                        print("touched")
                        change_players_color(ball)
                        change = False

                    # if display_screen.draw_change_color(ball):
                    #     print("111")
                    #     if ball.get_x_pos() == X_POS_LEFTEST:
                    #         print("l")
                    #         change_players_color(ball)

                # checks if right arrow key was pressed
                if key[pygame.K_RIGHT]:
                    # start score and blocks movement
                    start_score = True
                    start_blocks += 1
                    # move the ball to the right
                    ball.move_player(screen, "right")
                    if change:
                        print("touched")
                        change_players_color(ball)
                        change = False
                    # if display_screen.draw_change_color(ball):
                    #     print("111")
                    #     if ball.get_x_pos() == X_POS_RIGHTEST:
                    #         print("r")
                    #         change_players_color(ball)

                random_drawing = random.randint(0, 2)

                change_color_x = 0
                if random_drawing == 0 and start_blocks >= 1:
                    change_color_ball = Player()
                    display_screen.draw_change_color(ball, change_color_ball)
                    print(change_color_ball.get_x_pos())
                    print(0)
                    print(ball.get_x_pos())
                    change  = True
                    # if change_color_ball.get_x_pos() == ball.get_x_pos():
                    #     print("touched")


                # if random_drawing == 0 and change_color_ball.get_x_pos() == ball.get_x_pos():
                #     print("touched")


                    # if ball.get_x_pos() == x:
                    #     print("r")
                    #     change_players_color(ball)


        # checks if the blocks can start moving (only once the player pressed an arrow key)
        if start_blocks == 1:
            # create move blocks thread
            blocks_thread = threading.Thread(target=display_screen.move_blocks,
                                             args=(screen, block_list_right, block_list_left, Y_POS_CHANGE, ball))
            # start blocks thread
            blocks_thread.start()

        # Updating the score
        if start_score and not display_screen.game_over:
            score += SCORE_CHANGE
            # show current score on the screen
            pygame.draw.line(screen, BLACK, [X_START_SCORE_REC, Y_START_SCORE_REC],
                             [X_START_SCORE_REC, Y_END_SCORE_REC], SCORE_REC_WIDTH)
            show_text(screen, score_font, "SCORE: " + str(score), WHITE, X_POS_SCORE, Y_POS_SCORE)
            time.sleep(0.2)
            App(screen, ball, score)
            # update the screen
            pygame.display.flip()
            if score > display_screen.get_high_score():
                display_screen.set_high_score(score)

        # checks if the game is over
        if display_screen.game_over:
            # loads game over screen
            game_over_screen(screen)

            # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def game_over_screen(screen):
    """
        The function loads the game over screen.
        In addition, the function checks if the home button was clicked.
        :return: None
    """

    # show game over screen images
    show_img(screen, BACKGROUND, BACKGROUND_WIDTH, BACKGROUND_HEIGHT, BACKGROUND_X_POS, BACKGROUND_Y_POS)
    show_img(screen, GAME_OVER, GAME_OVER_WIDTH, GAME_OVER_HEIGHT, GAME_OVER_X_POS, GAME_OVER_Y_POS)
    show_img(screen, HOME_BUTTON, HOME_BUTTON_WIDTH, HOME_BUTTON_HEIGHT, HOME_BUTTON_X_POS, HOME_BUTTON_Y_POS)
    # create home button
    home_button = Button(HOME_BUTTON_X_POS, HOME_BUTTON_Y_POS, HOME_BUTTON_WIDTH, HOME_BUTTON_HEIGHT)
    # show current game's score and best score so far
    show_text(screen, score_font, "SCORE: " + str(score), WHITE, GAME_OVER_X_POS_SCORE, GAME_OVER_Y_POS_SCORE)
    show_text(screen, score_font, "HIGH SCORE: " + str(display_screen.get_high_score()), WHITE, GAME_OVER_X_POS_SCORE, GAME_OVER_Y_POS_SCORE + 50)

    # checks if the home button was clicked
    if click_home_button(home_button):
        # returns to the main screen
        main()


main()
