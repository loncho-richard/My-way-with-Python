import pygame
import numpy as np

pygame.init()
#Alto y ancho de la pantalla
width, height = 750, 750
#Creacion de la pantalla
screen = pygame.display.set_mode((height, width))
#Color de fondo, casi negro, casi oscuro
bg = 25, 25, 25
#Pintamos el fondo con el color elegido
screen.fill(bg)

nxC, nyC = 25, 25

dimCW = width  / nxC
dimCH = height / nyC

#Bucle de ejecucion
while True:
    
    for y in range(0, nxC):
        for x in range(0, nyC):

            poly = [((x)   * dimCW,  y * dimCH),
                    ((x+1) * dimCW,  y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH ),
                    ((X)   * dimCW, (y+1) * dimCH)]

            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
    pygame.display.flip()