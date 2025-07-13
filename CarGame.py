import pygame,random,time

def enemy_choose():
    Enmey_choosen=(random.randint(1,3))
    choosen=f"Enemy{Enmey_choosen}.png"
    return(choosen)

def Line_choose():
    Line = random.randint(1, 2)
    if Line == 1:
        return 530
    else:
        return 355



pygame.init()
#---------------------------------run only in startup
width=1024
heigth=1040
screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("CarGame")
car=pygame.image.load("Car.png").convert_alpha()
Road=pygame.image.load("road.png")
GameOver=pygame.image.load("GameOver.png").convert_alpha()
Enemy=pygame.image.load(enemy_choose())
Enemy2=pygame.image.load(enemy_choose())
Enemy_y=0
Enemy_y2=0
car_x=530
speed=0.2
Enemy_x=Line_choose()
Enemy_x2=Line_choose()
Lives=5
crashed = False
#---------------------------------run only in startup




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





#---------------------------------code goes here

    #register Keys
    keys = pygame.key.get_pressed()


    #speed control
    Enemy_y += speed
    Enemy_y2 += speed+0.3
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
    
    #respawn2
    if Enemy_y2 > 1040:
        Enemy2=pygame.image.load(enemy_choose())
        Enemy_y2 = 0
        Enemy_x2=Line_choose()+1
        if Enemy_x2 == 3:
            Enemy_x2 = 1
        crashed=False

    
    #Keep the car in Line
    if car_x>570:
        car_x=570

    if car_x <325:
        car_x=325

    #car collision
    car_rect = car.get_rect(topleft=(car_x, heigth - 200))
    enemy_rect = Enemy.get_rect(topleft=(Enemy_x, Enemy_y))
    if car_rect.colliderect(enemy_rect) and not crashed:
        print("CRASH")
        crashed = True
        Lives-=1
    
    #Gameover Logic
    if Lives<1:
        screen.blit(GameOver,(20,20))
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

    #Image loaderaa
    screen.blit(Road,(0, 0))
    screen.blit(car, (car_x, (heigth-200)))
    screen.blit(Enemy,(Enemy_x, Enemy_y))
    screen.blit(Enemy2,(Enemy_x2, Enemy_y2))
    
#---------------------------------code goes here



    pygame.display.flip()
pygame.quit()