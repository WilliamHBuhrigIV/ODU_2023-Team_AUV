from ast import AsyncFunctionDef
from asyncio.windows_events import NULL
from cmath import isclose
from math import trunc
from pickle import FALSE
import sys
from winreg import KEY_CREATE_SUB_KEY
import pygame
import socket
import time
from pygame.locals import *

def draw_Screen():
    # Control Display
    pygame.draw.rect(screen,x_y_grid_color, x_y_grid)
    pygame.draw.rect(screen,thrust_grid_color, thrust_grid)
    pygame.draw.rect(screen,motor1_grid_color, motor1_grid)
    pygame.draw.rect(screen,motor2_grid_color, motor2_grid)
    pygame.draw.rect(screen,motor3_grid_color, motor3_grid)
    pygame.draw.rect(screen,motor4_grid_color, motor4_grid)

    # Steering Window
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(margin_size-line_size,margin_size-line_size,line_size,bar_height+2*line_size))    # Left
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(margin_size-line_size,margin_size-line_size,bar_height+2*line_size,line_size))    # Top
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(margin_size-line_size,margin_size+bar_height,bar_height+2*line_size,line_size))   # Bottom
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(margin_size+bar_height,margin_size-line_size,line_size,bar_height+2*line_size))   # Right
    screen.blit(pygame.font.SysFont(FONT,int(bar_height/10)).render('S',False,(255,255,255)),(margin_size,margin_size))
    # Thrust Window
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(2*margin_size+bar_height-line_size,margin_size-line_size,line_size,bar_height+2*line_size))           # Left
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(2*margin_size+bar_height+bar_width,margin_size-line_size,line_size,bar_height+2*line_size))           # Right
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(2*margin_size+bar_height-line_size,margin_size-line_size,bar_width+line_size,line_size))              # Top
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(2*margin_size+bar_height-line_size,margin_size+bar_height,bar_width+line_size,line_size))             # Bottom
    #pygame.draw.rect(screen,[255,255,255],pygame.Rect(2*margin_size+bar_height,margin_size+bar_height/2,bar_width,line_size))                               # Center Line
    screen.blit(pygame.font.SysFont(FONT,int(bar_height/10)).render('T',False,(255,255,255)),(2*margin_size+margin_size/4+bar_height,margin_size))

    #Motor Number 1
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(3*margin_size+bar_height+bar_width-line_size,margin_size-line_size,line_size,bar_height/2+2*line_size-margin_size/2))     # Left
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(3*margin_size+bar_height+2*bar_width,margin_size-line_size,line_size,bar_height/2+2*line_size-margin_size/2))   # Right
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(3*margin_size+bar_height+bar_width-line_size,margin_size-line_size,bar_width+line_size,line_size))                        # Top
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(3*margin_size+bar_height+bar_width-line_size,margin_size+bar_height/2-margin_size/2,bar_width+line_size,line_size))       # Bottom
    screen.blit(pygame.font.SysFont(FONT,int(bar_height/10)).render('1',False,(255,255,255)),(3*margin_size+margin_size/4+bar_height+bar_width,margin_size))
    #Motor Number 2
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(3*margin_size+bar_height+bar_width-line_size,3*margin_size/2-line_size+bar_height/2,line_size,bar_height/2+2*line_size-margin_size/2))     # Left
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(3*margin_size+bar_height+2*bar_width,3*margin_size/2-line_size+bar_height/2,line_size,bar_height/2+2*line_size-margin_size/2))   # Right
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(3*margin_size+bar_height+bar_width-line_size,3*margin_size/2-line_size+bar_height/2,bar_width+line_size,line_size))                        # Top
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(3*margin_size+bar_height+bar_width-line_size,margin_size+bar_height,bar_width+line_size,line_size))       # Bottom
    screen.blit(pygame.font.SysFont(FONT,int(bar_height/10)).render('2',False,(255,255,255)),(3*margin_size+margin_size/4+bar_height+bar_width,3*margin_size/2+bar_height/2))
    #Motor Number 3
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(4*margin_size+bar_height+2*bar_width-line_size,margin_size-line_size,line_size,bar_height/2+2*line_size-margin_size/2))     # Left
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(4*margin_size+bar_height+3*bar_width,margin_size-line_size,line_size,bar_height/2+2*line_size-margin_size/2))   # Right
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(4*margin_size+bar_height+2*bar_width-line_size,margin_size-line_size,bar_width+line_size,line_size))                        # Top
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(4*margin_size+bar_height+2*bar_width-line_size,margin_size+bar_height/2-margin_size/2,bar_width+line_size,line_size))       # Bottom
    screen.blit(pygame.font.SysFont(FONT,int(bar_height/10)).render('3',False,(255,255,255)),(4*margin_size+margin_size/4+bar_height+2*bar_width,margin_size))
    #Motor Number 4
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(4*margin_size+bar_height+2*bar_width-line_size,3*margin_size/2-line_size+bar_height/2,line_size,bar_height/2+2*line_size-margin_size/2))     # Left
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(4*margin_size+bar_height+3*bar_width,3*margin_size/2-line_size+bar_height/2,line_size,bar_height/2+2*line_size-margin_size/2))   # Right
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(4*margin_size+bar_height+2*bar_width-line_size,3*margin_size/2-line_size+bar_height/2,bar_width+line_size,line_size))                        # Top
    pygame.draw.rect(screen,[255,255,255],pygame.Rect(4*margin_size+bar_height+2*bar_width-line_size,margin_size+bar_height,bar_width+line_size,line_size))       # Bottom
    screen.blit(pygame.font.SysFont(FONT,int(bar_height/10)).render('4',False,(255,255,255)),(4*margin_size+margin_size/4+bar_height+2*bar_width,3*margin_size/2+bar_height/2))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(1)
