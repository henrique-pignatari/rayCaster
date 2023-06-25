import pygame.draw


class Ball:
    def __init__(self, x, y, radius=20, color="red"):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.color = color

    def move(self):
        x, y = pygame.mouse.get_pos()

        self.position.x = x
        self.position.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
