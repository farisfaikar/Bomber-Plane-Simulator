import pygame
import sys

import config as cfg
import crt as c
import text
import line
import slider
import button
import ruler
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
        self.ui_lines = line.GroundLine()
        self.plane_path_line = line.PlanePathLine()
        self.bomb_trajectory = line.BombTrajectory()
        self.bomb_max_height_line = line.BombMaxHeightLine()
        self.bomb_trajectory_line = line.BombTrajectoryLine()

        self.velocity_slider = slider.VelocitySlider((110, 440), 180, cfg.GREEN, cfg.L_GREEN)
        self.angle_slider = slider.AngleSlider((310, 440), 180, cfg.GREEN, cfg.L_GREEN)
        self.starting_height_slider = slider.StartingHeightSlider((110, 490), 180, cfg.GREEN, cfg.L_GREEN)
        self.bomb_height_slider = slider.BombHeightSlider((310, 490), 180, cfg.GREEN, cfg.L_GREEN, .625)

        self.bomb_coords_text = text.BombCoordsText(510, 410)
        self.bomb_maxima_text = text.BombMaximaText(510, 430)
        self.bomb_travel_time_text = text.BombTravelTimeText(510, 450)
        self.bomb_travel_distance_text = text.BombTravelDistance(510, 470)

        self.start_button = button.StartButton("Start", 80, 30, (10, 410), cfg.L_GREEN)
        self.reset_button = button.ResetButton("Reset", 80, 30, (10, 460), cfg.L_GREEN)

        self.vertical_ruler = ruler.VerticalRuler((0, 300), 4, 1000, 4000, 300)
        self.horizontal_ruler = ruler.HorizontalRuler((0, 400), 9, 0, 8000, 800)

        # Experimental instances

    def run(self):
        Timer.count_timer()

        self.vertical_ruler.draw(screen)
        self.horizontal_ruler.draw(screen)

        self.velocity_slider.draw(screen, f"Velocity = {cfg.velocity * 10} m/s")
        self.angle_slider.draw(screen, f"Angle = {cfg.angle} deg")
        self.bomb_height_slider.draw(screen, f"Drop Bomb at = {cfg.bomb_height * 10} m")
        self.starting_height_slider.draw(screen, f"Initial Y = {cfg.starting_height * 10} m")

        self.ui_lines.draw(screen)
        self.plane_path_line.draw(screen)
        self.bomb_trajectory_line.draw(screen)
        self.bomb_trajectory.draw(screen)
        self.bomb_max_height_line.draw(screen)

        self.start_button.draw(screen)
        self.reset_button.draw(screen)

        self.bomb_coords_text.draw(screen)
        self.bomb_maxima_text.draw(screen)
        self.bomb_travel_time_text.draw(screen)
        self.bomb_travel_distance_text.draw(screen)

        # Experimental methods


def main():
    # Initiate instances
    program = Program()
    crt = c.CRT(cfg.screen_width, cfg.screen_height)

    while True:
        # Calculate delta time
        dt = clock.tick(FPS) * .001 * TARGET_FPS

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
