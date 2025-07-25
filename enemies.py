import pygame
from bulletClass import Bullet
class EnemyPlane:
    def __init__(self,SCREEN_WIDTH, SCREEN_HEIGHT):

        self.player = pygame.image.load("Resource/PNG/Enemies/enemyBlack1.png")

        # start position of airplane
        self.x = 0
        self.y = 0
        # attribute of airplane
        self.speed = 10

        # list for bullet

        self.bullets = []


    # display airplane in screen
    def display(self, screen):
        screen.blit(self.player, (self.x, self.y))

        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display(screen)

    def auto_move(self, Screen_Height):

        # modify coordinate y of bullet
        self.y += self.speed