clientsocket, address = s.accept()
print(f"Connection from {address} has been established!")
pygame.init()
pygame.display.set_caption('game base')
STATE_CONTROLLER = "PS3"
FONT = "Times New Roman"
scale_factor = 3
line_size = 1 #Pixels
margin_size = 3 * scale_factor
bar_width = 30 * scale_factor
bar_height = 100 * scale_factor
small_bar_height = (bar_height - 10 )*scale_factor
screen_size_x = (5*margin_size+3*bar_width+bar_height)
screen_size_y = (bar_height+2*margin_size)
cursor_size = 2*scale_factor
screen = pygame.display.set_mode((screen_size_x,screen_size_y), 0, 32)
clock = pygame.time.Clock()

pygame.joystick.init()
joystick = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

initalization_value = 0
x_y_grid = pygame.Rect(initalization_value,initalization_value,cursor_size,cursor_size)
x_y_grid_color = (initalization_value,initalization_value,initalization_value)
thrust_grid = pygame.Rect(2*margin_size+bar_height,initalization_value,bar_width,initalization_value)
thrust_grid_color = (initalization_value,initalization_value,initalization_value)
motion = [initalization_value,initalization_value,initalization_value,initalization_value,initalization_value]
dead_zone = 0.025
motor1 = initalization_value
motor1_grid = pygame.Rect(3*margin_size+bar_height+bar_width,initalization_value,bar_width,initalization_value)
motor1_grid_color = (initalization_value,initalization_value,initalization_value)
motor2 = initalization_value
motor2_grid = pygame.Rect(3*margin_size+bar_height+bar_width,initalization_value,bar_width,initalization_value)
motor2_grid_color = (initalization_value,initalization_value,initalization_value)
motor3 = initalization_value
motor3_grid = pygame.Rect(4*margin_size+bar_height+2*bar_width,initalization_value,bar_width,initalization_value)
motor3_grid_color = (initalization_value,initalization_value,initalization_value)
motor4 = initalization_value
motor4_grid = pygame.Rect(4*margin_size+bar_height+2*bar_width,initalization_value,bar_width,initalization_value)
motor4_grid_color = (initalization_value,initalization_value,initalization_value)
thrust_vector = initalization_value
motor_max_update_rate = 400 #hz

