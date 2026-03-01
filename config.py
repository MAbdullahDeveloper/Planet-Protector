import pygame

# Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont("{¡Estoy Bueno!}", 72)  # Original font
smallFont = pygame.font.SysFont("{¡Estoy Bueno!}", 48)
hoverFont = pygame.font.SysFont("{¡Estoy Bueno!}", 56)
answerFont = pygame.font.SysFont("{¡Estoy Bueno!}", 30)

# Game states
MENU = "menu"
PLAY = "play"
SETTINGS = "settings"
LEVEL1 = "L1"
LEVEL2 = "L2"
LEVEL3 = "L3"
LEVEL4 = "L4"
LEVEL5 = "L5"

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Planet Protectors')
