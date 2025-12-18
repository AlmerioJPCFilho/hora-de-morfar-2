import pygame
from pygame.locals import *
from sys import exit
from personagem import Personagem
from coletaveis import Coletaveis
from policial import Policial
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
background = pygame.image.load(os.path.join(diretorio_imagens, 'imagem-fundo.png')).convert()
background = pygame.transform.scale(background, (largura_tela, altura_tela))

# SONS
musica_titulo = pygame.mixer.Sound(os.path.join(diretorio_audios, 'jonny-fabisak-title-cube.mp3'))
musica_titulo.set_volume(0.5)
musica_titulo_rodando = False
musica_jogo = pygame.mixer.Sound(os.path.join(diretorio_audios, 'jonny-fabisak-blocky-blues.mp3'))
musica_jogo.set_volume(0.5)
musica_jogo_rodando = False
som_coleta1 = pygame.mixer.Sound(os.path.join(diretorio_audios, 'cube-sfx-1.mp3'))
som_coleta2 = pygame.mixer.Sound(os.path.join(diretorio_audios, 'cube-sfx-2.mp3'))
som_coleta3 = pygame.mixer.Sound(os.path.join(diretorio_audios, 'cube-sfx-3.mp3'))
som_dano = pygame.mixer.Sound(os.path.join(diretorio_audios, 'som-dano.wav.'))
som_morte = pygame.mixer.Sound(os.path.join(diretorio_audios, 'som-morte.mp3'))
som_morte.set_volume(0.5)

# PERSONAGEM
sprite_personagem = pygame.image.load(os.path.join(diretorio_imagens, 'sprite-mclovin.png')).convert_alpha()
McLovin = Personagem(sprite_personagem, largura_tela, altura_tela)
todas_sprites.add(McLovin)

# COLETAVEIS
# Carteira
sprite_carteira = pygame.image.load(os.path.join(diretorio_imagens, 'identidade.png')).convert()
carteira = Coletaveis(largura_tela, altura_tela,sprite_carteira, McLovin)
todas_sprites.add(carteira)
grupo_carteira = pygame.sprite.Group()
grupo_carteira.add(carteira)

# Cerveja
sprite_cerveja = pygame.image.load(os.path.join(diretorio_imagens, 'cerveja.png')).convert_alpha()
cerveja = Coletaveis(largura_tela, altura_tela,sprite_cerveja, McLovin)
todas_sprites.add(cerveja)
grupo_cerveja = pygame.sprite.Group()
grupo_cerveja.add(cerveja)

# Detergente
sprite_detergente = pygame.image.load(os.path.join(diretorio_imagens, 'detergente.png')).convert_alpha()
detergente = Coletaveis(largura_tela, altura_tela, sprite_detergente, McLovin)
todas_sprites.add(detergente)
grupo_detergente = pygame.sprite.Group()
grupo_detergente.add(detergente)

#Policial
sprite_policial = pygame.image.load(os.path.join(diretorio_imagens, 'policial.png')).convert_alpha()

grupo_policial_1 = pygame.sprite.Group()
policial_1 = Policial(sprite_policial, largura_tela, altura_tela)
todas_sprites.add(policial_1)
grupo_policial_1.add(policial_1)

grupo_policial_2 = pygame.sprite.Group()
policial_2 = Policial(sprite_policial, largura_tela, altura_tela)
todas_sprites.add(policial_2)
grupo_policial_2.add(policial_2)

grupo_policial_3 = pygame.sprite.Group()
policial_3 = Policial(sprite_policial, largura_tela, altura_tela)
todas_sprites.add(policial_3)
grupo_policial_3.add(policial_3)

grupo_policial_4 = pygame.sprite.Group()
policial_4 = Policial(sprite_policial, largura_tela, altura_tela)
todas_sprites.add(policial_4)
grupo_policial_4.add(policial_4)

