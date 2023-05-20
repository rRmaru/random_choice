import numpy as np
import sys, random
import pygame
import pygame.draw as draw
from pygame.locals import *


# ゲーム画面を初期化 --- (*1)
class Agent():
    def __init__(self, name):
        self.name = name
        self.pos = [300,300]
        self.stop = False
    
    def action(self):
        direction = range(4)
        prob = [0.20,0.27,0.20,0.33]
        act = np.random.choice(a=direction, p=prob)
        if act == 0:
            return [-5,-5]
        elif act == 1:
            return [5,-5]
        elif act == 2:
            return [-5,5]
        else:
            return [5,5]
        
    def update(self):
        act = self.action()
        self.pos[0] = self.pos[0] + act[0]
        self.pos[1] = self.pos[1] + act[1]
        
    def draw(self, scr, img):
        scr.blit(img, self.pos)
        
    def step(self, scr, img):
        if self.stop == False:
            self.update()
        self.draw(scr, img)
        
    def stop_fn(self):
        self.stop = True
        
    
    
def main():
    WIDTH, HEIGHT = 800, 800
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("第2回院飲み会場所決め")
    
    img = pygame.image.load("./images/char.png")
    img_rect = img.get_rect()
    img = pygame.transform.scale(img, (200,200))
    
    clock = pygame.time.Clock()
    
    white = (255,255,255)
    black = (0,0,0)
    font1 = pygame.font.SysFont('hg創英角ｺﾞｼｯｸub', 50)
    font2 = pygame.font.SysFont('hg創英角ｺﾞｼｯｸub', 100)
    text1 = font1.render("居酒屋１", True, black)
    text2 = font1.render("居酒屋２", True, black)
    text3 = font1.render("居酒屋３", True, black)
    text4 = font1.render("居酒屋４", True, black)
    count = 0
    #set agent
    selector = Agent("selector")
    
    # 繰り返し画面を描画 --- (*2)
    while True:
        # 背景と円を描画 --- (*3)
        clock.tick(15)  # 30fps
        
        screen.fill(white)
        draw.line(screen, black, (0,400), (800,400))
        draw.line(screen, black, (400,0), (400,800))
        screen.blit(text1, (80, 180))
        screen.blit(text2, (540, 180))
        screen.blit(text3, (150, 580))
        screen.blit(text4, (550, 580))
        selector.step(screen, img)
        draw.circle(screen, (255,0,0), (selector.pos[0]+100,selector.pos[1]+100),5)
        count += 1
        
        if count == 100:
            pos = selector.pos
            if pos[0]+100 <= 400:
                if pos[1]+100 <= 400:
                    text = "とりのすけ"
                else:
                    text = "魚民"
            else:
                if pos[1]+100 <= 400:
                    text = "トリキ"
                else:
                    text = "あうん"
            selector.stop_fn()
        
        if selector.stop:  
            result = font2.render(text+"に決定", True, (0,0,255))
            screen.blit(result, (120,350))
            
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT: sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()  
                
if __name__ == '__main__':
    main()
