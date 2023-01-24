import pygame
from sys import exit

# initializing pygame
pygame.init()
screen_size = (600, 700)

# creating window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Home")

clock = pygame.time.Clock()  # to keep time and frame rate info


def theme(selected='0'):
    global bg, board, x, o
    bg = pygame.image.load('./graphics/theme/' + selected + '/bg.jpg').convert()
    bg = pygame.transform.scale(bg, (600, 700))
    board = pygame.image.load('./graphics/theme/' + selected + '/board.png').convert_alpha()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    theme()
    screen.blit(bg, (0, 0))

    # flip() updates the screen to make our changes visible
    pygame.display.flip()

    clock.tick(60)

pygame.quit()