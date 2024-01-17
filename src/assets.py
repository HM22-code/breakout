import os
import pygame

sprites = {}
audios = {}

def load_sprites():
    path = os.path.join(os.path.abspath(os.curdir), "assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file)).convert_alpha()
        
def get_sprite(name):
    return sprites[name]

def load_audios():
    path = os.path.join(os.path.abspath(os.curdir), "assets", "audios")
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))
        
def get_audio(name):
    return audios[name]