import pygame


class Wall:
    def __init__(self, pos=None):
        if pos is None:
            pos = [0, 0]
        self.image = pygame.image.load("images/WallTiles/Wall.png")
        self.rect = self.image.get_rect(center=pos)
        self.kind = "wall"

    def update(self, size):
        pass
