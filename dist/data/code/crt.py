import pygame
from random import randint
import data.code.config as cfg


class CRT:
    def __init__(self, tv_width, tv_height):
        self.tv_width = tv_width
        self.tv_height = tv_height
        self.tv = pygame.image.load('data/sprite/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (self.tv_width, self.tv_height))

        gradient_width = tv_width
        gradient_height = 200
        self.gradient = pygame.image.load('data/sprite/green_gradient.png').convert_alpha()
        self.gradient = pygame.transform.scale(self.gradient, (gradient_width, gradient_height))
        self.dynamic_y_pos = 0 - self.gradient.get_height()

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(self.tv_height / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos), (self.tv_width, y_pos), 1)

    def create_grid_lines(self):
        line_space = 10
        x_line_amount = int(self.tv_width / line_space)
        y_line_amount = int(self.tv_height / line_space)
        for line in range(x_line_amount):
            x_pos = line * line_space
            if line % line_space == 0:
                pygame.draw.line(self.tv, cfg.GREEN, (x_pos, 0), (x_pos, self.tv_height), 2)
            else:
                pygame.draw.line(self.tv, cfg.GREEN, (x_pos, 0), (x_pos, self.tv_height), 1)

        for line in range(y_line_amount):
            y_pos = line * line_space
            if line % line_space == 0:
                pygame.draw.line(self.tv, cfg.GREEN, (0, y_pos), (self.tv_width, y_pos), 2)
            else:
                pygame.draw.line(self.tv, cfg.GREEN, (0, y_pos), (self.tv_width, y_pos), 1)

    def create_sweeper(self, screen, dt):
        if self.dynamic_y_pos <= self.tv_height:
            sweep_speed = 2 * dt
            screen.blit(self.gradient, (0, self.dynamic_y_pos))
            self.dynamic_y_pos += sweep_speed
        else:
            self.dynamic_y_pos = 0 - self.gradient.get_height()

    def draw(self, screen, dt):
        self.tv.set_alpha(randint(60, 90))
        self.gradient.set_alpha(10)
        self.create_crt_lines()
        self.create_grid_lines()
        self.create_sweeper(screen, dt)
        screen.blit(self.tv, (0, 0))
