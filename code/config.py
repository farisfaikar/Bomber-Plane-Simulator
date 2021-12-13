import pygame

# ----------- Global Variables -----------
# Screen dimension
screen_width = 800
screen_height = 500

# Terminal colors
L_GREEN = pygame.Color("#5ec830")
GREEN = pygame.Color("#1c4811")
D_GREEN = pygame.Color("#255517")
XD_GREEN = pygame.Color("#071404")
RED = pygame.Color("#f41919")
BLUE = pygame.Color("#32f4f4")
WHITE = pygame.Color("#ffffff")

# Font
chary_font = 'font/chary___.ttf'

# Slider attributes
dash_length = 10
MAX_DASH_LENGTH = 20
MIN_DASH_LENGTH = 10

angle = 0
MAX_ANGLE = 90
MIN_ANGLE = 0

velocity = 0
MAX_VELOCITY = 20
MIN_VELOCITY = 6

bomb_height = 0
MAX_BOMB_HEIGHT = 400
MIN_BOMB_HEIGHT = 0

starting_height = 0
MAX_STARTING_HEIGHT = 400
MIN_STARTING_HEIGHT = 0

# Trajectory attributes
dynamic_pos = (0, 0)
bomb_pos = (0, 0)

x_diff = 0
y_diff = 0

bomb_maxima = 0
bomb_travel_time = 0
is_bomb_landed = False
is_bomb_dropped = False
bomb_travel_distance = 0
