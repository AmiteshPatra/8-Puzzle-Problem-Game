# Import ------------------------------------------------------------------------------------------------------------
import pygame
import sys
import random
import time






# Initialize ---------------------------------------------------------------------------------------------------------
# pygame
pygame.init()
clock = pygame.time.Clock()

# screen
screen_width, screen_height = ( 800, 600)
bg_color = ( 45, 168, 216)
pygame.display.set_caption( "8 Puzzle Problem")
screen = pygame.display.set_mode( ( screen_width, screen_height))
fps = 60

# misc
tile_size = 25
draw_rect = False
board_size = 3
difficulty = 3
won = False

# tile positions
tile_pos = [
            [
                (  2 * tile_size + 9, 5 * tile_size + 9),
                (  8 * tile_size + 4, 5 * tile_size + 9),
                ( 14 * tile_size - 2, 5 * tile_size + 9),
            ],
            [
                (  2 * tile_size + 9, 11 * tile_size + 3),
                (  8 * tile_size + 4, 11 * tile_size + 3),
                ( 14 * tile_size - 2, 11 * tile_size + 3),
            ],
            [
                (  2 * tile_size + 9, 17 * tile_size - 3),
                (  8 * tile_size + 4, 17 * tile_size - 3),
                ( 14 * tile_size - 2, 17 * tile_size - 3)
            ]
]

tile_pos_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]

blank_tile_pos = [2, 2]
blank_tile_moves = []

tile_sol_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]







