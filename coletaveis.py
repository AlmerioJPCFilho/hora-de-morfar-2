import pygame
from pygame.locals import *
import os
from random import randint

class Coletaveis(pygame.sprite.Sprite):
    def __init__(self, largura_tela, altura_tela, imagem, personagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.largura_imagem = self.image.get_width()
        self.altura_imagem = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.largura_imagem // 8, self.altura_imagem // 8))
        self.mask = pygame.mask.from_surface(self.image)
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.rect = self.image.get_rect()
        self.rect.x = randint(40, self.largura_tela - 40)
        self.rect.y = randint(50, self.altura_tela - 50)
        if self.rect.right >= self.largura_tela or self.rect.left <= 0 or self.rect.bottom >= self.altura_tela:
            self.rect.x = randint(40, self.largura_tela - 40)
            self.rect.y = randint(50, self.altura_tela - 50)
        self.personagem = personagem
        self.colidiu = False

    def update(self):
        if self.colidiu == True:
            self.rect.x = randint(40, self.largura_tela - 40)
            self.rect.y = randint(50, self.altura_tela - 50)
            if self.rect.right >= self.largura_tela or self.rect.left <= 0 or self.rect.bottom >= self.altura_tela:
                self.rect.x = randint(40, self.largura_tela - 40)
                self.rect.y = randint(50, self.altura_tela - 50)
            self.colidiu = False


    
