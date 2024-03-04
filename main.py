import pygame
from pygame.locals import *

class snake:
    def __init__(self):
        self.block = pygame.image.load("Resource/block.jpg").convert()
        self.block_x=100
        self.block_y=100
    
    
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500))
        self.surface.fill((255,255,255))
        
    
    def run(self):
        pass

def draw_block():
    surface.fill((255,255,255))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

if __name__ == "__main__":
    game= Game()
    game.run
    
    
    
    
    surface.blit(block,(block_x,block_y))
    
    pygame.display.flip()
    
    running= True 
    
    while running:
        for event in pygame.event.get():
            
            if event.type  == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                                        
            elif event.type == QUIT:
                running = False
    
    