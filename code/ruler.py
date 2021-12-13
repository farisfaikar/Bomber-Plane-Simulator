import pygame
import config as cfg


class Ruler:
    def __init__(self, pos, total_marks, starting_value, end_value, length):
        self.pos = pos
        self.total_marks = total_marks
        self.starting_value = starting_value
        self.end_value = end_value
        self.length = length

        self.chary = pygame.font.Font(cfg.chary_font, 15)
        self.color = cfg.GREEN
        self.increments = 0
        self.increment_length = 0
        self.text_data = []

        self.ruler_logic()

    def ruler_logic(self):
        pass


class VerticalRuler(Ruler):
    def draw(self, screen):
        for i, (pos, dynamic_value) in enumerate(self.text_data):
            text_obj = self.chary.render(dynamic_value, True, self.color)
            screen.blit(text_obj, pos)

    def ruler_logic(self):
        self.increments = (self.end_value - self.starting_value) / (self.total_marks - 1)
        self.increment_length = self.length / (self.total_marks - 1)

        for i in range(self.total_marks):
            value = int(self.starting_value)
            self.text_data.append([self.pos, f"{value} m"])

            x, y = self.pos
            y -= self.increment_length
            self.pos = (x, y)
            self.starting_value += self.increments


class HorizontalRuler(Ruler):
    def draw(self, screen):
        for i, (pos, dynamic_value) in enumerate(self.text_data):
            text_obj = self.chary.render(dynamic_value, True, self.color)
            x, y = pos
            x -= text_obj.get_width()
            y -= text_obj.get_height()
            pos = (x, y)
            screen.blit(text_obj, pos)

    def ruler_logic(self):
        self.increments = (self.end_value - self.starting_value) / (self.total_marks - 1)
        self.increment_length = self.length / (self.total_marks - 1)

        for i in range(self.total_marks):
            value = int(self.starting_value)
            self.text_data.append([self.pos, f"{value} m"])

            x, y = self.pos
            x += self.increment_length
            self.pos = (x, y)
            self.starting_value += self.increments
