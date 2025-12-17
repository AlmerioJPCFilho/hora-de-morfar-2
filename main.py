import pygame
from pygame.locals import *
from sys import exit
from personagem import Personagem
from coletaveis import Coletaveis

import os

# inciando o pygame
pygame.init()

# CORES
preto = (0, 0, 0)

# TELA
largura_tela = 1280
altura_tela = 720
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('MacLovin')
fullscreen = False

# RELOGIO
relogio = pygame.time.Clock()

# DIRETORIOS
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')

# FONTES
fonte = pygame.font.SysFont('arial', 30, True, False)


# SPRITES
todas_sprites = pygame.sprite.Group()
sprites_coletaveis = pygame.sprite.Group()
background = pygame.image.load(os.path.join(
    diretorio_imagens, 'imagem_fundo.png')).convert()
background = pygame.transform.scale(background, (largura_tela, altura_tela))

# PERSONAGEM
sprite_sheet = pygame.image.load(os.path.join(
    diretorio_imagens, 'sprite_maclovin.png')).convert_alpha()
MacLovin = Personagem(sprite_sheet, largura_tela, altura_tela, fullscreen)
todas_sprites.add(MacLovin)

# COLETAVEIS
# Carteira
sprite_carteira = pygame.image.load(os.path.join(
    diretorio_imagens, 'carteira.png')).convert()
carteira = Coletaveis(largura_tela, altura_tela,
                      sprite_carteira, MacLovin, fullscreen)
todas_sprites.add(carteira)
grupo_carteira = pygame.sprite.Group()
grupo_carteira.add(carteira)

# Cerveja
sprite_cerveja = pygame.image.load(os.path.join(
    diretorio_imagens, 'cerveja.png')).convert_alpha()
cerveja = Coletaveis(largura_tela, altura_tela,
                     sprite_cerveja, MacLovin, fullscreen)
todas_sprites.add(cerveja)
grupo_cerveja = pygame.sprite.Group()
grupo_cerveja.add(cerveja)


def recomecar_jogo():
    global pontos_carteira, pontos_cerveja, jogadorMorreu, self
    pontos_carteira = 0
    pontos_cerveja = 0
    jogadorMorreu = False
    MacLovin.rect.center = (200,altura_tela - 100)


# PONTUAÇÃO
pontos_carteira = 0
img_carteira_pt = pygame.transform.scale(
    sprite_carteira, (sprite_carteira.get_width() // 12, sprite_carteira.get_height() // 12))


pontos_cerveja = 0
img_cerveja_pt = pygame.transform.scale(
    sprite_cerveja, (sprite_cerveja.get_width() // 12, sprite_cerveja.get_height() // 12))
jogadorMorreu = False
telademorte = pygame.image.load('imagens/tela-de-derrota.png')
transformartelademorte = pygame.transform.scale(telademorte, (1280, 720))
jogadorMorreu = False


def gameOver(tela, transformartelademorte):
    global jogadorMorreu
    tela.blit(transformartelademorte, (0, 0))
    som_morte = pygame.mixer.Sound('somdemorte.mp3')
    som_morte.set_volume(0.2)
    som_morte.play()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogadorMorreu = False
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                try:
                    recomecar_jogo()
                except:
                    print("O jogo não pôde ser reiniciado.")


def jogo():
    global pontos_carteira, pontos_cerveja, jogadorMorreu
    while True:
        while jogadorMorreu:
            gameOver(tela, transformartelademorte)
        relogio.tick(60)
        tela.fill(preto)
        tela.blit(background, (0, 0))
        todas_sprites.draw(tela)

        msg_carteira = f': {pontos_carteira}'
        txt_carteira = fonte.render(msg_carteira, False, (255, 255, 255))

        msg_cerveja = f': {pontos_cerveja}'
        txt_cerveja = fonte.render(msg_cerveja, False, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        # movimentação do retangulo
        if pygame.key.get_pressed()[K_a]:
            MacLovin.mover_esquerda()
        if pygame.key.get_pressed()[K_d]:
            MacLovin.mover_direita()
        if pygame.key.get_pressed()[K_w]:
            MacLovin.mover_cima()
        if pygame.key.get_pressed()[K_s]:
            MacLovin.mover_baixo()

        # colisão
        colisao_carteira = pygame.sprite.spritecollide(
            MacLovin, grupo_carteira, False, pygame.sprite.collide_mask)
        if colisao_carteira:
            carteira.colidiu = True
            pontos_carteira += 1

        colisao_cerveja = pygame.sprite.spritecollide(
            MacLovin, grupo_cerveja, False, pygame.sprite.collide_mask)
        if colisao_cerveja:
            cerveja.colidiu = True
            pontos_cerveja += 1

        tela.blit(img_carteira_pt, (20, 20))
        tela.blit(txt_carteira, (75, 18))

        tela.blit(img_cerveja_pt, (20, 70))
        tela.blit(txt_cerveja, (75, 72))

        todas_sprites.update()
        if pontos_cerveja == 2:
            jogadorMorreu = True
        pygame.display.flip()


try:
    jogo()
except:
    print("O jogo não pôde ser iniciado.")
