import pygame

# class de la plateforme de départ en bleue
class Platform1(pygame.sprite.Sprite):
    # definition de la plateforme de départ, elle est bleue
    def __init__(self):
        super().__init__()
        # definie l'image dela plateforme bleue et modifie sa taille
        self.image = pygame.transform.scale(pygame.image.load('C19_escape/images/platform1.png'), (83, 24))
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 680
    # faire descendre la plateforme,
    # la fonction ressoit la position y du joueur et le groupe ou elle se trouve
    def descendre1(self, joueur_y, group_platform1):
        # si la plateform est trop basse, elle disparait
        if self.rect.y == 700:
            self.remove(group_platform1)
        # si le joueur est trop haut, la plateforme descend de 4 pixels
        elif joueur_y < 300:
            self.rect.y += 4
