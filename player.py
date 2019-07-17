import pygame, random, main

class Player(object):

    def __init__(self, x, y, screen):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False
        self.maxX = 0
        self.maxY = 0
        self.screen = screen
        self.src = "player.png"

    def display(self):
        texture = pygame.image.load(self.src)
        texture_rect = texture.get_rect()
        texture_rect.topleft = (self.x, self.y)
        self.screen.blit(texture, texture_rect)

    def mypos(self): return (self.x, self.y)

    def move(self):
        if self.left and self.x > 0:
            self.left = False
            self.x -= 50
        if self.right and self.x < self.maxX:
            self.right = False
            self.x += 50
        if self.top and self.y > 0:
            self.top = False
            self.y -= 50
        if self.bottom and self.y < self.maxY:
            self.bottom = False
            self.y += 50
