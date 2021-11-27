import pygame
import sys

import config as cfg
import crt as c
import text
import ui
import trajectory
import slider
import button
from timer import Timer


# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
TARGET_FPS = 60
FPS = 60

# Initiate screen
cfg.screen_width = 800
cfg.screen_height = 500
screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))

# Set caption, icon
pygame.display.set_caption("Bomber Plane Simulator!")
icon = pygame.image.load('sprite/icon.png')
pygame.display.set_icon(icon)


class Program:
    def __init__(self):
        self.ui_lines = ui.UILines()
        self.plane_trajectory = trajectory.PlaneTrajectory()

        self.velocity_slider = slider.VelocitySlider((110, 440), 180, cfg.GREEN, cfg.L_GREEN)
        self.angle_slider = slider.AngleSlider((310, 440), 180, cfg.GREEN, cfg.L_GREEN)
        self.bomb_height_slider = slider.BombHeightSlider((510, 440), 180, cfg.GREEN, cfg.L_GREEN)

        # Experimental instances
        self.bomb_trajectory = trajectory.BombTrajectory()

        self.bomb_coords_text = text.Text(110, 470)
        self.plane_coords_text = text.Text(110, 450)
        self.time_text = text.Text(410, 450)

        self.play_pause_button = button.PlayPauseButton("Start", 80, 30, (10, 410), cfg.L_GREEN)
        self.reset_button = button.ResetButton("Reset", 80, 30, (10, 460), cfg.L_GREEN)

    def run(self):
        Timer.count_up()

        # self.input_text.draw(screen)
        self.ui_lines.draw(screen)

        self.velocity_slider.draw(screen, f"Velocity = {cfg.velocity * 10} m/s")
        self.angle_slider.draw(screen, f"Angle = {cfg.angle} deg")
        self.bomb_height_slider.draw(screen, f"Drop Bomb at = {cfg.bomb_height * 10} m")

        # Experimental methods
        self.plane_trajectory.draw(screen)
        self.bomb_trajectory.draw(screen)

        # TODO the code below me is a mess. Clean it
        plane_x, plane_y = self.format_coords(cfg.dynamic_pos)
        self.plane_coords_text.draw(screen, f"Plane Coords = [{plane_x} m, {plane_y} m]")
        bomb_x, bomb_y = self.format_coords(cfg.bomb_pos)
        if cfg.is_bomb_dropped:
            self.bomb_coords_text.draw(screen, f"Bomb Coords  = [{bomb_x} m, {bomb_y} m]")
        else:
            self.bomb_coords_text.draw(screen, f"Bomb Coords  = [{plane_x} m, {plane_y} m]")

        self.time_text.draw(screen, f"Time = {Timer.minutes}:{Timer.seconds}:{Timer.miliseconds}")

        self.play_pause_button.draw(screen)
        self.reset_button.draw(screen)

    @staticmethod
    def format_coords(pos):
        x, y = pos
        return int(x * 10), 4000 - int(y * 10)


def main():
    # Initiate instances
    program = Program()
    crt = c.CRT(cfg.screen_width, cfg.screen_height)

    while True:
        # Calculate delta time
        dt = clock.tick(FPS) * 0.001 * TARGET_FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Run game
        program.run()
        crt.draw(screen, dt)

        # Updates
        pygame.display.flip()
        screen.fill(cfg.XD_GREEN)


if __name__ == '__main__':
    main()