#Axis 0: Up    (+) Down  (-)
#Axis 1: Left  (+) Right (-)
#Axis 2: Front (-) Back  (+)
PAUSE = False
while True:
    screen.fill((0,0,0)) #Wipes Screen
    draw_Screen()
    pygame.display.update()
    if PAUSE:
        for i in range(len(motion)):
            motion[i] = 0
        pygame.display.update()
    while PAUSE:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p:
                    PAUSE = False
    if STATE_CONTROLLER == "X56":
        NULL    
    elif STATE_CONTROLLER == "PS3":
        motion[2] = motion[4]-motion[3]

    x_y_grid.x = motion[0]*(bar_height-cursor_size)/2+(margin_size+bar_height/2)-cursor_size/2
    x_y_grid.y = motion[1]*(bar_height-cursor_size)/2+(margin_size+bar_height/2)-cursor_size/2
    x_y_grid_color = ((motion[2]+1)*255/2,0,abs(motion[2]-1)*255/2)

    if motion[2] > 0:
        thrust_grid.y = margin_size+bar_height/2-bar_height*motion[2]/2
        thrust_grid.height = bar_height*motion[2]/2
        thrust_grid_color = (0,0,(motion[2]+1)*150/2+50)
    elif motion[2] < 0:
        thrust_grid.y = margin_size+bar_height/2
        thrust_grid.height = bar_height*abs(motion[2])/2
        thrust_grid_color = (abs(motion[2]-1)*150/2+50,0,0)
    else:
        thrust_grid.y = 0
        thrust_grid.height = 0
        thrust_grid_color = (127,0,127)

    if motor1 > 0.5:
        motor1_grid.y = margin_size+bar_height/4-bar_height*(motor1-0.5)/2
        motor1_grid.height = bar_height*(motor1-0.5)/2-margin_size/4
        motor1_grid_color = (0,0,150*(motor1-0.5)*2+50)
    elif motor1 < 0.5:
        motor1_grid.y = margin_size+bar_height/4-margin_size/4
        motor1_grid.height = bar_height*(0.5 - motor1)/2-margin_size/4
        motor1_grid_color = (150*(1-motor1*2)+50,0,0)
    else:
        motor1_grid.y = 0
        motor1_grid.height = 0

    if motor2 > 0.5:
        motor2_grid.y = 3*margin_size/2+bar_height/2+bar_height/4-bar_height*(motor2-0.5)/2
        motor2_grid.height = bar_height*(motor2-0.5)/2-margin_size/2
        motor2_grid_color = (0,0,150*(motor2-0.5)*2+50)
    elif motor2 < 0.5:
        motor2_grid.y = 2*margin_size+bar_height/2+bar_height/4-margin_size/2
        motor2_grid.height = bar_height*(0.5 - motor2)/2-margin_size/2
        motor2_grid_color = (150*(1-motor2*2)+50,0,0)
    else:
        motor2_grid.y = 0
        motor2_grid.height = 0

    if motor3 > 0.5:
        motor3_grid.y = margin_size+bar_height/4-bar_height*(motor3-0.5)/2
        motor3_grid.height = bar_height*(motor3-0.5)/2-margin_size/4
        motor3_grid_color = (0,0,150*(motor3-0.5)*2+50)
    elif motor3 < 0.5:
        motor3_grid.y = margin_size+bar_height/4-margin_size/4
        motor3_grid.height = bar_height*(0.5 - motor3)/2-margin_size/4
        motor3_grid_color = (150*(1-motor3*2)+50,0,0)
    else:
        motor3_grid.y = 0
        motor3_grid.height = 0

    if motor4 > 0.5:
        motor4_grid.y = 3*margin_size/2+bar_height/2+bar_height/4-bar_height*(motor4-0.5)/2
        motor4_grid.height = bar_height*(motor4-0.5)/2-margin_size/2
        motor4_grid_color = (0,0,150*(motor4-0.5)*2+50)
    elif motor4 < 0.5:
        motor4_grid.y = 2*margin_size+bar_height/2+bar_height/4-margin_size/2
        motor4_grid.height = bar_height*(0.5 - motor4)/2-margin_size/2
        motor4_grid_color = (150*(1-motor4*2)+50,0,0)
    else:
        motor4_grid.y = 0
        motor4_grid.height = 0

    motor1 = ((motion[0]+1)/2)
    motor2 = (abs(motion[0]-1)/2)
    motor3 = (abs(motion[1]-1)/2)
    motor4 = ((motion[1]+1)/2)
    #print("Motor 1: ",motor1,"Motor 2: ",motor2,"Motor 3: ",motor3,"Motor 4: ",motor4)
    motor1factor = (motion[2]*motor1+1)/2
    motor2factor = (motion[2]*motor2+1)/2
    motor3factor = (motion[2]*motor3+1)/2
    motor4factor = (motion[2]*motor4+1)/2
    #print("Motor 1: ",motor1factor,"Motor 2: ",motor2factor,"Motor 3: ",motor3factor,"Motor 4: ",motor4factor)
    motor1data = trunc(motor1factor*1000)
    motor2data = trunc(motor2factor*1000)
    motor3data = trunc(motor3factor*1000)
    motor4data = trunc(motor4factor*1000)
    
    max_transmission_frequency = 1000 #hz
    clientsocket.send(bytes(str(motor1data),"utf-8"))
    time.sleep(1/(max_transmission_frequency*4))
    clientsocket.send(bytes(str(motor2data),"utf-8"))
    time.sleep(1/(max_transmission_frequency*4))
    clientsocket.send(bytes(str(motor3data),"utf-8"))
    time.sleep(1/(max_transmission_frequency*4))
    clientsocket.send(bytes(str(motor4data),"utf-8"))
    time.sleep(1/(max_transmission_frequency*4))
    time.sleep(1/motor_max_update_rate)

    for event in pygame.event.get():
        #if event.type == JOYBUTTONDOWN:
            #if event.button == 1: #Eventually this Will be the Kill Drone Button
        if event.type == JOYAXISMOTION:
            if STATE_CONTROLLER == "X56":
                if event.axis == 0:
                    motion[0] = event.value
                if event.axis == 1:
                    motion[1] = event.value
                if event.axis == 4:
                    motion[2] = event.value
            elif STATE_CONTROLLER == "PS3":
                #if event.axis == 0: #LEFT/RIGHT Left Stick
                #if event.axis == 1: #UP/DOWN Left Stick
                if event.axis == 2: #LEFT/RIGHT Right Stick
                    motion[0] = event.value
                if event.axis == 3: #UP/DOWN Right Stick
                    motion[1] = event.value
                if event.axis == 4: #Left Bumper
                    motion[3] = (event.value+1)/2
                if event.axis == 5: #Right Bumper
                    motion[4] = (event.value+1)/2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_k:
                if STATE_CONTROLLER == "X56":
                    STATE_CONTROLLER == "PS3"
                    print("Switching to Controller")
                elif STATE_CONTROLLER == "PS3":
                    STATE_CONTROLLER == "X56"
                    print("Switching to Joystick")
            if event.key == K_p:
                PAUSE = True
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                socket.close()

    for i in range(len(motion)):
        if abs(motion[i]) < dead_zone:
                motion[i] = 0
        elif abs(motion[i]) > 1 - dead_zone:
            if motion[i] > 0:
                motion[i] = 1
            else:
                motion[i] = -1
        elif abs(motion[i]) < dead_zone-1:
            if motion[i] > 0:
                motion[i] = 1
            else:
                motion[i] = -1
    clock.tick(60)