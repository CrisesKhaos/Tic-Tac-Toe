import pygame
import sys
import numpy as np
pygame.init()

WIDTH = 600
HEIGHT = 600
B_ROWS = 3
B_COLS = 3
font = pygame.font.SysFont("comicsansms", 72)
font1 = pygame.font.Font('freesansbold.ttf', 32)
bg_colour = (23, 200, 180)
line_colour = (190, 240, 194)
x_space = 40
x_colour = (110, 100, 100)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(bg_colour)

# board(console)
board = np.zeros((B_ROWS, B_COLS))
bot_board = board


# functions start
def check_win(player1):
    # horizontal check
    for x in range(3):
        if board[x][0] == player1 and board[x][1] == player1 and board[x][2] == player1:

            # drawing winning lines
            if player1 == 1:
                pygame.draw.line(screen, (200, 240, 240),
                                 (20, x*200 + 100), (580, x*200+100), 8)
            else:
                pygame.draw.line(screen, x_colour,
                                 (20, x*200 + 100), (580, x*200+100), 8)
            return True

    # vertical check
    for x in range(3):
        if board[0][x] == player1 and board[1][x] == player1 and board[2][x] == player1:

            # drawing winning lines
            if player1 == 1:
                pygame.draw.line(screen, (200, 240, 240),
                                 (x*200 + 100, 20), (x*200+100, 580), 10)
            else:
                pygame.draw.line(screen, x_colour,
                                 (x*200 + 100, 20), (x*200+100, 580), 10)
            return True

    # leftdiagonal check
    if board[0][0] == player1 and board[2][2] == player1 and board[1][1] == player1:

        # drawing winning lines
        if player1 == 1:
            pygame.draw.line(screen, (200, 240, 240), (20, 20), (580, 580), 10)
        else:
            pygame.draw.line(screen, x_colour, (20, 20), (580, 580), 10)

        return True

    # rightdiagonal checkk
    if board[0][2] == player1 and board[1][1] == player1 and board[2][0] == player1:
        # drawing winning lines
        if player1 == 1:
            pygame.draw.line(screen, (200, 240, 240), (580, 0), (0, 580), 10)
        else:
            pygame.draw.line(screen, x_colour, (580, 20), (20, 580), 10)

        return True


def check_win_bot(player1, row, col):
    # horizontal check

    if bot_board[row][0] == player1 and bot_board[row][1] == player1 and bot_board[row][2] == player1:
        return True

    # vertical check

    if bot_board[0][col] == player1 and bot_board[1][col] == player1 and bot_board[2][col] == player1:
        return True

    # leftdiagonal check
    if bot_board[0][0] == player1 and bot_board[2][2] == player1 and bot_board[1][1] == player1:
        return True

    # rightdiagonal checkk
    if bot_board[0][2] == player1 and bot_board[1][1] == player1 and bot_board[2][0] == player1:
        return True


def draw_line():
    # vertical lines
    pygame.draw.line(screen, line_colour, (200, 0), (200, 600), 10)
    pygame.draw.line(screen, line_colour, (400, 0), (400, 600), 10)
    # horizontal lines
    pygame.draw.line(screen, line_colour, (0, 200), (600, 200), 10)
    pygame.draw.line(screen, line_colour, (0, 400), (600, 400), 10)


def draw_symbols():
    for rws in range(B_ROWS):
        for clms in range(B_COLS):
            if board[rws][clms] == 1:
                pygame.draw.circle(screen, (200, 240, 240), (int(
                    clms * 200 + 100), int(rws * 200 + 100)), 60, 12)
            elif board[rws][clms] == 2:
                pygame.draw.line(screen, x_colour, (clms * 200 + x_space, rws*200 + x_space),
                                 (clms * 200 - x_space + 200, rws * 200 - x_space + 200), 12)
                pygame.draw.line(screen, x_colour, (clms * 200 + 200 - x_space, rws *
                                                    200 + x_space), (clms * 200 + x_space, rws * 200 - x_space + 200), 12)


def mark_box(row,  x, player):
    board[row][x] = player


def is_available(row, x):
    if board[row][x] == 0:
        return True
    else:
        return False


def is_boardfull():
    for rws in range(B_ROWS):
        for clms in range(B_COLS):
            if board[rws][clms] == 0:
                return False
    return True


def restart_game():
    screen.fill(bg_colour)
    draw_line()
    player = 1
    for rws in range(B_ROWS):
        for clms in range(B_COLS):
            board[rws][clms] = 0


def display_font(msg):
    text = font.render(msg, False, (10, 10, 10))
    screen.blit(text, (310 - text.get_width() //
                       2, 290 - text.get_height() // 2, ))
    pygame.display.flip()


def text_continue(msg):
    text = font1.render(msg, False, (10, 10, 10))
    screen.blit(text, (310 - text.get_width() //
                       2, 350 - text.get_height() // 2, ))
    pygame.display.flip()


def bot():
    bot_board = board
    turn_done = False
    for row in range(B_ROWS):
        for col in range(B_COLS):

            if is_available(row, col) and turn_done == False:

                for row1 in range(B_ROWS):
                    for col1 in range(B_COLS):

                        if is_available(row1, col1):

                            bot_board[row1][col1] = 2
                            if check_win_bot(2, row1, col1):
                                mark_box(row1, col1, 2)
                                return

                            bot_board[row1][col1] = 1
                            if check_win_bot(1, row1, col1):
                                mark_box(row1, col1, 2)
                                return
                            bot_board[row1][col1] = 0
                            print(bot_board)

                mark_box(row, col, 2)
                turn_done = True
                bot_board = board
# fuctionsEnd


draw_line()
current_player = 1
game_over = False


# main loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # draw
        if is_boardfull() and game_over == False:
            display_font("Draw")
            text_continue("Press [SPACE] to continue ")

        if event.type == pygame.MOUSEBUTTONDOWN and game_over == False:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            main_row = int(mouse_y / 200)
            main_col = int(mouse_x / 200)

            if is_available(main_row, main_col) == True:

                # 1st player turn
                if current_player == 1:
                    mark_box(main_row, main_col, 1)
                    check_win(current_player)
                    draw_symbols()
                    if check_win(current_player):
                        game_over = True
                        display_font("You Won")
                        text_continue("Press [SPACE] to continue ")

                    # dumbot player turn
                    if game_over == False:
                        current_player = 2
                        bot()  # dunbot maes move
                        check_win(current_player)
                        draw_symbols()
                        if check_win(current_player):
                            game_over = True
                            display_font("You Dum")
                            text_continue("Press [SPACE] to continue ")
                        current_player = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart_game()
                game_over = False

    pygame.display.update()
