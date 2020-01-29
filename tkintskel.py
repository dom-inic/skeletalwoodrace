from tkinter import *
import pygame
pygame.init()

root=Tk()
root.minsize(400,400)

root.mainloop(for event in pygame.event.get():if event.type == pygame.KEYDOWN:if event.key == pygame.K_ESCAPE:sys.exit())