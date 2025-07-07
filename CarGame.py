import pygame
import random,time

def enemy_choose():
    Enmey_choosen=(random.randint(1,2))
    choosen=f"C:\\Users\\ARASH\\Desktop\\CarGame\\Enemy{Enmey_choosen}.png"
    return(choosen)



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
Enemy_x=530
car_x=530
speed=0.2
#---------------------------------run only in startup
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #test
#---------------------------------code goes here
    Enemy_y += speed


    if Enemy_y > 1040:
        Enemy=pygame.image.load(enemy_choose())
        Enemy_y = 0

    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_a]:
        car_x-=1
    if keys[pygame.K_d]:
        car_x+=1
    if keys[pygame.K_w]:
        speed+=0.1
    
    screen.blit(Road,(0, 0))
    screen.blit(car, (car_x, (heigth-200)))
    screen.blit(Enemy,(Enemy_x, Enemy_y))
    
#---------------------------------code goes here
    pygame.display.flip()
pygame.quit()