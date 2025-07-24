import time

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

class UserPlane:
    def __init__(self):

        self.player = pygame.image.load("Resource/PNG/playerShip1_red.png")

        # start position of airplane
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/4*3
        # attribute of airplane
        self.speed = 10

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

        # future definition for fire
        if keys[pygame.K_SPACE]:
            pass

    # display airplane in screen
    def display(self, screen):
        screen.blit(self.player, (self.x, self.y))

def init_screen():
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
    # background

    background = pygame.image.load('./Resource/Backgrounds/blue.png')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT   ))

    player = UserPlane()
    player.display(screen)




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
        pygame.display.update()
        time.sleep(0.01)


if __name__=='__main__':
    pygame.init()
    init_screen()
