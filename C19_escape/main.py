import pygame
from game import Game
from settings import Settings
from settings_sound import Settings_sound

pygame.init()

# génerer la fenetre
pygame.display.set_caption("C-19 Escape !!!")
screen = pygame.display.set_mode((680, 750))
# poser un icone
icon = pygame.image.load('images/LuisD.png')
pygame.display.set_icon(icon)

# importer le bg
bg = pygame.image.load('images/fond.png')
settings = Settings()
settings_sound = Settings_sound()


img_creature = pygame.image.load("images/creature.png")
img_settings_on = pygame.image.load("images/settings_on.png")
img_settings_off = pygame.image.load("images/settings_off.png")
img_settings_player = pygame.image.load("images/player.png")
img_set_player_rect = img_settings_player.get_rect()
img_game_over_enter_name = pygame.image.load("images/gameover1.png")
img_game_over = pygame.image.load("images/gameover2.png")
sound = pygame.mixer.Sound("soundbackground.wav")


settings_player = False
menu = True
setting_sound_menu = False
bool_sound_main = False



# importer la l'mage de menu
img_menu = pygame.image.load('images/principale.png')
# modifier les dimensions du menu
img_menu = pygame.transform.scale(img_menu, (680, 750))
img_menu_rect = img_menu.get_rect()
# importer le bouton pour pour lancer la partie




perso = "images/Luis"
# charger le jeu
game = Game(perso)
# definition de la méthode de clock
clock = pygame.time.Clock()
cpt_boucle = 0
run = True
a = True

while run:
    if bool_sound_main :
        sound.play()

    elif not bool_sound_main :
        sound.stop()


    # appliquer une image sur le screen (fond d'écran)
    screen.blit(bg, (0, 0))

    if not game.is_playing and not settings_player and not setting_sound_menu:
        cpt_boucle = 0
        # ajouter mon écran de bien venu
        screen.blit(img_menu, img_menu_rect)

    # verifier si le jeu a commencé ou non et enregistrer le nom et le score
    if game.is_playing:
        # declancher les instrucions de la partie
        game.update(screen, cpt_boucle)
        # compter le nombre de boucle
        #screen.blit(img_creature, (0,0))
        cpt_boucle += 1

    # verifier si notre jeu n'a pas commencé
    if settings_player:
        cpt_boucle = 0
        settings.start(screen)
    # verifie si on affiche le menu son lorsqu'il est activé
    elif setting_sound_menu and bool_sound_main:
        settings_sound.on(screen)
    # verifie si on affiche le menu son lorsqu'il est désactivé
    elif setting_sound_menu and not bool_sound_main:
        settings_sound.off(screen)

    # si le joueur est mort, il inscrira son nom grace a cette fonction qui est appelé ici
    if game.image_GO:
        screen.blit(img_game_over_enter_name, (0, 0))
        game.name(screen, cpt_boucle)
    # apres avoir entré son nom, affichage du menu de fin
    if game.image_GO_2:
        screen.blit(img_game_over, (0, 0))
        game.end_score()


    # verifier si le joueur souhaiter aller a gauche ou a droite et le déplacer
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right(screen.get_width(), perso)
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left(screen.get_width(), perso)

    # mettre a jour l'écran
    pygame.display.flip()

    # parcourir l'ensemble des actions du joueur
    for event in pygame.event.get():
        # si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        # detecter touche clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # retourner des settings au menu principale grace la touhe échape
            if event.key == pygame.K_ESCAPE and (settings_player or setting_sound_menu) :
                menu = True
                setting_sound_menu = False
                settings_player = False

        # comprendre si une touche est levée
        elif event.type == pygame.KEYUP and game.is_playing:
            game.pressed[event.key] = False


        # détection des cliques de la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 190 and pygame.mouse.get_pos()[1] >= 300 and game.menu and not settings_player:
                if pygame.mouse.get_pos()[0] <= 500 and pygame.mouse.get_pos()[1] <= 420:
                    # mettre le jeu en mode lancé s'il clique sur le rect boutton
                    # initialise le nom du joueur dans le file Scores.txt
                    menu = False
                    game.start()

            if pygame.mouse.get_pos()[0] >= 210 and pygame.mouse.get_pos()[1] >= 495 and not settings_player and game.menu:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 565:
                    # fermer le menu et entrer dans la selection des personnages
                    menu = False
                    settings_player = True

            # selectionner le personnage luis
            if pygame.mouse.get_pos()[0] in range(144, 300) and pygame.mouse.get_pos()[1] in range(325, 473) and settings_player:
                perso = "images/Luis"
                game = Game(perso)
                game.start()
                settings_player = False
            # selectionner le personnage christian
            if pygame.mouse.get_pos()[0] in range(365, 506) and pygame.mouse.get_pos()[1] in range(325, 473) and settings_player and game.menu:
                perso = "images/Christian"
                game = Game(perso)
                game.start()
                settings_player = False


            if pygame.mouse.get_pos()[0] >= 395 and pygame.mouse.get_pos()[1] >= 495 and game.menu and not settings_player and not setting_sound_menu:
                if pygame.mouse.get_pos()[0] <= 470 and pygame.mouse.get_pos()[1] <= 565:
                    # rentrer dans le menu son
                    setting_sound_menu = True
                    menu = False

            if pygame.mouse.get_pos()[0] in range(136, 380) and pygame.mouse.get_pos()[1] in range(150, 260) and setting_sound_menu and bool_sound_main:
                # désactiver le son
                bool_sound_main = False


            elif pygame.mouse.get_pos()[0] in range(136, 380) and pygame.mouse.get_pos()[1] in range(150, 260) and setting_sound_menu and not bool_sound_main:
                # activer le son
                bool_sound_main = True


    # utiliser le clock avec 100 images / seconde
    clock.tick(100)
