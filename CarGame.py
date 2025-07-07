import pygame
import random,time

def enemy_choose():
    Enmey_choosen=(random.randint(1,3))
    choosen=f"C:\\Users\\ARASH\\Desktop\\CarGame\\Enemy{Enmey_choosen}.png"
    return(choosen)

def Line_choose():
    Line = random.randint(1, 2)
    if Line == 1:
        return 530
    else:
        return 355


pygame.init()

width=1024
heigth=1040
screen = pygame.display.set_mode((width, heigth))

pygame.display.set_caption("CarGame")
#---------------------------------run only in startup
car=pygame.image.load("C:\\Users\\ARASH\\Desktop\\CarGame\\Car.png").convert_alpha()
Road=pygame.image.load("C:\\Users\\ARASH\\Desktop\\CarGame\\road.png")
Enemy=pygame.image.load(enemy_choose())
Enemy_y=0
car_x=530
speed=0.2
Enemy_x=Line_choose()
Lives=5
crashed = False
#---------------------------------run only in startup
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#---------------------------------code goes here
    keys = pygame.key.get_pressed()
    #speed control
    Enemy_y += speed
    if speed > 5:
        speed = 5

    if speed < 0.1:
        speed=0.1
    #respawn
    if Enemy_y > 1040:
        Enemy=pygame.image.load(enemy_choose())
        Enemy_y = 0
        Enemy_x=Line_choose()
        crashed=False
    
    if car_x>570:
        car_x=570

    if car_x <325:
        car_x=325

    car_rect = car.get_rect(topleft=(car_x, heigth - 200))
    enemy_rect = Enemy.get_rect(topleft=(Enemy_x, Enemy_y))

    car_rect = car.get_rect(topleft=(car_x, heigth - 200))
    enemy_rect = Enemy.get_rect(topleft=(Enemy_x, Enemy_y))

    if car_rect.colliderect(enemy_rect) and not crashed:
        print("💥 برخورد!")
        crashed = True
        Lives-=1
        
    if Lives<1:
        running=False


    #controls
    if keys[pygame.K_a]:
        car_x-=speed*1.5
    if keys[pygame.K_d]:
        car_x+=speed*1.5

    #gas pedal

    if keys[pygame.K_w]:
        speed+=0.002
    else:
        speed-=0.001
    
    if keys[pygame.K_s]:
        speed-=0.002


    screen.blit(Road,(0, 0))
    screen.blit(car, (car_x, (heigth-200)))
    screen.blit(Enemy,(Enemy_x, Enemy_y))
    
#---------------------------------code goes here
    pygame.display.flip()
pygame.quit()