# Classes ------------------------------------------------------------------------------------------------------------
class Button():
    def __init__( self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x - 150
        self.rect.y = y - 70
        self.clicked = False

    def draw( self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint( pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        screen.blit( self.image, self.rect)
        if draw_rect:
            pygame.draw.rect( screen, ( 255, 255, 255), self.rect, 4)

        return action





# Fuctions ------------------------------------------------------------------------------------------------------------
def drawGrid():
    for line in range( 0, 60):
        pygame.draw.line( screen, ( 255, 255, 255), ( 0, line * tile_size), ( screen_width, line * tile_size))
        pygame.draw.line( screen, ( 255, 255, 255), ( line * tile_size, 0), ( line * tile_size, screen_width))
    for line in range( 0, 10):
        pygame.draw.line( screen, ( 0, 0, 0), ( 0, line * tile_size * 4), ( screen_width, line * tile_size * 4), 5)
        pygame.draw.line (screen, ( 0, 0, 0), ( line * tile_size * 4, 0), ( line * tile_size * 4, screen_width), 5)



def draw_tiles( tile_pos_matrix):
    for i in range( board_size):
        for j in range( board_size):

            if tile_pos_matrix[i][j] == 0:
                screen.blit( tile_0_img, tile_pos[i][j])
                
            if tile_pos_matrix[i][j] == 1:
                screen.blit( tile_1_img, tile_pos[i][j])

            if tile_pos_matrix[i][j] == 2:
                screen.blit( tile_2_img, tile_pos[i][j])

            if tile_pos_matrix[i][j] == 3:
                screen.blit( tile_3_img, tile_pos[i][j])

            if tile_pos_matrix[i][j] == 4:
                screen.blit( tile_4_img, tile_pos[i][j])

            if tile_pos_matrix[i][j] == 5:
                screen.blit( tile_5_img, tile_pos[i][j])

            if tile_pos_matrix[i][j] == 6:
                screen.blit( tile_6_img, tile_pos[i][j])

            if tile_pos_matrix[i][j] == 7:
                screen.blit( tile_7_img, tile_pos[i][j])

            if tile_pos_matrix[i][j] == 8:
                screen.blit( tile_8_img, tile_pos[i][j])



def move_tile( direction, blank_tile_pos):
    i, j = blank_tile_pos
    moved = False

    if direction == "up":
        if i > 0:
            tile_pos_matrix[i][j], tile_pos_matrix[i - 1][j] = tile_pos_matrix[i - 1][j], tile_pos_matrix[i][j]
            blank_tile_pos = [i - 1, j]
            moved = True

    if direction == "down":
        if i < 2:
            tile_pos_matrix[i][j], tile_pos_matrix[i + 1][j] = tile_pos_matrix[i + 1][j], tile_pos_matrix[i][j]
            blank_tile_pos = [i + 1, j]
            moved = True

    if direction == "left":
        if j > 0:
            tile_pos_matrix[i][j], tile_pos_matrix[i][j - 1] = tile_pos_matrix[i][j - 1], tile_pos_matrix[i][j]
            blank_tile_pos = [i, j - 1]
            moved = True

    if direction == "right":
        if j < 2:
            tile_pos_matrix[i][j], tile_pos_matrix[i][j + 1] = tile_pos_matrix[i][j + 1], tile_pos_matrix[i][j]
            blank_tile_pos = [i, j + 1]
            moved = True

    return blank_tile_pos



def check_won( tile_sol_matrix, tile_pos_matrix):
    if tile_sol_matrix == tile_pos_matrix:
        return True
    return False



def shuffle_board(blank_tile_pos):
    turns = difficulty * 5
    moves = [ "up", "down", "left", "right"]
    last_move = ""
    i = 0
    blank_tile_moves = []
    while i < turns:
        curr_move = random.choice(moves)
        if not check_move_good(last_move, curr_move) or not movable(curr_move, blank_tile_pos):
            continue
        blank_tile_pos = move_tile( curr_move, blank_tile_pos)
        blank_tile_moves.append(curr_move)
        last_move = curr_move
        i += 1

    return blank_tile_pos, blank_tile_moves



def check_move_good( last_move, curr_move):
    if last_move == "up" and curr_move == "down":
        return False
    elif last_move == "down" and curr_move == "up":
        return False
    elif last_move == "left" and curr_move == "right":
        return False
    elif last_move == "right" and curr_move == "left":
        return False
    
    return True

def movable(move, blank_tile_pos):
    i, j = blank_tile_pos

    if move == "up" and i == 0:
        return False
    elif move == "down" and i == 2:
        return False
    elif move == "right" and j == 2:
        return False
    elif move == "left" and j == 0:
        return False
    
    return True

def solve_board( blank_tile_pos):
    for move in reversed( blank_tile_moves):
        if move == "up":
            blank_tile_pos = move_tile( "down", blank_tile_pos)
            redraw_window()
            pygame.display.update()
            pygame.time.delay(300)
        elif move == "down":
            blank_tile_pos = move_tile( "up", blank_tile_pos)
            redraw_window()
            pygame.display.update()
            pygame.time.delay(300)
        elif move == "right":
            blank_tile_pos = move_tile( "left", blank_tile_pos)
            redraw_window()
            pygame.display.update()
            pygame.time.delay(300)
        elif move == "left":
            blank_tile_pos = move_tile( "right", blank_tile_pos)
            redraw_window()
            pygame.display.update()
            pygame.time.delay(300)

    return blank_tile_pos

def redraw_window():
    screen.fill( bg_color)
    screen.blit( logo_img, ( screen_width // 2 - 9.5 * tile_size, 0))
    screen.blit( board_img, (2 * tile_size, 5 * tile_size))
    draw_tiles( tile_pos_matrix)
    new_game_btn.draw()
    solution_btn.draw()

    







# Load Assets ------------------------------------------------------------------------------------------------------------
# ui img
logo_img = pygame.image.load( 'assets/img/logo.png')
fade_img = pygame.image.load( 'assets/img/fade.png')
you_won_img = pygame.image.load( 'assets/img/you_won.png')

# btn img
new_game_btn     = pygame.image.load( 'assets/btn/new_game.png')
solution_btn     = pygame.image.load( 'assets/btn/solution.png')

# board img
board_img  = pygame.image.load( 'assets/img/board.png')
tile_0_img = pygame.image.load( 'assets/img/tile_0.png')
tile_1_img = pygame.image.load( 'assets/img/tile_1.png')
tile_2_img = pygame.image.load( 'assets/img/tile_2.png')
tile_3_img = pygame.image.load( 'assets/img/tile_3.png')
tile_4_img = pygame.image.load( 'assets/img/tile_4.png')
tile_5_img = pygame.image.load( 'assets/img/tile_5.png')
tile_6_img = pygame.image.load( 'assets/img/tile_6.png')
tile_7_img = pygame.image.load( 'assets/img/tile_7.png')
tile_8_img = pygame.image.load( 'assets/img/tile_8.png')

# btn
new_game_btn = Button( 27.5 * tile_size, 12 * tile_size, new_game_btn)
solution_btn = Button( 27.5 * tile_size, 18 * tile_size, solution_btn)






# Game Loop ------------------------------------------------------------------------------------------------------------
# init once
blank_tile_pos, blank_tile_moves = shuffle_board(blank_tile_pos)

# loop over
while True:

    # control screen refresh rate
    clock.tick( fps)

    # fill bg color
    screen.fill( bg_color)

    # fill images
    screen.blit( logo_img, ( screen_width // 2 - 9.5 * tile_size, 0))
    screen.blit( board_img, (2 * tile_size, 5 * tile_size))

    draw_tiles( tile_pos_matrix)

    # check for events
    for event in pygame.event.get():

        # check basic actions
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if won:
                won = False
                blank_tile_pos, blank_tile_moves = shuffle_board(blank_tile_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_l:
                draw_rect = not draw_rect
            if event.key == pygame.K_ESCAPE and won:
                won = False
                blank_tile_pos, blank_tile_moves = shuffle_board(blank_tile_pos)

        # check tile motion
            if not won:
                if event.key == pygame.K_UP:
                    blank_tile_pos = move_tile( "up", blank_tile_pos)
                    won = check_won( tile_sol_matrix, tile_pos_matrix)

                elif event.key == pygame.K_DOWN:
                    blank_tile_pos = move_tile( "down", blank_tile_pos)
                    won = check_won( tile_sol_matrix, tile_pos_matrix)

                elif event.key == pygame.K_LEFT:
                    blank_tile_pos = move_tile( "left", blank_tile_pos)
                    won = check_won( tile_sol_matrix, tile_pos_matrix)

                elif event.key == pygame.K_RIGHT:
                    blank_tile_pos = move_tile( "right", blank_tile_pos)
                    won = check_won( tile_sol_matrix, tile_pos_matrix)

    # check buttons
    if new_game_btn.draw() and not won:
        blank_tile_pos, blank_tile_moves  = shuffle_board(blank_tile_pos)

    if solution_btn.draw() and not won:
        blank_tile_pos = solve_board(blank_tile_pos)

    if won == True:
        screen.blit(fade_img, ( 0, 0))
        screen.blit(you_won_img, ( screen_width // 2 - 9 * tile_size, 9.5 * tile_size))

    # draw grid line
    if draw_rect:
        drawGrid()
    
    # refresh screen
    pygame.display.flip()