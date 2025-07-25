import pygame


class Bullet(object):
    def __init__(self,x,y,player_width):

        self.speed = 10
        self.image =pygame.image.load('Resource/PNG/Effects/fire01.png')
        self.x = x + player_width/2 - self.image.get_width()/2
        self.y = y - self.image.get_height() +1
        self.damage = 1

    def display(self, screen):
        screen.blit(self.image,(self.x,self.y))

    # this is method to move bullet automatically
    def auto_move(self):

        # modify coordinate y of bullet
        self.y -= self.speed
