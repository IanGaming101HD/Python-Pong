import pygame
import random
import math

def normaliseAngle(angle):
    newAngle = angle % 360
    if newAngle < 0:
        newAngle += 360
    return newAngle

def drawCentreLine(screen):
    x = screen.get_width() // 2
    y = 10
    while y < screen.get_height():
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + 5), width = 5)
        y += 5 + 5

def main():
    pygame.init()
    screenWidth = 650
    screenHeight = 350
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    fps = 60
    scoreFont = pygame.font.SysFont('Arial', 75)
    startingMessageFont = pygame.font.SysFont('Arial', 40)
    player1 = pygame.Rect(10, screenHeight // 2 - 50, 10, 100)
    player2 = pygame.Rect(screenWidth - 20, screenHeight // 2 - 50, 10, 100)
    player1Score = 0
    player2Score = 0
    playerSpeed = 3
    ball = pygame.Rect(screenWidth // 2, screenHeight // 2, 10, 10)
    # ballSpeed = 3
    ballSpeed = 5
    gameRunning = True
    gameStarted = False
    ballDirection = 270

    while gameRunning:
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()

        screen.fill((0, 0, 0))
        player1ScoreText = scoreFont.render('{:02}'.format(player1Score), False, (255, 255, 255))
        player2ScoreText = scoreFont.render('{:02}'.format(player2Score), False, (255, 255, 255))
        startingMessageText = startingMessageFont.render('Press any key to begin', False, (255, 255, 255))
        startingMessageRect = startingMessageText.get_rect(center = (screenWidth // 2, screenHeight // 2))

        drawCentreLine(screen)
        screen.blit(player1ScoreText, (5, 5))
        screen.blit(player2ScoreText, (screenWidth - 100, 5))
        pygame.draw.rect(screen, (255, 255, 255), player1)
        pygame.draw.rect(screen, (255, 255, 255), player2)
        pygame.draw.rect(screen, (255, 255, 255), ball)

        if event.type == pygame.QUIT:
            gameRunning = False
        if not gameStarted:
            screen.blit(startingMessageText, startingMessageRect)
            if True in keys:
                gameStarted = True
        else:
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
                    if ball.left <= 0:
                        player2Score += 1
                        ballDirection = 270
                    else:
                        player1Score += 1
                        ballDirection = 90
                    ballSpeed = 3
                    ball.center = (screenWidth // 2, screenHeight // 2)
                else:
                    # ballSpeed += 0.25
                    ballDirection = normaliseAngle(ballDirection + random.randint(-89, 89) + 180)
                    move(ball, ballDirection)
            else:
                move(ball, ballDirection)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
main()