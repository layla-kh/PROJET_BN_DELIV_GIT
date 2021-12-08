import pygame

img_settings_on = pygame.image.load("images/settings_on.png")
img_settings_off = pygame.image.load("images/settings_off.png")
img_set_rect_on = img_settings_on.get_rect()
img_set_rect_off = img_settings_off.get_rect()






class Settings_sound():
    def __init__(self):
        self.settings_s = False
        self.bool_sound = True

    # met à jour le menu des paramettres
    def on(self ,screen):
        self.settings_s = True
        screen.blit(img_settings_on, img_set_rect_on)
        pygame.display.flip()


    def off(self, screen):
        self.settings_s = False
        screen.blit(img_settings_off, img_set_rect_off)
        pygame.display.flip()

