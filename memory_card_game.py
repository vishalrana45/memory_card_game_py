import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((400, 450))
pygame.display.set_caption("Memory Game")

def reset():
    global cards, open_cards, matched

    cards = ["A","A","B","B","C","C","D","D",
             "E","E","F","F","G","G","H","H"]

    random.shuffle(cards)
    open_cards = []
    matched = []

reset()

while True:
    screen.fill((60, 60, 100))

    # draw cards
    for i in range(16):
        x = (i % 4) * 100
        y = (i // 4) * 100

        pygame.draw.rect(screen, (200,200,200), (x+10,y+10,80,80))

        if i in open_cards or i in matched:
            font = pygame.font.SysFont(None, 50)
            text = font.render(cards[i], True, (0,0,0))
            screen.blit(text, (x+35, y+25))

    # win text
    if len(matched) == 16:
        font = pygame.font.SysFont(None, 50)
        win = font.render("YOU WIN", True, (0,255,0))
        screen.blit(win, (120, 360))

    # TRY AGAIN button
    pygame.draw.rect(screen, (255,180,0), (120,400,160,40))
    font = pygame.font.SysFont(None, 40)
    text = font.render("TRY AGAIN", True, (0,0,0))
    screen.blit(text, (130, 405))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mx, my = event.pos

            # restart button
            if mx > 120 and mx < 280 and my > 400:
                reset()
                continue

            if my < 100:
                row = 0
            elif my < 200:
                row = 1
            elif my < 300:
                row = 2
            else:
                row = 3

            if mx < 100:
                col = 0
            elif mx < 200:
                col = 1
            elif mx < 300:
                col = 2
            else:
                col = 3

            i = row * 4 + col

            if i < 16:
                if i not in open_cards and i not in matched:
                    open_cards.append(i)

            if len(open_cards) == 2:
                pygame.display.update()
                time.sleep(0.5)

                if cards[open_cards[0]] == cards[open_cards[1]]:
                    matched.append(open_cards[0])
                    matched.append(open_cards[1])

                open_cards = []

pygame.quit()   