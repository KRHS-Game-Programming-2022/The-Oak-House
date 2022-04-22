import pygame


class Wall:
    def __init__(self, pos=None):
        self.size = 20
        if pos is None:
            pos = [self.size / 2, self.size / 2]
        self.image = pygame.image.load("images/WallTiles/Wall.png")
        self.rect = self.image.get_rect(center=pos)
        self.kind = "wall"

    def update(self, size):
        pass
