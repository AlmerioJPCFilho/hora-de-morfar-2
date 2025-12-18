import pygame
from pygame.locals import *

pygame.init()

class Personagem(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, largura_tela, altura_tela):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_personagem = []
        for i in range(4):
            img = sprite_sheet.subsurface((i * 600, 0), (600, 600))
            img = pygame.transform.scale(img, (600 // 4, 600 // 4))
            self.imagens_personagem.append(img)

        self.atual = 0
        self.image = self.imagens_personagem[self.atual]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = largura_tela // 2
        self.rect.y = altura_tela - 100
        self.rect.center = (self.rect.x, self.rect.y)
        self.velocidade = 7
        self.animar = False
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.flipar = False

    def animacao(self):
        self.animar = True

    def mover_esquerda(self):
        self.flipar = True
        if self.rect.x <= 0:
            self.rect.x = 0
        else:
            self.rect.x -= self.velocidade
            self.animacao()

    def mover_direita(self):
        self.flipar = False
        if self.rect.topright[0] >= self.largura_tela:
            self.rect.right = self.largura_tela
        else:
            self.rect.x += self.velocidade
            self.animacao()
    
    def mover_cima(self):
        if self.rect.y <= 0:
            self.rect.y = 0
        else:
            self.rect.y -= self.velocidade
            self.animacao()
    
    def mover_baixo(self):
        if self.rect.bottom >= self.altura_tela:
            self.rect.bottom = self.altura_tela
        else:
            self.rect.y += self.velocidade
            self.animacao()
    
    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.1
            if self.atual >= len(self.imagens_personagem):
                self.atual = 0
                self.animar = False
            self.image = self.imagens_personagem[int(self.atual)]
            if self.flipar == True:
                self.image = pygame.transform.flip(self.image, True, False)
