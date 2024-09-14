import pygame
import random
import math

def normaliseAngle(angle):
    newAngle = angle % 360
    if newAngle < 0:
        newAngle += 360
    return newAngle

def main():
    pygame.init()
    screenWidth = 650
    screenHeight = 350
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    fps = 60
    player1 = pygame.Rect(10, screenHeight // 2 - 50, 10, 100)
    player2 = pygame.Rect(screenWidth - 20, screenHeight // 2 - 50, 10, 100)
    playerSpeed = 3
    ball = pygame.Rect(screenWidth // 2, screenHeight // 2, 10, 10)
    ballSpeed = 3
    gameRunning = True
    ballDirection = 270

    if event.type == pygame.QUIT:
        gameRunning = False
    while gameRunning:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            gameRunning = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top >= 0:
            player1.move_ip(0, -playerSpeed)
        elif keys[pygame.K_s] and player1.bottom < screenHeight:
            player1.move_ip(0, playerSpeed)

        if keys[pygame.K_UP] and player2.top >= 0:
            player2.move_ip(0, -playerSpeed)
        elif keys[pygame.K_DOWN] and player2.bottom < screenHeight:
            player2.move_ip(0, playerSpeed)

        def move(ball, ballDirection):
            angleInRadians = math.radians(ballDirection - 90)
            x = math.cos(angleInRadians) * ballSpeed
            y = -math.sin(angleInRadians) * ballSpeed
            ball.move_ip(x, y)

        if ball.left <= 0  or ball.right >= screenWidth or ball.top <= 0 or ball.bottom >= screenHeight or (ball.left <= player1.right and ball.bottom >= player1.top and ball.top <= player1.bottom) or (ball.right >= player2.left and ball.bottom >= player2.top and ball.top <= player2.bottom):
            if ball.left <= 0 or ball.right >= screenWidth:
                ballSpeed = 3
                ball.move_ip(screenWidth // 2, screenHeight // 2)
            else:
                ballSpeed += 0.25
                ballDirection = normaliseAngle(ballDirection + random.randint(-90, 90) + 180)
                move(ball, ballDirection)
        else:
            move(ball, ballDirection)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), player1)
        pygame.draw.rect(screen, (255, 255, 255), player2)
        pygame.draw.rect(screen, (255, 255, 255), ball)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
main()
