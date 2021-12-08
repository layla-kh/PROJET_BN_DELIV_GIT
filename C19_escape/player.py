import pygame

# creer la class du joueur
class Player(pygame.sprite.Sprite):
    # definition du joueur
    def __init__(self, game, perso):
        super().__init__()
        # peut faire passer dans la class game
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load(perso + "D.png"),(38,75))
        self.rect = self.image.get_rect()
        self.rect.x = 340
        self.rect.y = 600
        # variables de saut
        self.somx = -2
        self.fonctx = 0
        # caractéristiques du joueur
        self.velocitx = 5
    # deplacement à droite
    def move_right(self, x, perso):
        # le joueur regarde a droite quand il se deplace à droite
        self.image = pygame.transform.scale(pygame.image.load(perso + "D.png"), (45, 75))
        self.rect.x += self.velocitx
        # si il sort entierement du coté droit de la fenetre, il reapparait de l'autre coté
        if self.rect.x > x + self.rect.width - 10:
            self.rect.x = -self.rect.width
    # deplacement à gauche
    def move_left(self, x, perso):
        # le joueur regarde a gauche quand il se deplace à gauche
        self.image = pygame.transform.scale(pygame.image.load(perso + "G.png"), (39, 75))
        self.rect.x -= self.velocitx
        # si il sort entierement du coté gauche de la fenetre, il reapparait de l'autre coté
        if self.rect.x < -self.rect.width + 10:
            self.rect.x = x
    # gestion du saut, des collisions et de la mort du joueur
    def jump(self, var):
        # self.fonctx est l'image de somx
        self.rect.y += self.fonctx
        # fonction polynomiales du second degré qui decrit le saut du joueur
        self.fonctx = (self.somx * self.somx) - 4
        # dans le graph imaginaire, on fait avancer l'ordonne imaginaire
        self.somx += 0.1
        # si le joueur touche la platforme bleue, il se remet alors a sauter
        # et on reinitialise l'ordoné imaginaire
        if self.game.check_collision(self, self.game.all_platform1):
            self.somx = -1.5
        # si le joueur touche une platforme verte, il se remet alors a sauter
        # et on reinitialise l'ordoné imaginaire
        if self.game.check_collision(self, self.game.all_platform):
            self.somx = -1.5
        # si le joueur tombe trop bas,
        if self.rect.y > 700:
            self.game.game_over()
