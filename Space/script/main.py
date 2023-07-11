import pygame
from pygame.locals import *
import sys ,os ,time
from random import *

def update_meteor(meteor_list):
    for meteorRec in meteor_list:
        meteorRec.y += round(1000 * dt)
        tela.blit(meteor, meteorRec)

def update_laser(laser_list):
    for laserRec in laser_list:
        tela.blit(lasersurf, laserRec)
        laserRec.y-=round(1000*dt)#padrao é 300
        if laserRec.midbottom[1] < 0:
            laser_list.remove(laserRec) 

def displayScore(tela, font):
    score_text = str(f'S T A R - GAME {pygame.time.get_ticks()//1000}')
    texto = font.render(score_text, True, (0, 0, 255))            
    recText = texto.get_rect(midleft=(30,15))
    tela.blit(texto, recText)    


pygame.init()

pygame.mixer_music.load(os.path.join("assets","Sound","Survivor - Eye Of The Tiger.mp3"))
pygame.mixer_music.set_volume(0.1)
pygame.mixer_music.play(-1)


largura,altura =1200,650
tela = pygame.display.set_mode((largura,altura))
fundo = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
bgr1 = fundo.get_rect(center = ((largura//2,(altura//2))))

nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave, (40,40))
lasersurf = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurf = pygame.transform.scale(lasersurf, (4, 40))

naveRec = nave.get_rect(center=(500, 500))
laser_list = []

meteor_list = []
meteor = pygame.image.load(os.path.join("assets","img","meteor.png")).convert_alpha()
meteor = pygame.transform.scale(meteor, (40,40))
meteorRec = meteor.get_rect(center=(500, 500)) 

pygame.display.set_caption("N A S A")

font = pygame.font.Font(os.path.join("assets","Font","sigmar", "Sigmar-Regular.ttf"),16)
texto = font.render('S T A R - GAME', True,(65,105, 225))
recText = texto.get_rect(center=(100,10))

force_fild = pygame.image.load(os.path.join("assets","img","circle.png")).convert_alpha()
force_fild = pygame.transform.scale(force_fild,(50,50))
fild = force_fild.get_rect(center=(500, 500))

force = False
relogio = pygame.time.Clock()
meteor_spawn = pygame.time.get_ticks()
temp = 0
bate = 0
loop = True
pos_y=400
while loop:
    relogio.tick(120)
    dt = relogio.tick(500)/1000
    start=int(round(time.time()*1000))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            loop = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            laserRec = lasersurf.get_rect(midbottom=naveRec.midtop)
            laser_list.append(laserRec)

        if event.type == pygame.MOUSEMOTION:
            naveRec.center = event.pos

        key = pygame.key.get_pressed()
        if event.type == pygame.MOUSEMOTION and pygame.time.get_ticks()//1000 >= 5:
            fild.center = event.pos
            if key[K_SPACE]:
                force = True

    tela.fill((0,0,0))
    tela.blit(fundo, bgr1)
    if force == True:
        tela.blit(force_fild, fild)
    temp+=1
        
    if pygame.time.get_ticks() - meteor_spawn >= 75:
        meteorRec = meteor.get_rect(center=(randint(40, 1160), 20))
        meteor_list.append(meteorRec)
        meteor_spawn = pygame.time.get_ticks()


    update_meteor(meteor_list)
    
    tela.blit(nave, naveRec)
    
    displayScore(tela=tela,font=font)

    update_laser(laser_list)
    for laserRec in laser_list:
        tela.blit(lasersurf, laserRec)

    for laserRec in laser_list:
        for meteorRec in meteor_list:
            if laserRec.colliderect(meteorRec):
                laser_list.remove(laserRec)
                meteor_list.remove(meteorRec)            

    if force:
        for meteorRec in meteor_list:
            if fild.colliderect(meteorRec):
                meteor_list.remove(meteorRec)
                bate+=1
                if bate >=3:
                    force = False
                    bate = 0

    else:
       for meteorRec in meteor_list:
            if naveRec.colliderect(meteorRec):
                #print("MORREU")
                loop = False

    pygame.display.update()
    end = int(round(time.time()*1000))

pygame.quit()