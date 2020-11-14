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

def Choice_Random(axis):

    Random1 = np.random.randint(0 , axis)
    Random2 = np.random.randint(0 , axis)
    print(Random1 , Random2)
    return Random1 , Random2

def player(X , y , screen):
    screen.blit(SorSar , (X , y))


def get_tile_color(till_cons):
    tile_color = (255 , 255 , 255)
    if till_cons == "s":
        tile_color = (220 , 12 , 90 )
    elif till_cons  == "o":
        tile_color = (0 , 0 , 0)
    return tile_color

def draw_graid(surface ):
    Color = (0,150,255)
    for i in range(number_of_block_width):
        new_hight = round(i * block_hight )
        new_width = round(i * block_width )
        pygame.draw.line(surface , Color , (0 , new_hight) , (Screen_width , new_hight) , 2)
        pygame.draw.line(surface , Color , (new_width , 0) , (new_width , Screen_hight) , 2)

def game_loop(screen , axis , block_hight , block_width):
    matrix  = np.zeros((axis , axis))
    freq_matrix = np.array(matrix , copy = True)
    
    Sum = 0
    index = 0
    Last_time = axis **2
    
    while True:
        index = index + 1
        screen.fill((255 , 255 , 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_graid(screen)
        Random1 , Random2 = Choice_Random(axis)
        x , y = Matrix[Random1][Random2][0] , Matrix[Random1][Random2][1]
        matrix[Random1][Random2] +=1
        
        if freq_matrix[Random1][Random2] == 0:
            freq_matrix[Random1][Random2] = 1
            Sum = Sum + 1
        if Sum == Last_time:
            print("Done After {} Step ".format(index))   
            print(matrix6)
            pygame.quit()
            sys.exit()
        
        player(x , y , screen)
        time.sleep(0.19)
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