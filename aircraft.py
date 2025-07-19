import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
def init_screen():
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
    # background

    background = pygame.image.load('./Resource/Backgrounds/blue.png')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT   ))

    # put background in screen

    screen.blit(background, (0, 0))

    #display screen
    while True:
        pygame.display.update()


if __name__=='__main__':
    pygame.init()
    init_screen()
    pygame.quit()
