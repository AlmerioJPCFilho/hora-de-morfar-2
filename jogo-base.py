#importando funções
import pygame
from pygame.locals import *
from sys import exit 
from random import randint

#inciando o pygame
pygame.init()

#largura e altura da tela
largura = 920
altura = 600
#tela do jogosd
tela = pygame.display.set_mode((largura, altura))
#mudança do nome da dela 
pygame.display.set_caption('Projeto de IP')

#um clock pra definir a quantidade de frames 
relogio = pygame.time.Clock()

#musica de fundo
pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('super_mario_medley.mp3')
pygame.mixer.music.play(-1)
#barulho de colisao
barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(1)

#largura e altura dos nossos retangulos
x_personagem = int(largura/ 2) 
y_personagem = int(altura / 2)

#aleatoriadade de spawn
x_azul = randint(40, largura - 40) 
y_azul = randint(50, altura - 50)

x_branco = randint(40, largura - 40) 
y_branco = randint(50, altura - 50)

x_amarelo = randint(40, largura - 40) 
y_amarelo = randint(50, altura - 50)

#variaveis para escrever na tela os pontos
fonte = pygame.font.SysFont('arial', 30, True, True)
pontos_azul = 0
pontos_branco = 0
pontos_amarelo = 0

#laço que roda o game
while True:
    relogio.tick(60) #quantidade de frames do jogo

    tela.fill((0,0,0)) #atualizando a dela

    mensagem_azul = f'Pontos Azul: {pontos_azul}'
    texto_azul = fonte.render(mensagem_azul, False, (255, 255, 255))

    mensagem_branco = f'Pontos Branco: {pontos_branco}'
    texto_branco = fonte.render(mensagem_branco, False, (255, 255, 255))
    
    mensagem_amarelo = f'Pontos Amarelo: {pontos_amarelo}'
    texto_amarelo = fonte.render(mensagem_amarelo, False, (255, 255, 255))

    #laço para verificar ações
    for event in pygame.event.get():
        #ação de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                
            elif event.key == pygame.K_ESCAPE:
                tela = pygame.display.set_mode((920, 600))
            

    #movimentação do retangulo
    if pygame.key.get_pressed()[K_a]:
        x_personagem -= 10
    if pygame.key.get_pressed()[K_d]:
        x_personagem += 10
    if pygame.key.get_pressed()[K_w]:
        y_personagem -= 10
    if pygame.key.get_pressed()[K_s]:
        y_personagem += 10

    #criar o retangulo
    ret_vermelho = pygame.draw.rect(tela, (255, 50, 0), (x_personagem, y_personagem, 40, 50))

    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 20, 25))
    ret_branco = pygame.draw.rect(tela, (255, 255, 255), (x_branco, y_branco, 20, 25))
    ret_amarelo = pygame.draw.rect(tela, (255, 255, 0), (x_amarelo, y_amarelo, 20, 25))

    #colisão e mover o retangulo que foi colidido para uma posição aleatoria
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, largura - 40)
        y_azul = randint(50, altura - 50)
        pontos_azul += 1
        barulho_colisao.play()
    
    if ret_vermelho.colliderect(ret_amarelo):
        x_amarelo = randint(40, largura - 40)
        y_amarelo = randint(50, altura - 50)
        pontos_amarelo += 1
        barulho_colisao.play()
    
    if ret_vermelho.colliderect(ret_branco):
        x_branco = randint(40, largura - 40)
        y_branco = randint(50, altura - 50)
        pontos_branco += 1
        barulho_colisao.play()

    tela.blit(texto_azul, (40, 40))
    tela.blit(texto_amarelo, (40, 90))
    tela.blit(texto_branco, (40, 130))


    pygame.display.update() #linha para atualizar o codigo e não deixar que ele trave
