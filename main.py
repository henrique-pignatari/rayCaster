# Example file showing a circle moving on screen
from random import random

import pygame
from Ball import Ball
from Ray import create_rays
from Wall import create_walls
from config import WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

drawables = []
walls = []
propagation_array = []

ball = Ball(screen.get_width() / 2, screen.get_height() / 2, radius=10)

drawables.append(ball)

create_walls(10, drawables, walls)
create_rays(ball.position, 90, 360, drawables, propagation_array)



def draw_loop():
    screen.fill("black")
    pygame.draw.circle(screen, "blue", [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2], 10)
    for drawable in drawables:
        drawable.draw(screen)

    pygame.display.flip()


def propagation_loop():
    for element in propagation_array:
        element.calculate_propagation(walls)


def check_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True


while running:
    ball.move()
    propagation_loop()
    draw_loop()

    running = check_close()

    dt = clock.tick(60) / 1000

pygame.quit()
