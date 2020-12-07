import pygame
import sys
import random
import pygame_menu
pygame.init()

size_of_block = 20
background_color = (59,153,0)
color_1 = (255,254,255)
color_2= (204,255,204)
color_snake = (204,255,0)
red = (255, 0, 0)
head = 100
head_color = (51,255,102)
size = [625, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
font = pygame.font.SysFont('new times roman', 36)
pygame.init()

class snakeblock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_in(self):
        return 0 < self.x < 30 and 0 < self.y < 28
    def __eq__(self, other):
        return isinstance(other, snakeblock) and self.x == other.x and self.y == other.y

time = pygame.time.Clock()


def draw_snake(color_snake,stroka,stolb):
    pygame.draw.rect(screen, color_snake, [(stolb-1)*21+10, (stroka-1)*21+140, size_of_block, size_of_block])

def draw_block(color_snake,stroka,stolb):
    pygame.draw.rect(screen, color_snake, [(stolb-1)*21+10, (stroka-1)*21+140, size_of_block, size_of_block])

difficult = 1

def set_difficulty(value, difficulty):
    global difficult
    difficult = difficulty

def start_the_game():
    score = 0
    fps = difficult
    def random_block():
        x = random.randint(1, 29)
        y = random.randint(1, 27)
        new_block = snakeblock(x, y)
        while new_block in snake_blocks:
            x = random.randint(0, 29)
            y = random.randint(0, 27)
            new_block = snakeblock(x, y)
        return new_block

    snake_blocks = [snakeblock(5,5),snakeblock(5,6),snakeblock(5 ,7)]
    food = random_block()
    d_1 = 1
    d_2 = 0
    h = 0

    while True:
        snake_coordinates = [[],[]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Вышли')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and h == 0:
                    if (d_2 != 1 and d_1 != 0 and h == 0):
                        d_2 = -1
                        d_1 = 0
                        h += 1
                elif event.key == pygame.K_DOWN and h == 0:
                    if (d_2 != -1 and d_1 != 0 and h == 0):
                        d_2 = 1
                        d_1 = 0
                        h += 1
                elif event.key == pygame.K_LEFT and h == 0:
                    if (d_1 != 1 and d_2 != 0 and h == 0):
                        d_1 = -1
                        d_2 = 0
                        h += 1
                elif event.key == pygame.K_RIGHT and h == 0:
                    if (d_1 != -1 and d_2 != 0 and h == 0):
                        d_1 = 1
                        d_2 = 0
                        h += 1
                elif event.key == pygame.K_SPACE:
                    if fps == 0.0000001:
                        fps = 2
                    else:
                        fps = 0.0000001
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

        text_total = font.render(f"Ваша длина: {score}", 20, color_1)
        screen.blit(text_total, (size_of_block, size_of_block))
        text_fps = font.render(f"Ваш уровень: {fps - 1}", 20, color_1)
        screen.blit(text_fps, (size_of_block + 250, size_of_block))
        head_snake = snake_blocks[-1]

        if not head_snake.is_in():
            l.append(score)
            l.sort()
            print('Врезались,ваша длина:',score,'Максимальная длина за сессию :',l[len(l) - 1])
            break
        draw_block(red, food.y, food.x)

        for block in snake_blocks:
            draw_snake(color_snake, block.y, block.x)
        h = 0
        pygame.display.flip()
        if food == snake_blocks[-1]:
            snake_blocks.append(food)
            food = random_block()
            score += 1
            if score % 5 == 0:
                fps += 1

        new_head_snake = snakeblock(head_snake.x + d_1, head_snake.y + d_2)
        if new_head_snake in snake_blocks:
            l.append(score)
            l.sort()
            print('Врезались в себя, ваша длина:', score, 'Максимальная длина за сессию :',l[len(l) - 1])
            break
        snake_blocks.append(new_head_snake)
        snake_blocks.pop(0)

        time.tick(fps)



menu = pygame_menu.Menu(800, 625, 'Приветствуем в игре "Змейка"',theme=pygame_menu.themes.THEME_DARK)
l=[]

menu.add_text_input('Введите ваше имя :', default='Игрок ')
menu.add_selector('Выберете сложность :', [('Очень легко', 1),('Легко',2),('Нормально',3),('Тяжелый',4),('Серьезный', 5),("Невозможный",6),("Безграничный",7),("Экстрим",8),("Безграничный",15)], onchange=set_difficulty)
menu.add_button('Играть', start_the_game)
menu.add_button('Выход из игры', pygame_menu.events.EXIT)
menu.mainloop(screen)
