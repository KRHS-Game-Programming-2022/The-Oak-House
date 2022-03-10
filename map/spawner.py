import pygame


class Spawner:
    def __init__(self, pos=None):
        if pos is None:
            pos = [0, 0]
        self.image = pygame.image.load("Images/WallTiles/Spawner.png")
        self.rect = self.image.get_rect(center=pos)
        self.kind = "Spawner"

    def update(self, size):
        pass
