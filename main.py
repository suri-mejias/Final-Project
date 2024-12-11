import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 720))

game = Game('img/case1_img.png', 'img/case2_img.png', 'img/case3_img.png', 'img/case4_img.png', 'img/case5_img.png', 'img/case6_img.png', 'img/case7_img.png', 'img/case8_img.png', 'img/case9_img.png', 'img/case10_img.png')
game.resize_images()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()







if game.active:
    game.case1_img(screen)