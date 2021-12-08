import pygame
from player import Player
from platform1 import Platform1
from platform import Platform
import random


# class du jeu

img_game_over_enter_name = pygame.image.load("C19_escape/images/gameover1.png")

class Game():
    def __init__(self, perso):
        # definir si le jeu a commencé ou non
        self.is_playing = False
        # definir si le les settings ont commencé ou non
        self.settings_player = False
        # definir si le menu a commencé ou non
        self.menu = True
        # definir que le joueur n'a pas perdu
        self.end = False
        # definir que la page pour entrer le nom n'apparait pas
        self.image_GO = False
        # definir que la page de fin n'apparait pas
        self.image_GO_2 = False

        # stocker les evenement du joueur
        self.pressed = {}
        # generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self, perso)
        # generer le groupe qui contient la plateforme bleue
        self.all_platform1 = pygame.sprite.Group()
        # generer le groupe qui contient les plateformes vertes
        self.all_platform = pygame.sprite.Group()

    # apparition de la platform de depart bleue
    def spawn_platform1(self):
        platform1 = Platform1()
        self.all_platform1.add(platform1)

    # apparition des premières plateformes vertes
    def spawn_platform(self):
        # apparition d'une platform verte
        # les plateforms seront généré a chaque fois avec des coordonées en y
        # qui seront séparé d'une distance de 0 à 40 pixels
        cpt = 700
        while cpt > 30:
            y = random.randint(cpt - 40, cpt)
            if cpt % 2 == 0:
                platform = Platform(y)
                self.all_platform.add(platform)
            cpt = y

    # répond lors d'une collision
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # démarre les étapes de génération du jeu
    def start(self):
        # démare le jeu
        self.menu = False
        self.is_playing = True
        # fait apparaitre la plateforme de départ bleue
        self.spawn_platform1()
        # fait apparaitre les plateformes vertes de départ
        self.spawn_platform()
        # fait apparaitre le joueur et (re)initialise ses coordonées pour ne pas qu'il reste en bas
        self.all_players.add(self.player)
        self.player.rect.y = 600
        self.player.rect.x = 340


    def name(self, screen, score):
        # permetre au joueur d'entrer son nom
        pygame.init()
        name = ""
        font = pygame.font.Font(None, 50)
        fin_nom = True
        cpt = ""
        while fin_nom and len(name)<13:
            for evt in pygame.event.get():
                if evt.type == pygame.KEYDOWN:
                    if evt.unicode.isalpha():
                        name += evt.unicode
                    elif evt.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == pygame.K_RETURN or evt.key == pygame.K_KP_ENTER:
                        fin_nom = False
                elif evt.type == pygame.QUIT:
                    pygame.quit()
            block = font.render(name, True, (255, 255, 255))
            screen.blit(block, (180, 350))
            pygame.display.flip()
            screen.blit(img_game_over_enter_name, (0, 0))
        # sauvegarde du nom et du score
        file = open("Scores.txt", "a")
        file.write(name + " : \n" + str(score) + "\n")
        file.close()
        self.settings_player = False
        # fin de cette fonction et de l'affichage
        self.image_GO = False
        # début de la fonction end_score
        self.image_GO_2 = True


    def end_score(self):
    # tentative non abouti de faire apparaitre le nom et score du joueur et du meilleur joueur
        for event in pygame.event.get():
            # faire revenir dans la page de menu  si le joueur apuis au bon endroit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(210, 450) and pygame.mouse.get_pos()[1] in range(425, 563) :
                    self.image_GO_2 = False
                    self.menu = True


    def game_over(self):
        # remettre je jeux a neuf (retirer les platefomres, le joeur et pose le jeu en attente)
        # on écrase le groupes par un groupe par default qui est vide du coup
        self.all_platform1 = pygame.sprite.Group()
        self.all_platform = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.image_GO = True
        self.end = True
        # stope le jeu
        self.menu = True
        self.settings_player = False
        self.is_playing = False


    # ensembles des tâches lorsque le jeu est en route
    def update(self, screen, var):
        # appliquer l'image du joueur

        screen.blit(self.player.image, self.player.rect)
        # appliquer les img de la platform 1 en bleue
        self.all_platform1.draw(screen)
        # appliquer les img des platforms vertes
        self.all_platform.draw(screen)
        # si le joueur est trop haut, les platforms vertes descendront
        score = 0
        for la_platform in self.all_platform:
            la_platform.descendre(self.player.rect.y, self.all_platform)
        # creation des nouvelles plateformes verte toute les 29 boucles
        # elles appraitront au dessus de la fenêtre entre y [-24 ; -44]
        if var % 29 == 0:
            une_platform = Platform(-24)
            self.all_platform.add(une_platform)
            # creation des nouvelles plateformes verte toute les si var est pair
            if var % 2 == 0:
                une_platform = Platform(-24)
                self.all_platform.add(une_platform)
        # dès que on atteint les 600 boucles jusqu'à 1000 (6 secondes à 10 secondes),
        # les plateformes descendent automatiquement de 1 pixel
        if 600 < var < 1000:
            for la_platform in self.all_platform:
                la_platform.tombe(1)
        # dès que on atteint les 1001 boucles (10 secondes),
        # les plateformes descendent automatiquement de 2 pixel
        if var > 1001:
            for la_platform in self.all_platform:
                la_platform.tombe(2)
        # dès que on atteint les 6000 boucles (60 secondes),
        # les plateformes descendent automatiquement de 1 pixel supplémentaire qd var est pair
        if var > 6000 and var % 2 == 0:
            for la_platform in self.all_platform:
                la_platform.tombe(1)
        # dès que on atteint les 12000 boucles (120 secondes),
        # les plateformes descendent automatiquement de 1 pixel supplémentaire qd var est impair
        if var > 12000 and var+1 % 2 == 0:
            for la_platform in self.all_platform:
                la_platform.tombe(1)
        # si le joueur est trop haut, la platform 1 de base bleue descendra
        for platform1 in self.all_platform1:
            platform1.descendre1(self.player.rect.y, self.all_platform1)
        # faire sauter le joueur en modifiant ses coordonées y
        self.player.jump(var)

