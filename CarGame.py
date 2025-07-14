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
clock = pygame.time.Clock()
fps = 100
pygame.display.set_caption("CarGame")
car=pygame.image.load("Car.png").convert_alpha()
Road=pygame.image.load("road.png")
GameOver=pygame.image.load("GameOver.png").convert_alpha()
Enemy=pygame.image.load(enemy_choose())
Enemy2=pygame.image.load(enemy_choose())
BOSS=pygame.image.load("BOSS.png").convert_alpha()
Enemy_y=0
Enemy_y2=-300
car_x=530
speed=0.2
Enemy_x=Line_choose()
Enemy_x2=Line_choose()
BOSS_x=Line_choose()
BOSS_y=0
Lives=5
crashed1 = False
crashed2 = False
cars_passed=0
boss_active = False
boss_speed = 8
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

    if boss_active:
        BOSS_y += boss_speed
        if BOSS_y > 1040:
            boss_active = False

    #respawn
    if Enemy_y > 1040:
        Enemy=pygame.image.load(enemy_choose())
        Enemy_y = 0
        Enemy_x=Line_choose()
        crashed1=False
        cars_passed += 1
    #respawn2
    if Enemy_y2 > 1040:
        Enemy2 = pygame.image.load(enemy_choose())
        Enemy_y2 = 0
        cars_passed += 1

        while True:
            Enemy_x2 = Line_choose()
            if Enemy_x2 != Enemy_x:
                break
    

    #boss enemy
    if not boss_active and cars_passed >= 5:
        boss_active = True
        cars_passed = 0
        BOSS_x = Line_choose()
        BOSS_y = -200



    
    #Keep the car in Line
    if car_x>570:
        car_x=570

    if car_x <325:
        car_x=325

    #car collision1
    car_rect = car.get_rect(topleft=(car_x, heigth - 200)).inflate(-20, -20)
    enemy_rect = Enemy.get_rect(topleft=(Enemy_x, Enemy_y)).inflate(-20, -20)
    if car_rect.colliderect(enemy_rect) and not crashed1:
        print("CRASH")
        crashed1 = True
        Lives-=1

    #car collision2
    enemy_rect2 = Enemy.get_rect(topleft=(Enemy_x2, Enemy_y2))
    if car_rect.colliderect(enemy_rect2) and not crashed2:
        print("CRASH")
        crashed2 = True
        Lives-=1


    #boss collision
    if boss_active:
        boss_rect = BOSS.get_rect(topleft=(BOSS_x, BOSS_y)).inflate(-30, -30)
        if car_rect.colliderect(boss_rect):
            print("BOSS CRASH")
            Lives -= 2
            boss_active = False

    #Gameover Logic
    if Lives < 1:
        screen.blit(GameOver, (width // 2 - GameOver.get_width() // 2, heigth // 2 - GameOver.get_height() // 2))
        pygame.display.flip()
        time.sleep(2)
        running = False
        


    #controls
    if keys[pygame.K_a]:
        car_x-=speed*1.5
    if keys[pygame.K_d]:
        car_x+=speed*1.5

    #gas pedal

    if keys[pygame.K_w]:
        speed+=0.03
    else:
        speed-=0.0001
    
    if keys[pygame.K_s]:
        speed-=0.04

    #Image loaderaa
    screen.blit(Road,(0, 0))
    screen.blit(car, (car_x, (heigth-200)))
    screen.blit(Enemy,(Enemy_x, Enemy_y))
    screen.blit(Enemy2,(Enemy_x2, Enemy_y2))
    if boss_active:
        screen.blit(BOSS, (BOSS_x, BOSS_y))

#---------------------------------code goes here


    clock.tick(fps)
    pygame.display.flip()
pygame.quit()