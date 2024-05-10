import math
n=input("Введите целое число: ")
while type(n) !=int:
    try:
        n=int(n)
    except ValueError:
        print('Непраильно ввели!')
        n=input("Введите целое число: ")

if not(math.fmod(n,2)):
    print("Четное")
else:
    print('Нечетное')






import pygame, sys, random


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

light_grey = (200,200,200)
bg_color = pygame.Color(37, 71, 33)

ball = pygame.Rect(625, 335, 30, 30)
player1 = pygame.Rect(1260, 280, 10, 140)
player2 = pygame.Rect(10, 280, 10, 140)

ball_speed_x = 7
ball_speed_y = 7

player1_speed = 0
player2_speed = 0

player1_score = 0
player2_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

while True:

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        ball.center = (screen_width / 2, screen_height / 2)
        ball_speed_y *= random.choice((1, -1))
        ball_speed_x *= random.choice((1, -1))
        player1_score += 1

    if ball.right >= screen_width:
        ball.center = (screen_width / 2, screen_height / 2)
        ball_speed_y *= random.choice((1, -1))
        ball_speed_x *= random.choice((1, -1))
        player2_score += 1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    player1.y += player1_speed
    player2.y += player2_speed

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                 player1_speed -= 7
            if event.key == pygame.K_DOWN:
                    player1_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_speed += 7
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                 player2_speed -= 7
            if event.key == pygame.K_s:
                    player2_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player2_speed += 7
            if event.key == pygame.K_s:
                player2_speed -= 7


    player1_text = basic_font.render(f'{player1_score}', False, light_grey)
    screen.blit(player1_text, (660, 470))

    player2_text = basic_font.render(f'{player2_score}', False, light_grey)
    screen.blit(player2_text, (600, 470))


    pygame.display.flip()
    clock.tick(60)