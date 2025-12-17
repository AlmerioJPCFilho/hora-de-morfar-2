import pygame
from pygame.locals import *
from sys import exit 
from personagem import Personagem
import os

#inciando o pygame
pygame.init()

#CORES
preto = (0, 0, 0)

#TELA
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('MacLovin')
fullscreen = False

#RELOGIO
relogio = pygame.time.Clock()

#DIRETORIOS
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')

#SPRITES
todas_sprites = pygame.sprite.Group()
sprites_coletaveis = pygame.sprite.Group()
background = pygame.image.load(os.path.join(diretorio_imagens, 'imagem_fundo.png')).convert()
background = pygame.transform.scale(background, (largura_tela, altura_tela))

#PERSONAGEM
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'sprite_maclovin.png')).convert_alpha()
MacLovin = Personagem(sprite_sheet, largura_tela, altura_tela, fullscreen)
todas_sprites.add(MacLovin)


while True:
    relogio.tick(60)
    tela.fill(preto)
    tela.blit(background, (0,0))
    todas_sprites.draw(tela)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == pygame.K_f:
                MacLovin.fullscreen = True
                MacLovin.image = pygame.transform.scale(MacLovin.image, (600 // 2, 600 // 2))
                largura_tela = 1920
                altura_tela = 1080
                MacLovin.largura_tela = largura_tela
                MacLovin.altura_tela = altura_tela - 100
                background = pygame.transform.scale(background, (largura_tela, altura_tela))
                tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    
            elif event.key == pygame.K_ESCAPE:
                MacLovin.fullscreen = False
                largura_tela = 640
                altura_tela = 480
                MacLovin.largura_tela = largura_tela
                MacLovin.altura_tela = altura_tela
                background = pygame.transform.scale(background, (largura_tela, altura_tela))
                tela = pygame.display.set_mode((largura_tela, altura_tela))

    #movimentação do retangulo
    if pygame.key.get_pressed()[K_a]:
        MacLovin.mover_esquerda()
    if pygame.key.get_pressed()[K_d]:
        MacLovin.mover_direita()
    if pygame.key.get_pressed()[K_w]:
        MacLovin.mover_cima()
    if pygame.key.get_pressed()[K_s]:
        MacLovin.mover_baixo()

    todas_sprites.update()
    pygame.display.flip()

