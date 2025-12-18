import pygame
from pygame.locals import *
from random import randint, randrange, choice

pygame.init()

class Policial(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, largura_tela, altura_tela):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_personagem = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 600, 0), (600, 600))
            img = pygame.transform.scale(img, (600 // 4, 600 // 4))
            self.imagens_personagem.append(img)

        self.largura_tela = largura_tela
        self.altura_tela = altura_tela

        self.atual = 0
        self.image = self.imagens_personagem[self.atual]

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.escolha = choice([0, 1, 2, 3])
        if self.escolha == 0:
            self.rect.x = randrange(-300, 0, 50)
            self.rect.y = randrange(0, self.altura_tela - 60, 30)
        
        elif self.escolha == 1:
            self.rect.x = randrange(0, self.largura_tela - 50, 50)
            self.rect.y = randrange(- 150, - 50, 30)
        
        elif self.escolha == 2:
            self.rect.x = randrange(self.largura_tela + 50, self.largura_tela + 200, 50)
            self.rect.y = randrange(0, self.altura_tela - 60, 30)
        
        elif self.escolha == 3:
            self.rect.x = randrange(0, self.largura_tela - 50, 50)
            self.rect.y = randrange(self.altura_tela + 50, self.altura_tela + 150, 30)

        self.rect.center = (self.rect.x, self.rect.y)

        self.velocidade = 4
        self.colidiu = False
        self.pontos = 0
    
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.imagens_personagem):
            self.atual = 0
        self.image = self.imagens_personagem[int(self.atual)]

        if self.escolha == 0: #esquerda
            if self.colidiu == True or (self.rect.right >= self.largura_tela or self.rect.bottom >= self.altura_tela):
                self.rect.x = randint(-300, 0)
                self.rect.y = randint(0, self.altura_tela - 60)
                self.escolha = choice([0, 1, 2, 3])
                self.colidiu = False
            else:
                self.rect.x += self.velocidade
        
        elif self.escolha == 1: #cima
            if self.colidiu == True or (self.rect.right >= self.largura_tela or self.rect.bottom >= self.altura_tela):
                self.rect.x = randint(0, self.largura_tela - 50)
                self.rect.y = randint(-150, -50)
                self.escolha = choice([0, 1, 2, 3])
                self.colidiu = False
            else:
                self.rect.y += self.velocidade

        elif self.escolha == 2: #direita
            if self.colidiu == True or (self.rect.left <= 0 or self.rect.bottom >= self.altura_tela):
                self.rect.x = randint(self.largura_tela + 50, self.largura_tela + 150)
                self.rect.y = randint(0, self.altura_tela - 60)
                self.escolha = choice([0, 1, 2, 3])
                self.colidiu = False
            else:
                self.rect.x -= self.velocidade
            
        elif self.escolha == 3: #baixo
            if self.colidiu == True or (self.rect.left <= 0 or self.rect.bottom >= self.altura_tela):
                self.rect.x = randint(0, self.largura_tela - 50)
                self.rect.y = randint(self.altura_tela + 50, self.altura_tela + 150)
                self.escolha = choice([0, 1, 2, 3])
                self.colidiu = False
            else:
                self.rect.y -= self.velocidade

