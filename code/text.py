import pygame
import config as cfg


class Text:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.chary = pygame.font.Font(cfg.chary_font, 20)

    def draw(self, screen, text):
        color = cfg.L_GREEN
        text_obj = self.chary.render(text, True, color)
        screen.blit(text_obj, (self.x, self.y))
