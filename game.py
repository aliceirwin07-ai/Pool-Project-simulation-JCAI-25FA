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
#ball position consts
ball_rad=15
#ball1
ball1_x = random.randint(int(screen_width*3/4+ball_rad),screen_width-ball_rad) #start on the right 4th of the screen
ball1_y = random.randint(ball_rad,screen_height-ball_rad)   #random y pos
ball1_pos = (ball1_x,ball1_y) #ball pos vector
#ball2
ball2_x = random.randint(ball_rad,int(screen_width/4-ball_rad)) #start on the left 4th of the screen
ball2_y = random.randint(ball_rad,screen_height-ball_rad)   #random y pos
ball2_pos = (ball2_x,ball2_y) #ball pos vector
#ball velocity consts
#ball1
ball1_vx = 0
ball1_vy = 0
ball1_vel = (ball1_vx,ball1_vy)
#ball2
ball2_vx = 0
ball2_vy = 0
ball2_vel = (ball2_vx,ball2_vy)
#ball direction consts: theta reference is right to down dir
ball1_vtheta = 0   #just setting to 0 as a placeholder  
ball2_vtheta = 0   #just setting to 0 as a placeholder
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

    #friction on the table(NEED TO REWORK)  
    ball1_speed = math.sqrt(ball1_vx**2+ball1_vy**2)
    ball2_speed = math.sqrt(ball2_vx**2+ball2_vy**2)
    #updating direction velocity of the balls
    #ball1 theta
    if ball1_vx !=0:    #theta is undef if vx=0
        ball1_vtheta = math.atan(ball1_vy/ball1_vx) #angle from horizontal to down
    if ball1_vx == 0 and ball1_vy > friction_accel: #if v points straight
        ball1_vtheta = -math.pi/2
    if ball1_vx == 0 and ball1_vy < friction_accel: #if v points straight
        ball1_vtheta = math.pi/2
        #ball2 theta
    if ball2_vx !=0:    #theta is undef if vx=0
        ball2_vtheta = math.atan(ball2_vy/ball2_vx) #angle from horizontal to down
    if ball2_vx == 0 and ball2_vy > friction_accel: #if v points straight
        ball2_vtheta = -math.pi/2
    if ball2_vx == 0 and ball2_vy < friction_accel: #if v points straight
        ball2_vtheta = math.pi/2
    #checking if we need to apply acceleration
    #ball1
    if ball1_speed > friction_accel:#check if speed > accel(if the speed is < accel we treat it as being 0 because it's negligible)
        if ball1_vx > friction_accel and ball1_vy > friction_accel: #case when vx,ball2_vy are pos
            ball1_vx-=friction_accel*math.cos(ball1_vtheta)
            ball1_vy-=friction_accel*math.sin(ball1_vtheta)
        if ball1_vx < friction_accel and ball1_vy < friction_accel: #case when vx,ball2_vy are neg
            ball1_vx+=friction_accel*math.cos(ball1_vtheta)
            ball1_vy+=friction_accel*math.sin(ball1_vtheta)
        if ball1_vx < friction_accel and ball1_vy > friction_accel: #case when vx pos and vy neg
            ball1_vx+=friction_accel*math.cos(ball1_vtheta)
            ball1_vy+=friction_accel*math.sin(ball1_vtheta)
        if ball1_vx > friction_accel and ball1_vy < friction_accel: #case when vx neg and vy pos
            ball1_vx-=friction_accel*math.cos(ball1_vtheta)
            ball1_vy-=friction_accel*math.sin(ball1_vtheta)
    #ball2
    if ball2_speed > friction_accel: #check if speed > accel (if speed < accel treat as 0)
        if ball2_vx > friction_accel and ball2_vy > friction_accel: #vx, vy positive
            ball2_vx -= friction_accel * math.cos(ball2_vtheta)
            ball2_vy -= friction_accel * math.sin(ball2_vtheta)
        if ball2_vx < friction_accel and ball2_vy < friction_accel: #vx, vy negative
            ball2_vx += friction_accel * math.cos(ball2_vtheta)
            ball2_vy += friction_accel * math.sin(ball2_vtheta)
        if ball2_vx < friction_accel and ball2_vy > friction_accel: #vx negative, vy positive
            ball2_vx += friction_accel * math.cos(ball2_vtheta)
            ball2_vy += friction_accel * math.sin(ball2_vtheta)
        if ball2_vx > friction_accel and ball2_vy < friction_accel: #vx positive, vy negative
            ball2_vx -= friction_accel * math.cos(ball2_vtheta)
            ball2_vy -= friction_accel * math.sin(ball2_vtheta)
    #rounding velocity to 0 if the speed is too low
    #ball1
    if ball1_speed <= friction_accel:
        ball1_vx = 0
        ball1_vy = 0
    #ball2
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
    normal_x = (ball1_x-ball2_x)/dist_balls
    normal_y = (ball1_y-ball2_y)/dist_balls
    normal = (normal_x,normal_y)    #points to ball2 from ball1
    delta = (ball1_vx - ball2_vx)*normal_x + (ball1_vy - ball2_vy)*normal_y #scalar of relative velcoity

    #FIX COLLISIONS
    if dist_balls<=2*ball_rad:
        print("they collided")

        # overlap = 2*ball_rad - dist_balls
        #need to work on this math, possibly do better work on paper?
        # ball1_vx = ball1_vx - delta * normal_x
        # ball1_vy = ball1_vy - delta * normal_y
        # ball2_vx = ball2_vx - delta * normal_x
        # ball2_vy = ball2_vy - delta * normal_y

        #trying to move balls away from each other if they're inside each other
        # # ball1_x -= (normal_x * overlap)/2
        # # ball1_y -= (normal_y * overlap)/2
        # # ball2_x += (normal_x * overlap)/2
        # # ball2_y += (normal_y * overlap)/2

    #updating positions of the balls
    ball1_x += ball1_vx
    ball1_y += ball1_vy
    ball1_pos = (ball1_x, ball1_y)
    ball2_x += ball2_vx
    ball2_y += ball2_vy
    ball2_pos = (ball2_x, ball2_y)
    #drawing balls + fill screen
    screen.fill(white)
    ball1 = pygame.draw.circle(screen,blue,ball1_pos,ball_rad)
    ball2 = pygame.draw.circle(screen,red,ball2_pos,ball_rad)
    #updating the display so we can see changes
    pygame.display.update()