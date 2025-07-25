import time

import pygame

from bulletClass import Bullet
from enemies import EnemyPlane
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

class UserPlane:
    def __init__(self):

        self.player = pygame.image.load("Resource/PNG/playerShip1_red.png")

        # start position of airplane
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/4*3
        # attribute of airplane
        self.speed = 10

        # list for bullet

        self.bullets = []


    def key_control(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

        # press space for fire
        if keys[pygame.K_SPACE]:
            bullet = Bullet(self.x, self.y,self.player.get_width())

            # add bullet at list

            self.bullets.append(bullet)


    # display airplane in screen
    def display(self, screen):
        screen.blit(self.player, (self.x, self.y))

        for bullet in self.bullets:
            limit = bullet.auto_move()
            bullet.display(screen)
            if (limit):
                self.bullets.remove(bullet)

def init_screen():
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
    # background

    background = pygame.image.load('./Resource/Backgrounds/blue.png')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT   ))

    player = UserPlane()
    player.display(screen)


    enemy = EnemyPlane(SCREEN_WIDTH, SCREEN_HEIGHT)

    while True:
        # put background in screen
        screen.blit(background, (0, 0))
        #get and process events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # execute pygame quit
                pygame.quit()
                exit()

        player.key_control()
        # display screen
        player.display(screen)
        enemy.display(screen)
        enemy.auto_move(SCREEN_HEIGHT)
        pygame.display.update()

        time.sleep(0.01)


if __name__=='__main__':
    pygame.init()
    init_screen()
