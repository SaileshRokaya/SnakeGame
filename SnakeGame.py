import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# Colors
Pink = (233,210, 229)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 200, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background Image
bgimg = pygame.image.load("wc.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

bgimg1 = pygame.image.load("over.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()

bgimg2 = pygame.image.load("bgmain.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game By Sailesh")
pygame.display.update()
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()

def plot_snak(gameWindow, color, snk_list , snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def welcome():
    exit_game = False
    while not exit_game:
        pygame.mixer.music.load('3.mp3')
        pygame.mixer.music.play()
        gameWindow.fill(black)
        gameWindow.blit(bgimg, (0, 0))
        # text_screen("Welcome To Snake Game", white, 225, 240)
        # text_screen("Press Space Bar To Play", red, 232, 290)
        # text_screen("By Mr. Sailesh Rokaya", white, 460, 540)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('1.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    snk_list = []
    snk_length = 1

    # Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5

    snake_size = 10
    fps = 60



    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(black)
            gameWindow.blit(bgimg1, (0, 0))
            text_screen("               " + str(hiscore) + "                                  " + str(score), red, 210, 414)
            # text_screen("Game Over! Press Enter To Continue.", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('1.mp3')
                        pygame.mixer.music.play()
                        gameloop()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 1 * 3
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 3
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(Pink)
            gameWindow.blit(bgimg2, (0, 0))
            text_screen("               " + str(score) + "                      " + str(hiscore), red, 5, 5)

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('2.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('2.mp3')
                pygame.mixer.music.play()

            plot_snak(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
