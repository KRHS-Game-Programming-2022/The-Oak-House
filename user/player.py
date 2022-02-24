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

        stillImage = pygame.image.load(os.path.join("assets", "images", "player", "still.png"))
        leftImages = []
        for i in range(2,10):
            leftImages+=[pygame.image.load("assets/images/player/Player Animations/WalkCycle000"+str(i)+".png")]
        leftImages += [pygame.image.load("assets/images/player/Player Animations/WalkCycle000"+str(i)+".png")]
        rightImage = pygame.image.load(os.path.join("assets", "images", "player", "right.png"))

        self.images = {"still": stillImage, "left": leftImages, "right": rightImage}
        self.image = self.images["still"]

        self.rect = self.image.get_rect()

    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def animate(self):
        if self.headingy == "up":
            if self.headingx == "left":
                self.image = self.images["left up"]
            elif self.headingx == "right":
                self.image = self.images["right up"]
            elif self.headingx == "none":
                self.image = self.images["up"]
        elif self.headingy == "down":
            if self.headingx == "left":
                self.image = self.images["left down"]
            elif self.headingx == "right":
                self.image = self.images["right down"]
            elif self.headingx == "none":
                self.image = self.images["down"]
        elif self.headingy == "none":
            if self.headingx == "left":
                self.image = self.images["left"]
            elif self.headingx == "right":
                self.image = self.images["right"]

    def update(self):
        self.animate()
        self.move()

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
