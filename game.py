import pygame

pygame.init()

screen_height = 500
screen_width = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pool Game")
#colors
white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
#ball consts
ball_rad=15
#game loop, runs when the game runs and we put stuff in here
run = True
while run:
    #turn off the game when we try to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #setting background
    screen.fill(white)
    #creating balls
    ball1 = pygame.draw.circle(screen,blue,(screen_width/2,screen_height/2),ball_rad)
    ball2 = pygame.draw.circle(screen,red,(screen_width/4,screen_height/2),ball_rad)

    pygame.display.update() #updating the display so we can see changes