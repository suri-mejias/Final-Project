import pygame
import random


class Game:

    def __init__(self, case1_img, case2_img, case3_img, case4_img, case5_img, case6_img, case7_img, case8_img, case9_img, case10_img, background):
        self.case1_img = pygame.image.load(case1_img).convert_alpha
        self.case2_img = pygame.image.load(case1_img).convert_alpha
        self.case3_img = pygame.image.load(case1_img).convert_alpha
        self.case4_img = pygame.image.load(case1_img).convert_alpha
        self.case5_img = pygame.image.load(case1_img).convert_alpha
        self.case6_img = pygame.image.load(case1_img).convert_alpha
        self.case7_img = pygame.image.load(case1_img).convert_alpha
        self.case8_img = pygame.image.load(case1_img).convert_alpha
        self.case9_img = pygame.image.load(case1_img).convert_alpha
        self.case10_img = pygame.image.load(case1_img).convert_alpha
        self.background = (0, 0, 0)


    def resize_images(self):
        self.case_1 = pygame.transform.scale(self.case_1, (51,34))
        self.case_2 = pygame.transform.scale(self.case_2, (51,34))
        self.case_3 = pygame.transform.scale(self.case_3, (51,34))
        self.case_4 = pygame.transform.scale(self.case_4, (51,34))
        self.case_5 = pygame.transform.scale(self.case_5, (51,34))
        self.case_6 = pygame.transform.scale(self.case_6, (51,34))
        self.case_7 = pygame.transform.scale(self.case_7, (51,34))
        self.case_8 = pygame.transform.scale(self.case_8, (51,34))
        self.case_9 = pygame.transform.scale(self.case_9, (51,34))
        self.case_10 = pygame.transform.scale(self.case_10, (51,34))
        
    def show_background(self, screen):
        screen.blit(self.background,(0,0))