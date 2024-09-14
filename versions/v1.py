import pygame

def main():
    pygame.init()
    screenWidth = 650
    screenHeight = 300
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    player1 = pygame.Rect(10, screenHeight // 2, 10, 100)
    player2 = pygame.Rect(screenWidth - 20, screenHeight // 2, 10, 100)
    increment = 5

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if player1.top > 0:
                    player1.move_ip(0, -increment)
            elif event.key == pygame.K_DOWN:
                if player1.bottom < (screenHeight - player1.bottom):
                    player1.move_ip(0, increment)
            if event.key == pygame.K_w:
                if player2.top > 0:
                    player1.move_ip(0, -increment)
            elif event.key == pygame.K_s:
                if player2.bottom < (screenHeight - player2.bottom):
                    player1.move_ip(0, increment)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), player1)
        pygame.draw.rect(screen, (255, 255, 255), player2)
        pygame.display.flip()
    pygame.quit()
main()
