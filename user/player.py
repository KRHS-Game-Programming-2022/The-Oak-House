import pygame, os


class Player:
    def __init__(self):
        self.speedx = 0
        self.speedy = 0
        self.frames = 0
        self.maxSpeed = 5
        self.headingx = "none"
        self.headingy = "none"
        self.speed = [0, 0]

        stillImages = []
        stillPath = "assets/images/player/still/"
        for file in os.listdir(stillPath):
            if file[-4:] == ".png":
                stillImages += [pygame.image.load(stillPath + file)]

        leftImages = []
        rightImages = []
        leftPath = "assets/images/player/left/"
        for file in os.listdir(leftPath):
            if file[-4:] == ".png":
                leftImages += [pygame.image.load(leftPath + file)]
                rightImages += [pygame.transform.flip(leftImages[-1], True, False)]





        self.imagesDict = {"still": stillImages, "left": leftImages, "right": rightImages}
        self.images = self.imagesDict["still"]
        self.frame = 0
        self.maxFrame = len(self.images)
        self.animationDelayMax = 60/5
        self.animationDelay = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()

    def update(self):
        self.animate()
        self.move()

    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def animate(self):
        self.animationDelay += 1
        if self.animationDelay > self.animationDelayMax:
            self.animationDelay = 0
            self.frame += 1
            if self.frame >= self.maxFrame:
                self.frame = 0
            self.image = self.images[self.frame]

        if self.headingy == "up":
            if self.headingx == "left":
                self.images = self.imagesDict["left"]
            elif self.headingx == "right":
                self.images = self.imagesDict["right"]
            elif self.headingx == "none":
                self.images = self.imagesDict["still"]
        elif self.headingy == "down":
            if self.headingx == "left":
                self.images = self.imagesDict["left"]
            elif self.headingx == "right":
                self.images = self.imagesDict["right"]
            elif self.headingx == "none":
                self.images = self.imagesDict["still"]
        elif self.headingy == "none":
            if self.headingx == "left":
                self.images = self.imagesDict["left"]
            elif self.headingx == "right":
                self.images = self.imagesDict["right"]
            elif self.headingx == "none":
                self.images = self.imagesDict["still"]

    def control(self, direction: str):
        if direction == "up":
            self.speedy = -self.maxSpeed
            self.headingy = "up"
        elif direction == "down":
            self.speedy = self.maxSpeed
            self.headingy = "down"
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.headingx = "left"
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.headingx = "right"
        if direction == "stop up":
            if self.headingy == "up":
                self.speedy = 0
                self.headingy = "none"
        elif direction == "stop down":
            if self.headingy == "down":
                self.speedy = 0
                self.headingy = "none"
        if direction == "stop left":
            if self.headingx == "left":
                self.speedx = 0
                self.headingx = "none"
        elif direction == "stop right":
            if self.headingx == "right":
                self.speedx = 0
                self.headingx = "none"
