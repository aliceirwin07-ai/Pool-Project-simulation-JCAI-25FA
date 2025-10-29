import pygame
import random

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
ball1_x = random.randint(int(screen_width*3/4+ball_rad),screen_width-ball_rad)
ball1_y = random.randint(ball_rad,screen_height-ball_rad)
ball1_pos = (ball1_x,ball1_y)
ball2_x = random.randint(ball_rad,int(screen_width/4-ball_rad))
ball2_y = random.randint(ball_rad,screen_height-ball_rad)
ball2_pos = (ball2_x,ball2_y)
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
    ball1 = pygame.draw.circle(screen,blue,ball1_pos,ball_rad)
    ball2 = pygame.draw.circle(screen,red,ball2_pos,ball_rad)

    pygame.display.update() #updating the display so we can see changes