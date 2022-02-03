import pygame, sys, math

class Ball():
    def __init__(self, fastness = [1,1], starting = [0,0]):
        self.picture = pygame.image.load("ball1.png")
    self.rectangle = self.image.get_rect("ball1.png")
    self.speedx = speed[0]
    self.speedy = speed[1]
    self.speed = [self.speedx, self.speedy]
    self.rad = (self.rectangle.height/2 + self.rectangle.width/2)/2
    self.frame = 0
    self.frameMax = len(self.images)-1 
    self.picture = self.picture[self.frame]
        
    def moveSelf(self): 
        pass 
        
    def hitWall(self, size):  width = size[0]
    height = size[1]
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rectangle.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
            if self.rectangle.top < 0:
                self.speedy = -self.speedy
                self.didBounceY = True
        if not self.didBounceX:
            if self.rectangle.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
            if self.rectangle.left < 0:
                self.speedx = -self.speedx
                self.didBounceX = True
        
    def hitOtherBall(self, otherBall):
        pass
        
pygame.init()

clock = pygame.time.Clock()

width = 600
height = 400
size = width, height

screen = pygame.display.set_mode(size)

ball = Ball([3,3], [width/2, height/2])

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
    
    ball.moveSelf()
    ball.hitWall(size)
    
    screen.fill((0,0,0))
    screen.blit(ball.picture, ball.rectangle)
    pygame.display.flip() 
    clock.tick(60)
