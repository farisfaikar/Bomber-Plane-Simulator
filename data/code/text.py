import pygame
import data.code.config as cfg


class Text:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.chary = pygame.font.Font(cfg.chary_font, 20)

    def render(self, screen, text):
        color = cfg.L_GREEN
        text_obj = self.chary.render(text, True, color)
        screen.blit(text_obj, (self.x, self.y))

    @staticmethod
    def format_coords(pos):
        x, y = pos
        return int(x * 10), int((400 - y) * 10)


class BombCoordsText(Text):
    def draw(self, screen):
        plane_x, plane_y = self.format_coords(cfg.dynamic_pos)
        bomb_x, bomb_y = self.format_coords(cfg.bomb_pos)
        if not cfg.is_bomb_dropped:
            bomb_x = plane_x
            bomb_y = plane_y
        self.render(screen, f"Bomb Coords = [{bomb_x} m, {bomb_y} m]")


class BombMaximaText(Text):
    def draw(self, screen):
        plane_x, plane_y = self.format_coords(cfg.dynamic_pos)
        bomb_maxima = int((400 - cfg.bomb_maxima) * 10)
        if not cfg.is_bomb_dropped:
            bomb_maxima = plane_y
        self.render(screen, f"Bomb Maxima = {bomb_maxima} m")


class BombTravelTimeText(Text):
    def draw(self, screen):
        bomb_travel_time = cfg.bomb_travel_time * 1000
        b_miliseconds = str(int(bomb_travel_time % 1000))
        b_seconds = int(bomb_travel_time // 1000 % 60)
        if len(b_miliseconds) == 2:
            b_miliseconds = f"0{b_miliseconds}"
        elif len(b_miliseconds) == 1:
            b_miliseconds = f"00{b_miliseconds}"
        self.render(screen, f"Travel Time = {b_seconds}.{b_miliseconds} seconds")


class BombTravelDistance(Text):
    def draw(self, screen):
        bomb_travel_distance = int(cfg.bomb_travel_distance * 10)
        self.render(screen, f"Distance    = {bomb_travel_distance} m")
