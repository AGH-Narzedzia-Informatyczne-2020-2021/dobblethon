# gui with pygame - unstable
# in order to install pygame type in command prompt "pip install pygame" or "pip3 install pygame"
# if you use anaconda type: "pip install pygame"

import pygame

#colors (separate file later)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
screen = pygame.display.set_mode((1920,1080))

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
