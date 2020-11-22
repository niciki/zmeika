import pygame
import math

size_of_block = 20
background_color = (59,153,0)
color_1 = (255,254,255)
color_2= (204,255,204)
color_snake = (204,255,0)
head = 100
head_color = (51,255,102)
size = [625, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

class snakeblock:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_snake(color_snake,stroka,stolb):
    pygame.draw.rect(screen, color_snake, [(stolb-1)*21+10, (stroka-1)*21+140, size_of_block, size_of_block])

snake_block = [snakeblock(1,2)]
while True:
    snake_coordinates = [[],[]]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(background_color)
    for number_stroka in range(10, 600, 42):
        for number_stolb in range(20+head+20, 700, 42):
            pygame.draw.rect(screen, color_1, [number_stroka, number_stolb, size_of_block, size_of_block])
    for number_stroka_2 in range(31, 600, 42):
        for number_stolb_2 in range(41+head+20, 700, 42):
            pygame.draw.rect(screen, color_2, [number_stroka_2, number_stolb_2, size_of_block, size_of_block])
    for number_stroka in range(31, 600, 42):
        for number_stolb in range(20+head+20, 700, 42):
            pygame.draw.rect(screen, color_1, [number_stroka, number_stolb, size_of_block, size_of_block])
    for number_stroka_2 in range(10, 600, 42):
        for number_stolb_2 in range(41+head+20, 700, 42):
            pygame.draw.rect(screen, color_1, [number_stroka_2, number_stolb_2, size_of_block, size_of_block])
    pygame.draw.rect(screen, head_color, [0, 0, 625, 120])
    for block in snake_block:
        draw_snake(color_snake,15,10)

    pygame.display.flip()
