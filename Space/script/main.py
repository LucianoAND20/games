import pygame
from pygame.locals import * 
import sys ,os ,time
pygame.init()
largura,altura =1200,650
tela = pygame.display.set_mode((largura,altura))
fundo = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()

nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave, (40,40))
naveRec = nave.get_rect(center=(500, 500))
bgr1 = fundo.get_rect(center = ((largura//2,(altura//2))))

meteoro = pygame.image.load(os.path.join("assets","img","meteor.png")).convert_alpha()
laser= pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()

pygame.display.set_caption("N A S A")

font = pygame.font.Font(os.path.join("assets","Font","sigmar", "Sigmar-Regular.ttf"),16)
texto = font.render('S T A R - GAME', True,(65,105, 225))
recText = texto.get_rect(center=(100,10))

relogio = pygame.time.Clock()

loop = True
pos_y=400
while loop:
    start=int(round(time.time()*1000))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
        relogio.tick(120)
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            naveRec.center = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            print(f"Tiro:{event.pos}")
    if event.type == pygame.KEYDOWN:
        if pygame.key.get_pressed()[K_SPACE]:
            tela.blit(laser, naveRec)





    tela.fill((0,0,0))
    tela.blit(fundo, bgr1)
    tela.blit(nave, naveRec)
    tela.blit(texto, recText)



    pygame.display.update()
    end = int(round(time.time()*1000))
    #print(f"{end-start} ms")
pygame.quit()