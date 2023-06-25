from random import random

import pygame

from config import WINDOW_WIDTH, WINDOW_HEIGHT


class Wall:
    def __init__(self, x1, y1, x2, y2, width=2, color="white"):
        self.position_1 = pygame.Vector2(x1, y1)
        self.position_2 = pygame.Vector2(x2, y2)
        self.width = width
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.position_1, self.position_2, self.width)


def create_walls(quantity, draw_array, walls_array):
    for index in range(0, quantity):
        x1 = random() * WINDOW_WIDTH
        x2 = random() * WINDOW_WIDTH
        y1 = random() * WINDOW_HEIGHT
        y2 = random() * WINDOW_HEIGHT
        new_wall = Wall(x1, y1, x2, y2)

        draw_array.append(new_wall)
        walls_array.append(new_wall)
