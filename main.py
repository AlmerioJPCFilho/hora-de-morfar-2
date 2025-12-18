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
pygame.display.set_caption('The adventures of McLovin')
fullscreen = False

# RELOGIO
relogio = pygame.time.Clock()

# DIRETORIOS
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_audios = os.path.join(diretorio_principal, 'audios')

# FONTES
fonte = pygame.font.SysFont('arial', 30, True, False)


# SPRITES
todas_sprites = pygame.sprite.Group()
sprites_coletaveis = pygame.sprite.Group()
background = pygame.image.load(os.path.join(
    diretorio_imagens, 'imagem-fundo.png')).convert()
background = pygame.transform.scale(background, (largura_tela, altura_tela))

# SONS
musica_titulo = pygame.mixer.Sound(os.path.join(
    diretorio_audios, 'jonny-fabisak-title-cube.mp3'))
musica_jogo = pygame.mixer.Sound(os.path.join(
    diretorio_audios, 'jonny-fabisak-blocky-blues.mp3'))
musica_jogo.set_volume(0.5)
musica_jogo_rodando = False
som_coleta1 = pygame.mixer.Sound(
    os.path.join(diretorio_audios, 'cube-sfx-1.mp3'))
som_coleta2 = pygame.mixer.Sound(
    os.path.join(diretorio_audios, 'cube-sfx-2.mp3'))
som_coleta3 = pygame.mixer.Sound(
    os.path.join(diretorio_audios, 'cube-sfx-3.mp3'))
som_morte = pygame.mixer.Sound(os.path.join(diretorio_audios, 'som-morte.mp3'))
som_morte.set_volume(0.5)

# PERSONAGEM
sprite_sheet = pygame.image.load(os.path.join(
    diretorio_imagens, 'sprite-mclovin.png')).convert_alpha()
McLovin = Personagem(sprite_sheet, largura_tela, altura_tela, fullscreen)
todas_sprites.add(McLovin)

# COLETAVEIS
# Carteira
sprite_carteira = pygame.image.load(os.path.join(
    diretorio_imagens, 'identidade.png')).convert()
carteira = Coletaveis(largura_tela, altura_tela,
                      sprite_carteira, McLovin, fullscreen)
todas_sprites.add(carteira)
grupo_carteira = pygame.sprite.Group()
grupo_carteira.add(carteira)

# Cerveja
sprite_cerveja = pygame.image.load(os.path.join(
    diretorio_imagens, 'cerveja.png')).convert_alpha()
cerveja = Coletaveis(largura_tela, altura_tela,
                     sprite_cerveja, McLovin, fullscreen)
todas_sprites.add(cerveja)
grupo_cerveja = pygame.sprite.Group()
grupo_cerveja.add(cerveja)

telainicial = pygame.image.load(os.path.join(
    diretorio_imagens, 'tela-inicial.png')).convert()
transformarTelaInicial = pygame.transform.scale(telainicial, (1280, 720))


def iniciar_jogo():
    retanguloTransparente = pygame.Surface((320, 60))
    retanguloTransparente.set_alpha(100)
    retanguloTransparente.fill((255, 255, 255)) 
    rect_jogar = pygame.Rect(480, 420, 320, 60)
    rect_sair = pygame.Rect(480, 510, 320, 60)

    while True:
        tela.blit(transformarTelaInicial, (0, 0))
        
        mouse = pygame.mouse.get_pos()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if rect_jogar.collidepoint(mouse):
                        try:
                            jogo()
                        except:
                            print("O jogo não pôde ser iniciado.")
                    
                    if rect_sair.collidepoint(mouse):
                        pygame.quit()
                        exit()
        pygame.display.update()

def recomecar_jogo():
    global pontos_carteira, pontos_cerveja, jogadorMorreu, self
    pontos_carteira = 0
    pontos_cerveja = 0
    jogadorMorreu = False
    McLovin.rect.center = (200, altura_tela - 100)


# PONTUAÇÃO
pontos_carteira = 0
img_carteira_pt = pygame.transform.scale(
    sprite_carteira, (sprite_carteira.get_width() // 12, sprite_carteira.get_height() // 12))

pontos_cerveja = 0
img_cerveja_pt = pygame.transform.scale(
    sprite_cerveja, (sprite_cerveja.get_width() // 12, sprite_cerveja.get_height() // 12))
jogadorMorreu = False
telademorte = pygame.image.load(os.path.join(
    diretorio_imagens, 'tela-derrota.png')).convert()
transformartelademorte = pygame.transform.scale(telademorte, (1280, 720))
jogadorMorreu = False


def gameOver(tela, transformartelademorte):
    global jogadorMorreu, musica_jogo_rodando
    musica_jogo.stop()
    musica_jogo_rodando = False
    som_morte.play()
    esperando_reiniciar = True
    while esperando_reiniciar:
        relogio.tick(30)
        tela.blit(transformartelademorte, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogadorMorreu = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    esperando_reiniciar = False
                    try:
                        som_morte.stop()
                        recomecar_jogo()
                    except:
                        print("O jogo não pôde ser reiniciado.")


def jogo():
    global pontos_carteira, pontos_cerveja, jogadorMorreu, som_coleta1, som_coleta2, som_coleta3, musica_jogo_rodando
    while True:
        if jogadorMorreu:
            gameOver(tela, transformartelademorte)
        if not musica_jogo_rodando:
            musica_jogo.play(-1)
            musica_jogo_rodando = True
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
            McLovin.mover_esquerda()
        if pygame.key.get_pressed()[K_d]:
            McLovin.mover_direita()
        if pygame.key.get_pressed()[K_w]:
            McLovin.mover_cima()
        if pygame.key.get_pressed()[K_s]:
            McLovin.mover_baixo()

        # colisão
        colisao_carteira = pygame.sprite.spritecollide(
            McLovin, grupo_carteira, False, pygame.sprite.collide_mask)
        if colisao_carteira:
            som_coleta1.play()
            carteira.colidiu = True
            pontos_carteira += 1

        colisao_cerveja = pygame.sprite.spritecollide(
            McLovin, grupo_cerveja, False, pygame.sprite.collide_mask)
        if colisao_cerveja:
            som_coleta3.play()
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
    iniciar_jogo()
except:
    print("O jogo não pôde ser iniciado.")
