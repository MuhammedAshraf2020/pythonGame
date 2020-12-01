import pygame
import sys
import time
import numpy as np

Screen_width = 500
Screen_hight = 500

number_of_block_width = int(input("Enter axis nums:"))
number_of_block_high = number_of_block_width

block_hight = round(Screen_hight / number_of_block_high )
block_width = round(Screen_width / number_of_block_width )


SorSar = pygame.image.load("cockroach.png")


def Create_places(step , number_of_blocks):
    init_place = int(step // 2)
    x_places = [i * step + init_place for  i in range(number_of_blocks )]
    return x_places
 
Places = np.array(Create_places( block_hight , number_of_block_width ))

def CreateMatrix(List):
    Matrix = list()
    for i in List:
        array = []
        for j in List:
            array.append((i , j))
        Matrix.append(array)
    return np.array(Matrix)

Matrix = CreateMatrix(Places)

def Choice_Random(Random1 , Random2):
    axisX = [Random1 - 1 , Random1 , Random1+1]
    axisY = [Random2 - 1 , Random2 , Random2 + 1]
    Random1 = np.random.choice(axisX)
    Random2 = np.random.choice(axisY)
    print(Random1 , Random2)
    return Random1 , Random2

def player(X , y , screen):
    screen.blit(SorSar , (X , y))


def draw_graid(surface ):
    Color = (0,150,255)
    for i in range(number_of_block_width):
        new_hight = round(i * block_hight )
        new_width = round(i * block_width )
        pygame.draw.line(surface , Color , (0 , new_hight) , (Screen_width , new_hight) , 2)
        pygame.draw.line(surface , Color , (new_width , 0) , (new_width , Screen_hight) , 2)

def game_loop(screen , axis , block_hight , block_width):

    matrix  = np.zeros((axis , axis))    
    Sum = 0
    index = 0
    Last_time = axis **2
    Random1 , Random2 = 2 , 2
    while True:
        
        index = index + 1
        screen.fill((255 , 255 , 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_graid(screen)
        RandomTemp = (Random1 , Random2)
        Random1 , Random2 = Choice_Random(Random1 , Random2)
        if (Random1 not in range(0 , axis) or Random2 not in range(0 , axis)):
            Random1 , Random2 = RandomTemp[0] , RandomTemp[1]
            x , y = Matrix[Random1][Random2][0] , Matrix[Random1][Random2][1]
        else:
            x , y = Matrix[Random1][Random2][0] , Matrix[Random1][Random2][1]
        
        if matrix[Random1][Random2] == 0:
            Sum = Sum + 1
            
        matrix[Random1][Random2] +=1
        
        if Sum == Last_time:
            print("Done After {} Step ".format(index))   
            print(matrix)
            pygame.quit()
            sys.exit()
        
        player(x , y , screen)
        time.sleep(0.25)
        pygame.display.update()


def initialize_game(Screen_width  , Screen_depth ):
    pygame.init()
    screen = pygame.display.set_mode((Screen_width , Screen_depth))
    pygame.display.set_caption("SorSar")
    return screen
    

def main(axis ):
    screen = initialize_game(Screen_width  , Screen_hight)
    game_loop(screen , axis , block_hight , block_width)

if __name__ == "__main__":
    main(number_of_block_width)
