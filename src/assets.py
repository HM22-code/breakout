import os
import pygame

sprites = {}
audios = {}

def load_sprites():
    """ Load all sprites from assets/images/
    """
    path = os.path.join(os.path.abspath(os.curdir), "assets", "images")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file)).convert_alpha()
        
def get_sprite(name):
    """ Get sprite from name

    Args:
        name (_type_): string

    Returns:
        _type_: image
    """
    return sprites[name]

def load_audios():
    """ Load all audios from assets/audios/
    """
    path = os.path.join(os.path.abspath(os.curdir), "assets", "audios")
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))
        
def get_audio(name):
    """ Get audio from name

    Args:
        name (_type_): string

    Returns:
        _type_: audio
    """
    return audios[name]