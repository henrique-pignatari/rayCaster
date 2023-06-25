import math

import pygame

from config import WINDOW_WIDTH, WINDOW_HEIGHT


class Ray:
    def __init__(self, position, angle, color="white", width=1):
        self.position_1 = position
        self.position_2 = pygame.Vector2(0, 0)
        self.color = color
        self.width = width
        self.angle = angle

    def calculate_center_angle(self):
        x1 = WINDOW_WIDTH/2
        y1 = WINDOW_HEIGHT/2
        x2, y2 = self.position_1

        return math.atan2((y2-y1), -(x2-x1))

    def calculate_propagation(self, walls):
        radian_angle = math.radians(self.angle - 45) + self.calculate_center_angle()
        x1, y1 = self.position_1
        x2 = x1 + ((WINDOW_WIDTH*2) * math.cos(radian_angle))
        y2 = y1 - ((WINDOW_WIDTH*2) * math.sin(radian_angle))
        self.position_2 = pygame.Vector2(x2, y2)

        for wall in walls:
            x3, y3 = wall.position_1
            x4, y4 = wall.position_2

            den = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))

            if den != 0:
                t = (((x1 - x3) * (y3 - y4)) - ((y1 - y3) * (x3 - x4)))/den
                u = (((x1 - x3) * (y1 - y2)) - ((y1 - y3) * (x1 - x2)))/den

                if 0 < t < 1 and 0 < u < 1:
                    new_x = x1 + (t * (x2 - x1))
                    new_y = y1 + (t * (y2 - y1))
                    new_position = pygame.Vector2(new_x, new_y)
                    current_distance = self.position_1.distance_to(self.position_2)
                    new_distance = self.position_1.distance_to(new_position)

                    if new_distance < current_distance:
                        self.position_2 = new_position

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.position_1, self.position_2, self.width)


def create_rays(position, angle, quantity, draw_array, propagation_array):
    for index in range(0, quantity+1):
        new_ray = Ray(position, (angle/quantity)*index)
        draw_array.append(new_ray)
        propagation_array.append(new_ray)
