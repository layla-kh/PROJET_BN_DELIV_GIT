import pygame


img_players = pygame.image.load('images/player.png')
img_players_rect = img_players.get_rect()

class Settings:
    def __init__(self):
        self.settings_player = False

    #affiche le menu de selection de personnages
    def start(self ,screen):
        self.settings_player = True
        screen.blit(img_players, img_players_rect)
        pygame.display.flip()




