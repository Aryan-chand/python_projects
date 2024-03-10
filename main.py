import pygame
from pygame.locals import *
import time
import random

Size = 40
bgcolor = (104 , 166 ,67)

class Apple :
    
    def __init__(self ,parent_screen) -> None:
        self.image = pygame.image.load("Resource/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = Size * 3
        self.y = Size * 3
        
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
        
    def move(self):
        self.x = random.randint(1,24)*Size
        self.y = random.randint(1,19)*Size
        
class Snake:
    
    def __init__(self, parent_screen, length):
        
        self.parent_screen = parent_screen
        self.block = pygame.image.load("Resource/block.jpg").convert()
        self.direction = "down"
        
        self.length = length
        self.x= [Size]*length
        self.y= [Size]*length
        
    def inc_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
        
    def move_left(self):
        self.direction ="left"
        
    def move_right(self):
        self.direction ="right"
        
    def move_up(self):
        self.direction ="up"
        
    def move_down(self):
        self.direction ="down"
        
    def draw(self):
        self.parent_screen.fill((bgcolor))
        for i in range (self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
        
    def walk(self):
        
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= Size
        if self.direction == 'right':
            self.x[0] += Size
        if self.direction == 'up':
            self.y[0] -= Size
        if self.direction == 'down':
            self.y[0] += Size
            
        self.draw()

class Game:
    
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800))
        self.snake = Snake(self.surface ,1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
    
    def is_collision(self , x1 ,y1 , x2, y2):
        if x1 >= x2 and x1 < x2 + Size:
            if y1 >= y2 and y1 <= y2 + Size:
                return True
        return False
    
    def diplay_score(self):
        font= pygame.font.SysFont('arial',28)
        score = font.render(f"Score: {self.snake.length}" ,True, (200,200,200))
        self.surface.blit(score,(800,10))
              
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.diplay_score()
        pygame.display.flip()
        
        #snake collision with apple
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.apple.move()
            self.snake.inc_length()
            
        # snake collisio with itself
        for i in range (4,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise " Game over"   
                   
    def  show_game_over(self):
        self.surface.fill((bgcolor))
        font= pygame.font.SysFont('arial',28)
        line1 = font.render(f"Score: {self.snake.length}",True, (200,200,200))
        self.surface.blit(line1,(200,300)) 
        line2 = font.render("play again ",True, (200,200,200))
        self.surface.blit(line2 ,(200,350)) 
        pygame.display.flip()
    
    def reset(self):
        self.snake = Snake(self.surface ,1)
        self.apple = Apple(self.surface)
       
    def run(self):
        running= True 
        pause = False
    
        while running:
            for event in pygame.event.get():
            
                if event.type  == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        
                    if event.key == K_RETURN:
                        pause = False
                        
                    if not pause:    
                        if event.key == K_UP:
                            self.snake.move_up()
                        
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                                            
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e :
                self.show_game_over()
                pause = True
                self.reset()
                    
            time.sleep(0.4)         

if __name__ == "__main__":
    game = Game()
    game.run()