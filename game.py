import pygame

pygame.init()

screen_width=500
screen_height=500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pool Game")
#colors
white = (255, 255, 255)
blue = (0, 0, 255)

#game loop, runs when the game runs and we put stuff in here
run = True
while run:
    #turn off the game when we try to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    ball1 = pygame.draw.circle(screen,white,(screen_width/2,screen_height/2),15)
    pygame.display.update() #updating the display so we can see changes