import pygame
from data.code.timer import Timer
import data.code.config as cfg


class Button:
    def __init__(self, text, width, height, pos, color):
        # Core attributes
        self.pressed = False
        self.executed = False
        self.text = text
        self.pos = pos

        # top rectangle
        self.button_rect = pygame.Rect(pos, (width, height))
        self.BUTTON_COLOR = color
        self.button_color = color

        # text
        button_font = pygame.font.Font(cfg.chary_font, 20)
        self.text_surf = button_font.render(self.text, True, cfg.XD_GREEN)
        self.text_rect = self.text_surf.get_rect(center=self.button_rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.button_color, self.button_rect, border_radius=5)

        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.button_rect.collidepoint(mouse_pos):
            self.button_color = cfg.WHITE
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.button_color = cfg.GREEN
            else:
                if self.pressed:
                    self.button_action()
                    self.pressed = False
        else:
            self.pressed = False
            self.button_color = self.BUTTON_COLOR

    def button_action(self):
        pass


class StartButton(Button):
    def button_action(self):
        Timer.start_timer()


class ResetButton(Button):
    def button_action(self):
        Timer.reset_timer()
