import pygame
import random
import math
#initialize the screen
pygame.init()
#set screen variables and stuff
screen_height = 500
screen_width = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pool Game")
#colors(NEED TO CHANGE BALL COLORS TO BE LESS UGLY)
white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
#ball starting position consts
ball_rad=15
ball1_x = random.randint(int(screen_width*3/4+ball_rad),screen_width-ball_rad) #start on the right 4th of the screen
ball1_y = random.randint(ball_rad,screen_height-ball_rad)   #random y pos
ball1_pos = (ball1_x,ball1_y) #ball pos vector
ball2_x = random.randint(ball_rad,int(screen_width/4-ball_rad)) #start on the left 4th of the screen
ball2_y = random.randint(ball_rad,screen_height-ball_rad)   #random y pos
ball2_pos = (ball2_x,ball2_y) #ball pos vector
#ball starting velocity consts
ball1_speed = 0
ball2_speed = 0
ball1_vx = 0
ball1_vy = 0
ball1_vel = (ball1_vx,ball1_vy)
ball2_vx = 0
ball2_vy = 0
ball2_vel = (ball2_vx,ball2_vy)
#ball acceleration consts
friction_accel = 0.001  #acceleration due to friction

#game loop, runs when the game runs and we put stuff in here
run = True
while run:
    #turn off the game when we try to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #checking mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos = (mouse_x, mouse_y)
    #allowing you to "hit" the ball
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:   #if left click
            ball1_vx = 0.005*(mouse_x-ball1_x) #making the velocities proportional to the dist you click from.
            ball1_vy = 0.005*(mouse_y-ball1_y)

    #friction on the table 
    ball1_speed = math.sqrt(ball1_vx**2+ball1_vy**2)
    ball2_speed = math.sqrt(ball2_vx**2+ball2_vy**2)
    #updating direction velocity of the balls
    #checking if we need to apply acceleration
    if ball1_speed > friction_accel:    #check if speed > accel(if speed is < accel we treat it as being 0 because it's negligible)
        nx = ball1_vx / ball1_speed   # normalized vx
        ny = ball1_vy / ball1_speed   # normalized vy
        ball1_vx -= friction_accel * nx
        ball1_vy -= friction_accel * ny
    if ball2_speed > friction_accel:    #check if speed > accel(if speed is < accel we treat it as being 0 because it's negligible)
        nx = ball2_vx / ball2_speed   # normalized vx
        ny = ball2_vy / ball2_speed   # normalized vy
        ball2_vx -= friction_accel * nx
        ball2_vy -= friction_accel * ny
    #rounding velocity to 0 if the speed is too low
    if ball1_speed <= friction_accel:
        ball1_vx = 0
        ball1_vy = 0
    if ball2_speed <= friction_accel:
        ball2_vx = 0
        ball2_vy = 0

    #wall bounces(assuming no energy lost in a bounce)
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
    #FIX COLLISIONS
    if dist_balls<=2*ball_rad:
        theta = math.atan2(ball1_y-ball2_y,ball1_x-ball2_x)
        #use a rotation matrix to turn the problem into the 1d scenario
        rot_ball1_vx = ball1_vx*math.cos(theta)+ball1_vy*math.sin(theta)
        rot_ball1_vy = ball1_vy*math.cos(theta)-ball1_vx*math.sin(theta)
        rot_ball2_vx = ball2_vx*math.cos(theta)+ball2_vy*math.sin(theta)
        rot_ball2_vy = ball2_vy*math.cos(theta)-ball2_vx*math.sin(theta)
        #switch them because m1=m2
        rot_ball1_vx = ball2_vx*math.cos(theta)+ball2_vy*math.sin(theta)
        rot_ball2_vx = ball1_vx*math.cos(theta)+ball1_vy*math.sin(theta)
        #apply inverse rotation matrix
        ball1_vx = rot_ball1_vx*math.cos(theta)-rot_ball1_vy*math.sin(theta)
        ball1_vy = rot_ball1_vx*math.sin(theta)+rot_ball1_vy*math.cos(theta)
        ball2_vx = rot_ball2_vx*math.cos(theta)-rot_ball2_vy*math.sin(theta)
        ball2_vy = rot_ball2_vx*math.sin(theta)+rot_ball2_vy*math.cos(theta)

    #updating positions of the balls
    ball1_x += ball1_vx
    ball1_y += ball1_vy
    ball1_pos = (ball1_x, ball1_y)
    ball2_x += ball2_vx
    ball2_y += ball2_vy
    ball2_pos = (ball2_x, ball2_y)
    #drawing balls at their new pos + fill screen
    screen.fill(white)
    ball1 = pygame.draw.circle(screen,blue,ball1_pos,ball_rad)
    ball2 = pygame.draw.circle(screen,red,ball2_pos,ball_rad)
    #updating the display so we can see changes
    pygame.display.update()