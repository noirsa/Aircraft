import pygame
from pygame.examples.go_over_there import screen

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

class UserPlane:
    def __init__(self):

        self.player = pygame.image.load("Resource/PNG/player.png")

        # start position of airplane
        self.x = screen.get_width()/2
        self.y = screen.get_height()/4*3

        # attribute of airplane
        self.speed = 10

    def key_control(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed

        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y += self.speed

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y -= self.speed

def init_screen():
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
    # background

    background = pygame.image.load('./Resource/Backgrounds/blue.png')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT   ))

    # put background in screen

    screen.blit(background, (0, 0))

    while True:
        #get and process events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # execute pygame quit
                pygame.quit()
                exit()

        # display screen
        pygame.display.update()


if __name__=='__main__':
    pygame.init()
    init_screen()
