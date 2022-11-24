# Import ------------------------------------------------------------------------------------------------------------
import pygame
import sys






# Initialize ---------------------------------------------------------------------------------------------------------
pygame.init()
screen_width, screen_height = ( 800, 600)
tile_size = 25
screen = pygame.display.set_mode( ( screen_width, screen_height))
draw_rect = True
pygame.display.set_caption( "8 Puzzle Problem")
bg_color = ( 45, 168, 216)





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
        pygame.draw.line(screen, ( 255, 255, 255), ( 0, line * tile_size), ( screen_width, line * tile_size))
        pygame.draw.line(screen, ( 255, 255, 255), ( line * tile_size, 0), ( line * tile_size, screen_width))
    for line in range( 0, 10):
        pygame.draw.line(screen, ( 0, 0, 0), ( 0, line * tile_size * 4), ( screen_width, line * tile_size * 4), 5)
        pygame.draw.line(screen, ( 0, 0, 0), ( line * tile_size * 4, 0), ( line * tile_size * 4, screen_width), 5)




# Load Assets ------------------------------------------------------------------------------------------------------------
# ui img
logo_img = pygame.image.load( 'assets/img/logo.png')

# btn img
new_game_btn = pygame.image.load( 'assets/btn/new_game.png')
solution_btn = pygame.image.load( 'assets/btn/solution.png')
speed_x_btn = pygame.image.load( 'assets/btn/speed_x.png')

# board img
board_img = pygame.image.load( 'assets/img/board.png')
tile_0 = pygame.image.load( 'assets/img/tile_0.png')
tile_1 = pygame.image.load( 'assets/img/tile_1.png')
tile_2 = pygame.image.load( 'assets/img/tile_2.png')
tile_3 = pygame.image.load( 'assets/img/tile_3.png')
tile_4 = pygame.image.load( 'assets/img/tile_4.png')
tile_5 = pygame.image.load( 'assets/img/tile_5.png')
tile_6 = pygame.image.load( 'assets/img/tile_6.png')
tile_7 = pygame.image.load( 'assets/img/tile_7.png')
tile_8 = pygame.image.load( 'assets/img/tile_8.png')

# btn
new_game_btn = Button( 27.5 * tile_size, 10 * tile_size, new_game_btn)
solution_btn = Button( 27.5 * tile_size, 15 * tile_size, solution_btn)
speed_x_btn = Button( 27.5 * tile_size, 20 * tile_size, speed_x_btn)






# Game Loop ------------------------------------------------------------------------------------------------------------
while True:

    # Fill BG Color
    screen.fill( bg_color)

    # Fill Images
    screen.blit( logo_img, ( screen_width // 2 - 9.5 * tile_size, 0))
    screen.blit(board_img, (2 * tile_size, 5 * tile_size))

    screen.blit(tile_1, (  2 * tile_size + 9    ,    5 * tile_size + 9))
    screen.blit(tile_2, (  8 * tile_size + 4    ,    5 * tile_size + 9))
    screen.blit(tile_3, ( 14 * tile_size - 2    ,    5 * tile_size + 9))
    screen.blit(tile_4, (  2 * tile_size + 9    ,   11 * tile_size + 3))
    screen.blit(tile_5, (  8 * tile_size + 4    ,   11 * tile_size + 3))
    screen.blit(tile_6, ( 14 * tile_size - 2    ,   11 * tile_size + 3))
    screen.blit(tile_7, (  2 * tile_size + 9    ,   17 * tile_size - 3))
    screen.blit(tile_8, (  8 * tile_size + 4    ,   17 * tile_size - 3))
    screen.blit(tile_0, ( 14 * tile_size - 2    ,   17 * tile_size - 3))

    # Check for Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_l:
                draw_rect = not draw_rect

    if new_game_btn.draw():
        pass

    if solution_btn.draw():
        pass

    if speed_x_btn.draw():
        pass

    # Draw Grid Line
    if draw_rect:
        drawGrid()
    
    # Refresh Screen
    pygame.display.flip()