import pygame


class bg(pygame.sprite.Sprite):
    def __init__(self, theme_num, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/theme/' + theme_num + '/bg.jpg').convert()
        self.image = pygame.transform.scale(self.image, (x, y))
        self.rect = self.image.get_rect(center=(x/2, y/2))


class board_spr(pygame.sprite.Sprite):
    def __init__(self, theme_num, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/theme/' + theme_num + '/board.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (420, 420))
        self.rect = self.image.get_rect(center=(x/2, y/2))


class x(pygame.sprite.Sprite):
    def __init__(self, theme_num, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/theme/' + theme_num + '/x_sprite.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


class o(pygame.sprite.Sprite):
    def __init__(self, theme_num, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/theme/' + theme_num + '/o_sprite.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
