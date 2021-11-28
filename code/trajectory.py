import pygame
import math
import numpy

import config as cfg
from timer import Timer


class PlaneTrajectory:
    def __init__(self):
        # Core Attributes
        cfg.angle = 40
        self.color = cfg.L_GREEN
        self.start_pos = (0, 400)
        self.dynamic_pos = self.start_pos

        self.plane = pygame.image.load('sprite/plane.png')
        self.plane = pygame.transform.scale(self.plane, (30, 15))
        self.dashed_line_length = 1000

    def draw(self, screen):
        self.run_logic()

        # Draw dashed line
        x0, y0 = self.start_pos
        angle_rad = math.radians(cfg.angle)
        x1 = x0 + math.cos(angle_rad) * self.dashed_line_length
        y1 = y0 + -math.sin(angle_rad) * self.dashed_line_length
        draw_dashed_line(screen, self.color, self.start_pos, (x1, y1), dash_length=cfg.dash_length)

        # Draw line
        pygame.draw.line(screen, self.color, self.start_pos, self.dynamic_pos, 2)

        # Draw plane
        x, y = self.dynamic_pos
        plane_copy = pygame.transform.rotate(self.plane, cfg.angle)
        screen.blit(plane_copy, (x - int(plane_copy.get_width() / 2), y - int(plane_copy.get_height() / 2)))

        # Update dynamic pos to config
        cfg.dynamic_pos = self.dynamic_pos

    def run_logic(self):
        x0, y0 = self.start_pos
        time = round(Timer.dynamic_time * .001, 3)
        angle_rad = math.radians(cfg.angle)
        x1 = x0 + math.cos(angle_rad) * cfg.velocity * time
        y1 = y0 + -math.sin(angle_rad) * cfg.velocity * time
        self.dynamic_pos = (x1, y1)


class BombTrajectory:
    def __init__(self):
        # Core attributes
        self.bomb = pygame.image.load('sprite/bomb.png')
        self.bomb = pygame.transform.scale(self.bomb, (20, 10))
        self.cross = pygame.image.load('sprite/cross.png')
        self.cross = pygame.transform.scale(self.cross, (20, 20))

        self.x = self.y = 0
        self.bomb_starting_pos = (0, 0)
        self.bomb_height = 400 - cfg.bomb_height
        self.GRAVITY = 0.9807  # m/s^2 = px/s^2
        self.bomb_timer = Timer()
        self.bomb_angle = 0
        self.is_bomb_landed = False

    def draw(self, screen):
        # Draw height line
        self.bomb_height = 400 - cfg.bomb_height
        draw_dashed_line(screen, cfg.BLUE, (0, self.bomb_height), (800, self.bomb_height))

        # Draw bomb landing zone 'X'
        if self.y >= 400 and Timer.is_timer_running:
            self.is_bomb_landed = True
            screen.blit(self.cross, (self.x - int(self.cross.get_width() / 2), self.y
                                     - int(self.cross.get_height() / 2)))

        # Draw bomb trajectory
        self.run_logic()
        if cfg.is_bomb_dropped and not self.is_bomb_landed:
            bomb_copy = pygame.transform.rotate(self.bomb, self.bomb_angle)
            screen.blit(bomb_copy, (self.x - int(bomb_copy.get_width() / 2), self.y - int(bomb_copy.get_height() / 2)))

    def run_logic(self):
        # Check if height is reached
        if cfg.dynamic_pos[1] <= self.bomb_height and not cfg.is_bomb_dropped and Timer.is_timer_running:
            self.bomb_starting_pos = cfg.dynamic_pos
            cfg.is_bomb_dropped = True

        # Run bomb trajectory calculation
        x_before = self.x
        y_before = self.y

        if cfg.is_bomb_dropped and not self.is_bomb_landed:
            self.x = cfg.dynamic_pos[0]
            y0 = self.bomb_starting_pos[1]
            time = self.bomb_timer.count() * .001
            angle_rad = math.radians(cfg.angle)
            self.y = y0 - cfg.velocity * math.sin(angle_rad) * time + .5 * self.GRAVITY * time ** 2
            # Update bomb pos
            cfg.bomb_pos = self.x, self.y

        # Run bomb dynamic angle calculation
        x_after = self.x - x_before
        y_after = self.y - y_before
        bomb_angle_rad = -math.atan2(y_after, x_after)
        self.bomb_angle = math.degrees(bomb_angle_rad)

        # Check if timer is reset
        if not Timer.is_timer_running:
            cfg.is_bomb_dropped = False
            self.is_bomb_landed = False
            self.bomb_timer.reset()
            self.x = self.y = 0


def draw_dashed_line(surface, color, start_pos, end_pos, width=1, dash_length=10, exclude_corners=True):
    # convert tuples to numpy arrays
    start_pos = numpy.array(start_pos)
    end_pos = numpy.array(end_pos)

    # get euclidian distance between start_pos and end_pos
    length = numpy.linalg.norm(end_pos - start_pos)

    # get amount of pieces that line will be split up in (half of it are amount of dashes)
    dash_amount = int(length / dash_length)

    # x-y-value-pairs of where dashes start (and on next, will end)
    dash_knots = numpy.array([numpy.linspace(start_pos[i], end_pos[i], dash_amount) for i in range(2)]).transpose()

    return [pygame.draw.line(surface, color, tuple(dash_knots[n]), tuple(dash_knots[n + 1]), width)
            for n in range(int(exclude_corners), dash_amount - int(exclude_corners), 2)]
