import pygame, random

class Block(object):

    def __init__(self, x, y, color, screen):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen

    def chcolor(self,color):
        self.color = color

    def display(self):
        pygame.draw.rect(self.screen, self.color, [self.x,self.y,self.width,self.height])
