import pygame
from sys import exit
import json
from game import game_screen

# importing theme configuration json file
with open("source/theme_config.json", encoding='utf-8') as load_theme:
        theme_config = json.load(load_theme)

# initializing pygame
pygame.init()
screen_size = (600, 700)

# creating window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Home")

clock = pygame.time.Clock()  # to keep time and frame rate info


def theme(selected="0"):
    global bg, board, x, o, head_font_surf, head_font_rect, comp_font_surf, comp_font_rect, player_font_surf, player_font_rect

    theme = theme_config[selected]
    font_config = theme["Font"]

    bg = pygame.image.load('./graphics/theme/' + selected + '/bg.jpg').convert()
    bg = pygame.transform.scale(bg, (600, 700))
    board = pygame.image.load('./graphics/theme/' + selected + '/board.png').convert_alpha()

    head_font = pygame.font.SysFont(font_config[0], font_config[1], font_config[2], font_config[3])
    head_font_surf = head_font.render('TIC-TAC-TOE', False, font_config[4], None)
    head_font_rect = head_font_surf.get_rect(center=(300, 100))

    comp_font = pygame.font.SysFont(font_config[0], 40, font_config[2], font_config[3])
    comp_font_surf = comp_font.render('Play with Computer', False, font_config[4], None)
    comp_font_rect = comp_font_surf.get_rect(center=(300, 270))

    player_font = pygame.font.SysFont(font_config[0], 40, font_config[2], font_config[3])
    player_font_surf = player_font.render('Play with Friend', False, font_config[4], None)
    player_font_rect = player_font_surf.get_rect(center=(300, 370))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    pygame.mouse.set_visible(False)

    mouse_pos = pygame.mouse.get_pos()

    theme()
    screen.blit(bg, (0, 0))
    screen.blit(head_font_surf, head_font_rect)

    pygame.draw.rect(screen, theme_config["0"]["Color"][1], (0, 0, 600, 700), 3)
    pygame.draw.rect(screen, theme_config["0"]["Color"][1], (5, 5, 590, 690), 3)

    # computer button
    if comp_font_rect.topleft[0] <= mouse_pos[0] <= comp_font_rect.bottomright[0] and comp_font_rect.topleft[1] <= mouse_pos[1] <= comp_font_rect.bottomright[1]:
        pygame.draw.rect(screen, theme_config["0"]["Color"][1],[comp_font_rect.topleft[0]-10, comp_font_rect.topleft[1]-6, comp_font_rect.width + 20, comp_font_rect.height + 12], border_radius=10)
        screen.blit(comp_font_surf, comp_font_rect)

        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            game_screen('Computer')
            exit()

    else:
        screen.blit(comp_font_surf, comp_font_rect)
        pygame.draw.rect(screen, theme_config["0"]["Color"][0],[comp_font_rect.topleft[0]-10, comp_font_rect.topleft[1]-6, comp_font_rect.width + 20, comp_font_rect.height + 12], 2, 10)

    # player button
    if player_font_rect.topleft[0] <= mouse_pos[0] <= player_font_rect.bottomright[0] and player_font_rect.topleft[1] <= mouse_pos[1] <= player_font_rect.bottomright[1]:
        pygame.draw.rect(screen, theme_config["0"]["Color"][1], [player_font_rect.topleft[0]-10, player_font_rect.topleft[1]-6, player_font_rect.width + 20, player_font_rect.height + 12], border_radius=10)
        screen.blit(player_font_surf, player_font_rect)

        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            game_screen('Player 2')
            exit()

    else:
        screen.blit(player_font_surf, player_font_rect)
        pygame.draw.rect(screen, theme_config["0"]["Color"][0], [player_font_rect.topleft[0]-10, player_font_rect.topleft[1]-6, player_font_rect.width + 20, player_font_rect.height + 12], 2, 10)

    screen.blit(player_font_surf, player_font_rect)

    pygame.draw.circle(screen, theme_config["0"]["Color"][2], mouse_pos, 5)

    pygame.display.update()
    # flip() updates the screen to make our changes visible
    pygame.display.flip()

    clock.tick(200)

pygame.quit()
