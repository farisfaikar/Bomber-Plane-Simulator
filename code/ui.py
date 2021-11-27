import pygame
import config as cfg


class UILines:
    def __init__(self):
        pass

    def draw(self, screen):
        pygame.draw.line(screen, cfg.L_GREEN, (0, 400), (800, 400), 4)
