import numpy as np
import pygame
from sys import exit
import json
from sprites import *
from computer import *

def block(screen):
    x = pygame.mouse.get_pos()[1]
    y = pygame.mouse.get_pos()[0]
    if 185<=x<=295 and 135<=y<=245:
        return (0,0)
    elif 185<=x<=295 and 245<=y<=355:
        return (1,0)
    elif 185<=x<=295 and 355<=y<=465:
        return (2,0)
    elif 295<=x<=405 and 245<=y<=355:
        return (1,1)
    elif 295<=x<=405 and 135<=y<=245:
        return (0,1)
    elif 295<=x<=405 and 355<=y<=465:
        return (2,1)
    elif 405<=x<=515 and 135<=y<=245:
        return (0,2)
    elif 405<=x<=515 and 245<=y<=355:
        return (1,2)
    elif 405<=x<=515 and 355<=y<=465:
        return (2,2)
    else:
        return False

global score_1, score_2, np_board
score_1 = 0
score_2 = 0
np_board = np.array([['' for i in range(0, 3)] for j in range(0, 3)])


def game_screen(player, theme_num='0'):
    global score_1, score_2, np_board

    # importing theme configuration json file
    with open("source/theme_config.json", encoding='utf-8') as load_theme:
        theme_config = json.load(load_theme)
    theme_config = theme_config[theme_num]
    font_config = theme_config["Font"]
    print(type(player))

    # initializing pygame
    pygame.init()
    screen_size = (600, 700)
    turn_arr = ['o', 'x']
    block_arr = []
    turn = 0
    result = None

    # creating window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Tic-Tac-Toe")

    clock = pygame.time.Clock()  # to keep time and frame rate info

    head_font = pygame.font.SysFont(font_config[0], font_config[1], font_config[2], font_config[3])
    head_font_surf = head_font.render('TIC-TAC-TOE', False, font_config[4], None)
    head_font_rect = head_font_surf.get_rect(center=(300, 70))

    player2_font = pygame.font.SysFont(font_config[0], 40, font_config[2], font_config[3])
    player2_font_surf = player2_font.render(player + ': ' + str(score_2), False, font_config[4], None)
    player2_font_rect = player2_font_surf.get_rect(center=(300, 650))

    player1_font = pygame.font.SysFont(font_config[0], 40, font_config[2], font_config[3])
    player1_font_surf = player1_font.render('Player 1: ' + str(score_1), False, font_config[4], None)
    player1_font_rect = player1_font_surf.get_rect(center=(300, 600))

    bg_sprite = bg(theme_num, screen.get_width(), screen.get_height())
    bg_img = pygame.sprite.GroupSingle()
    bg_img.add(bg_sprite)

    board_sprite = board_spr(theme_num, screen.get_width(), screen.get_height())
    board_img = pygame.sprite.GroupSingle()
    board_img.add(board_sprite)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # if result:
            #     if event. == pygame.K_SPACE:
            #     # if pygame.mouse.get_pressed()[0]:
            #         np_board = np.array([['' for i in range(0, 3)] for j in range(0, 3)])
            #         game_screen(player, theme_num)

        screen.fill((0, 0, 0))

        bg_img.draw(screen)
        board_img.draw(screen)
        screen.blit(head_font_surf, head_font_rect)
        screen.blit(player1_font_surf, player1_font_rect)
        screen.blit(player2_font_surf, player2_font_rect)
        
        if len(block_arr)!=0:
            for i in block_arr:
                i.draw(screen)
                
        if player == "Player 2":
            if pygame.mouse.get_pressed()[0]:
                pos = block(screen)
                print(pos)
                
                if pos:
                    if turn_arr[turn] == 'o':
                        o_sprite = o(theme_num, 60 + (pos[0]+1)*120, 110 + (pos[1]+1)*120)
                        o_img = pygame.sprite.GroupSingle()
                        o_img.add(o_sprite)
                        
                        block_arr.append(o_img)
                        
                        turn = (turn+1)%2
                        
                        np_board[pos[0]][pos[1]] = 'O'
                        
                    else:
                        x_sprite = x(theme_num, 60 + (pos[0]+1)*120, 110 + (pos[1]+1)*120)
                        x_img = pygame.sprite.GroupSingle()
                        x_img.add(x_sprite)
                        
                        block_arr.append(x_img)
                        
                        turn = (turn+1)%2
                        
                        np_board[pos[0]][pos[1]] = 'X'

                result = checkWinner(np_board)
                if result:
                    screen.fill(theme_config['Color'][0])
                    if result == "Draw":
                        result_font = pygame.font.SysFont(font_config[0], 60, font_config[2], font_config[3])
                        result_font_surf = result_font.render(result + '!', False, "#fb1349", None)
                        result_font_rect = result_font_surf.get_rect(center=(300, 300))
                        screen.blit(result_font_surf, result_font_rect)

                    elif result=="O":
                        result_font = pygame.font.SysFont(font_config[0], 60, font_config[2], font_config[3])
                        result_font_surf = result_font.render('Player 1 Wins !!!', False, "#fb1349", None)
                        result_font_rect = result_font_surf.get_rect(center=(300, 300))
                        screen.blit(result_font_surf, result_font_rect)
                        score_1 += 1
                    else:
                        result_font = pygame.font.SysFont(font_config[0], 60, font_config[2], font_config[3])
                        result_font_surf = result_font.render('Player 2 Wins !!!', False, "#fb1349", None)
                        result_font_rect = result_font_surf.get_rect(center=(300, 300))
                        screen.blit(result_font_surf, result_font_rect)
                        score_2 += 1
                    
        else:
            if pygame.mouse.get_pressed()[0]:
                
                pos = block(screen)
                print(pos)

                if pos:
                    o_sprite = o(theme_num, 60 + (pos[0]+1)*120, 110 + (pos[1]+1)*120)
                    o_img = pygame.sprite.GroupSingle()
                    o_img.add(o_sprite)

                    block_arr.append(o_img)

                    turn = (turn+1)%2

                    np_board[pos[0]][pos[1]] = 'O'
                    # print('Computer')
                    x_pos = playWithComputer(np_board)
                    # print(x_pos)
                    result = checkWinner(np_board)
                    if result:
                        screen.fill(theme_config['Color'][0])
                        if result == "Draw":
                            result_font = pygame.font.SysFont(font_config[0], 60, font_config[2], font_config[3])
                            result_font_surf = result_font.render(result + '!', False, "#fb1349", None)
                            result_font_rect = result_font_surf.get_rect(center=(300, 300))
                            screen.blit(result_font_surf, result_font_rect)

                        elif result == "O":
                            result_font = pygame.font.SysFont(font_config[0], 60, font_config[2], font_config[3])
                            result_font_surf = result_font.render('Player 1 Wins !!!', False, "#fb1349", None)
                            result_font_rect = result_font_surf.get_rect(center=(300, 300))
                            screen.blit(result_font_surf, result_font_rect)
                            score_1 += 1
                        else:
                            result_font = pygame.font.SysFont(font_config[0], 60, font_config[2], font_config[3])
                            result_font_surf = result_font.render('Computer Wins !!!', False, "#fb1349", None)
                            result_font_rect = result_font_surf.get_rect(center=(300, 300))
                            screen.blit(result_font_surf, result_font_rect)
                            score_2 += 1
                    else:
                        if x_pos:
                            x_sprite = x(theme_num, 60 + (x_pos[0]+1)*120, 110 + (x_pos[1]+1)*120)
                            x_img = pygame.sprite.GroupSingle()
                            x_img.add(x_sprite)

                            block_arr.append(x_img)

                            np_board[x_pos[0]][x_pos[1]] = 'X'


        clock.tick(12)

        pygame.display.flip()
        pygame.display.update()

    pygame.quit()


# game_screen('Player 2')