# PONTUAÇÃO
pontos_carteira = 0
img_carteira_pt = pygame.transform.scale(sprite_carteira, (sprite_carteira.get_width() // 12, sprite_carteira.get_height() // 12))

pontos_cerveja = 0
img_cerveja_pt = pygame.transform.scale(sprite_cerveja, (sprite_cerveja.get_width() // 12, sprite_cerveja.get_height() // 12))

pontos_detergente = 0
img_detergente_pt = pygame.transform.scale(sprite_detergente, (sprite_detergente.get_width() // 12, sprite_detergente.get_height() // 12))

pontos_policial = 0
sprite_policial_pt = pygame.image.load(os.path.join(diretorio_imagens, 'policial-pt.png')).convert_alpha()
img_policial_pt = pygame.transform.scale(sprite_policial_pt, (sprite_policial_pt.get_width() // 12, sprite_policial_pt.get_height() // 12))

jogador_morreu = False
tela_morte = pygame.image.load(os.path.join(diretorio_imagens, 'tela-derrota.png')).convert()
transformar_tela_morte = pygame.transform.scale(tela_morte, (1280, 720))

jogador_venceu = False
#tela_vitoria = pygame.image.load(os.path.join(diretorio_imagens, 'tela-vitoria.png')).convert()
#transformar_tela_vitoria = pygame.transform.scale(tela_vitoria, (1280, 720))

# TEXTOS
msg_reiniciar = 'Pressione (ESPAÇO) para reiniciar'
txt_reiniciar = fonte.render(msg_reiniciar, False, (130, 0, 0))
msg_sair = 'Pressione (ESC) para sair'
txt_sair = fonte.render(msg_sair, False, (130, 0, 0))

telainicial = pygame.image.load(os.path.join(diretorio_imagens, 'tela-inicial.png')).convert()
transformarTelaInicial = pygame.transform.scale(telainicial, (1280, 720))

# TEMPORIZADOR
tempo_restante = 1100
fonte = pygame.font.SysFont(None, 50)

#FUNÇÃO TEMPO
def timer(tempo_restante):
    lista = str(tempo_restante)
    if len(lista) >= 4:
        return lista[0] + lista[1]
    elif len(lista) == 3:
        return lista[0]
    elif len(lista)  == 2:
        return "0." + lista[0]
    else:
        return 0


def iniciar_jogo():
    global musica_titulo_rodando
    retanguloTransparente = pygame.Surface((320, 60))
    retanguloTransparente.set_alpha(100)
    retanguloTransparente.fill((255, 255, 255)) 
    rect_jogar = pygame.Rect(480, 420, 320, 60)
    rect_sair = pygame.Rect(480, 510, 320, 60)
    while True:
        if not musica_titulo_rodando:
            musica_titulo.play(-1)
            musica_titulo_rodando = True
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
    global pontos_carteira, pontos_cerveja, pontos_detergente, pontos_policial, jogador_morreu, jogador_venceu, tempo_restante, self
    pontos_carteira = 0
    pontos_cerveja = 0
    pontos_detergente = 0
    pontos_policial = 0
    tempo_restante = 1100
    jogador_morreu = False
    jogador_venceu = False
    McLovin.rect.center = (200, altura_tela - 100)

def vitoria(tela, transformar_tela_vitoria):
    global jogador_venceu, musica_jogo_rodando
    musica_jogo.stop()
    musica_jogo_rodando = False
    esperando_reiniciar = True
    while esperando_reiniciar:
        relogio.tick(30)
        tela.blit(transformar_tela_vitoria, (0, 0))
        tela.blit(txt_reiniciar, ((10,5)))
        tela.blit(txt_sair, ((10,45)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    jogador_venceu = False
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    esperando_reiniciar = False
                    try:
                        #som_vitoria.stop()
                        recomecar_jogo()
                    except:
                        print("O jogo não pôde ser reiniciado.")

def gameOver(tela, transformar_tela_morte):
    global jogador_morreu, musica_jogo_rodando
    musica_jogo.stop()
    musica_jogo_rodando = False
    som_morte.play()
    esperando_reiniciar = True
    while esperando_reiniciar:
        relogio.tick(30)
        tela.blit(transformar_tela_morte, (0, 0))
        tela.blit(txt_reiniciar, ((10,5)))
        tela.blit(txt_sair, ((10,45)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    jogador_morreu = False
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    esperando_reiniciar = False
                    try:
                        som_morte.stop()
                        recomecar_jogo()
                    except:
                        print("O jogo não pôde ser reiniciado.")
tempo_anterior = 0
def jogo():
    global pontos_carteira, pontos_cerveja, pontos_detergente, pontos_policial, jogador_morreu, jogador_venceu, som_coleta1, som_coleta2, som_coleta3, musica_jogo_rodando, musica_titulo, musica_titulo_rodando, tempo_restante, tempo_anterior
    while True:
        if jogador_morreu:
            gameOver(tela, transformar_tela_morte)
        #if jogador_venceu:
            #vitoria(tela, transformar_tela_vitoria)
        if not musica_jogo_rodando:
            if musica_titulo_rodando:
                musica_titulo.stop()
                musica_titulo_rodando = False
            musica_jogo.play(-1)
            musica_jogo_rodando = True
        relogio.tick(60)
        tela.fill(preto)
        tela.blit(background, (0, 0))
        todas_sprites.draw(tela)
        tempo_restante -= 1.5
        tempo_print = timer(int(tempo_restante))
        mensagem = fonte.render(f"Tempo Restante: {tempo_print}", False, (255, 255, 255))
        tela.blit(mensagem, (500, 20))

        msg_carteira = f': {pontos_carteira}'
        txt_carteira = fonte.render(msg_carteira, False, (255, 255, 255))

        msg_cerveja = f': {pontos_cerveja}'
        txt_cerveja = fonte.render(msg_cerveja, False, (255, 255, 255))

        msg_detergente = f': {pontos_detergente}'
        txt_detergente = fonte.render(msg_detergente, False, (255, 255, 255))

        msg_policial = f': {pontos_policial}'
        txt_policial = fonte.render(msg_policial, False, (255, 255, 255))

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
        colisao_carteira = pygame.sprite.spritecollide(McLovin, grupo_carteira, False, pygame.sprite.collide_mask)
        if colisao_carteira:
            som_coleta3.play()
            carteira.colidiu = True
            pontos_carteira += 1
            tempo_restante += 100
            msg_tempo = fonte.render("+1 segundos!", False, (255, 255, 0))
            tela.blit(msg_tempo, (500, 70))

        colisao_cerveja = pygame.sprite.spritecollide(McLovin, grupo_cerveja, False, pygame.sprite.collide_mask)
        if colisao_cerveja:
            som_coleta1.play()
            cerveja.colidiu = True
            pontos_cerveja += 1

        colisao_detergente = pygame.sprite.spritecollide(McLovin, grupo_detergente, False, pygame.sprite.collide_mask)
        if colisao_detergente:
            som_coleta2.play()
            detergente.colidiu = True
            pontos_detergente += 1
            tempo_restante += 50
            msg_tempo = fonte.render("+0.5 segundos!", False, (255, 255, 0))
            tela.blit(msg_tempo, (500, 70))

        colisao_policial_1 = pygame.sprite.spritecollide(McLovin, grupo_policial_1, False, pygame.sprite.collide_mask)
        if colisao_policial_1:
            som_dano.play()
            policial_1.colidiu = True
            pontos_policial += 1
            tempo_restante -= 100
            
        colisao_policial_2 = pygame.sprite.spritecollide(McLovin, grupo_policial_2, False, pygame.sprite.collide_mask)
        if colisao_policial_2:
            som_dano.play()
            policial_2.colidiu = True
            pontos_policial += 1
            tempo_restante -= 100

        colisao_policial_3 = pygame.sprite.spritecollide(McLovin, grupo_policial_3, False, pygame.sprite.collide_mask)
        if colisao_policial_3:
            som_dano.play()
            policial_3.colidiu = True
            pontos_policial += 1
            tempo_restante -= 100

        colisao_policial_4 = pygame.sprite.spritecollide(McLovin, grupo_policial_4, False, pygame.sprite.collide_mask)
        if colisao_policial_4:
            som_dano.play()
            policial_4.colidiu = True
            pontos_policial += 1
            tempo_restante -= 100


        tela.blit(img_carteira_pt, (20, 20))
        tela.blit(txt_carteira, (75, 18))

        tela.blit(img_cerveja_pt, (20, 70))
        tela.blit(txt_cerveja, (75, 72))

        tela.blit(img_detergente_pt, (20, 140))
        tela.blit(txt_detergente, (75, 145))

        tela.blit(img_policial_pt, (largura_tela - 100 , 20))
        tela.blit(txt_policial, (largura_tela - 45, 20))

        todas_sprites.update()
        if pontos_cerveja >= 25:
            jogador_venceu = True
        if tempo_restante <= 0:
            jogador_morreu = True
        pygame.display.flip()

try:
    iniciar_jogo()
except:
    print("O jogo não pôde ser iniciado.")
