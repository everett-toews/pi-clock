import fnmatch
import logging
import os
import random

import pygame

logger = logging.getLogger(__name__)


def play_songs(num=3):
    songs = []
    for root, dirnames, filenames in os.walk('audio'):
        for filename in fnmatch.filter(filenames, '*.mp3'):
            songs.append(os.path.join(root, filename))

    if not songs:
        logger.warn("No songs in %s", os.path.abspath('audio'))
        return

    clock = pygame.time.Clock()
    pygame.mixer.init()

    for _ in xrange(num):
        song = random.choice(songs)
        songs.remove(song)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
