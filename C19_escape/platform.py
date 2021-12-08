import pygame
import random

# class des plateformes verte
class Platform(pygame.sprite.Sprite):
    # definition d'une plateforme verte
    def __init__(self, y):
        super().__init__()
        # definie l'image dela plateforme verte et modifie sa taille
        self.image = pygame.transform.scale(pygame.image.load("images/platform.png"),
                                            (83, 24))
        self.rect = self.image.get_rect()
        # definie les coordnées de la plateforme verte
        self.rect.x = random.randint(0, 600)
        self.rect.y = random.randint(y - 20, y)
    # faire descendre la plateforme,
    # la fonction ressoit la position y du joueur et le groupe ou elle se trouve
    def descendre(self, joueur_y, group_platform):
        # si la plateform est trop basse, elle disparait
        if self.rect.y == 700:
            # print("g disparue")
            self.remove(group_platform)
        # si le joueur est trop haut, la plateforme descend de 1 pixel
        elif joueur_y < 300:
            self.rect.y += 1
    # la plateforme descend automatiquement de y pixel(s)
    def tombe(self, y):
        self.rect.y += y