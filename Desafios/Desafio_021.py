# Faça um programa de Python que abra e reproduza o áudio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('Desafio_021')
pygame.mixer.music.play
pygame.event.wait()