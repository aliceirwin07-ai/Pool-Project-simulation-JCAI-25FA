import pygame
import random
import math

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

#ball position consts
ball_rad=15
ball1_x = random.randint(int(screen_width*3/4+ball_rad),screen_width-ball_rad) #start on the right 4th of the screen
ball1_y = random.randint(ball_rad,screen_height-ball_rad)   #random y pos
ball1_pos = (ball1_x,ball1_y) #ball pos vector
ball2_x = random.randint(ball_rad,int(screen_width/4-ball_rad)) #start on the left 4th of the screen
ball2_y = random.randint(ball_rad,screen_height-ball_rad)   #random y pos
ball2_pos = (ball2_x,ball2_y) #ball pos vector
#ball velocity consts
ball1_vx = 0
ball1_vy = 0
ball1_vel = (ball1_vx,ball1_vy)
ball2_vx = 0
ball2_vy = 0
ball2_vel = (ball2_vx,ball2_vy)
#ball friction acceleration
ax = 0
ay = 0
friction_accel = 0.005
#game loop, runs when the game runs and we put stuff in here
run = True
while run:
    #turn off the game when we try to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #checking mouse position every frame
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos = (mouse_x, mouse_y)
    #allowing you to "hit" the ball
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:   #if left click
            ball1_vx = 0.005*(mouse_x-ball1_x)
            ball1_vy = 0.005*(mouse_y-ball1_y)
    #friction on the table(NEED TO REWORK)
    # if ball1_vx<=2*friction_accel and ball1_vx<=-2*friction_accel:
    #     ax = 0
    # if ball1_vx>2*friction_accel:
    #     ax = -friction_accel
    # if ball1_vx<-2*friction_accel:
    #     ax = friction_accel
    # if ball1_vy<=2*friction_accel and ball1_vy<=-2*friction_accel:
    #     ay = 0

    # if ball1_vy>2*friction_accel:
    #     ay = -friction_accel
    # if ball1_vy<-2*friction_accel:
    #     ay = friction_accel
    #PLS FIX
    #wall bounces
    if ball1_x - ball_rad < 0 or ball1_x + ball_rad > screen_width:
        ball1_vx = -ball1_vx
    if ball1_y - ball_rad < 0 or ball1_y + ball_rad > screen_height:
        ball1_vy = -ball1_vy
    if ball2_x - ball_rad < 0 or ball2_x + ball_rad > screen_width:
        ball2_vx = -ball2_vx
    if ball2_y - ball_rad < 0 or ball2_y + ball_rad > screen_height:
        ball2_vy = -ball2_vy
    #ball bounces
    dist_balls = math.sqrt((ball1_x-ball2_x)**2+(ball1_y-ball2_y)**2)
    if dist_balls<2*ball_rad:
        print("they collided")
        #add math for coliisions
    #updating positions of the balls
    ball1_x += ball1_vx
    ball1_y += ball1_vy
    ball1_pos = (ball1_x, ball1_y)
    ball2_x += ball2_vx
    ball2_y += ball2_vy
    ball2_pos = (ball2_x, ball2_y)
    #drawing stuff
    screen.fill(white)
    ball1 = pygame.draw.circle(screen,blue,ball1_pos,ball_rad)
    ball2 = pygame.draw.circle(screen,red,ball2_pos,ball_rad)
    #updating the display so we can see changes
    pygame.display.update()