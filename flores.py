import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flowers")

WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 234, 0)
YELLOW_2 = (220, 220, 0)
BLACK = (0, 0, 0)
BROWN = (218, 165, 32)

clock = pygame.time.Clock()

screen.fill(LIGHT_BLUE)

drawn = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not drawn:
        prev_x, prev_y = [], []
        for i in range(19):

            petal_surface = pygame.Surface((200, 30), pygame.SRCALPHA)
            petal_surface_2 = pygame.Surface((200, 30), pygame.SRCALPHA)
            petal_back = pygame.Surface((202, 31), pygame.SRCALPHA)
            center_surface = pygame.Surface((70, 70), pygame.SRCALPHA)
            center_back = pygame.Surface((72, 72), pygame.SRCALPHA)
            pygame.draw.ellipse(petal_surface, YELLOW, (0, 0, 200, 28))
            pygame.draw.ellipse(petal_surface_2, YELLOW_2, (0, 0, 200, 28))
            pygame.draw.ellipse(petal_back, BLACK, (0, 0, 202, 30))
            pygame.draw.ellipse(center_surface, BROWN, (0, 0, 70, 70))
            pygame.draw.ellipse(center_back, BLACK, (0, 0, 72, 72))

            close = True
            while close:
                ran_x = random.randint(80, 720)
                ran_y = random.randint(150, 720)

                close = False
                for i in range(len(prev_x)):
                    if abs(ran_x - prev_x[i]) < 110 and abs(ran_y - prev_y[i]) < 110:
                        close = True
            
            prev_x.append(ran_x)
            prev_y.append(ran_y)
            
            for j in range(0, 360, 20):
                back_rotated = pygame.transform.rotate(petal_back, j)
                rect_back = back_rotated.get_rect(center=(ran_x, ran_y))
                rec_center_back = center_back.get_rect(center=(ran_x, ran_y))
                screen.blit(back_rotated, rect_back)

                petal_rotated = pygame.transform.rotate(petal_surface, j)
                petal_rotated_2 = pygame.transform.rotate(petal_surface_2, j)
                rect_petal = petal_rotated.get_rect(center=(ran_x, ran_y))
                rect_petal_2 = petal_rotated_2.get_rect(center=(ran_x, ran_y))
                rect_center = center_surface.get_rect(center=(ran_x, ran_y))
                if j % 40 == 0:
                    screen.blit(petal_rotated, rect_petal)
                else:
                    screen.blit(petal_rotated_2, rect_petal_2)

                pygame.display.flip()

                clock.tick(70)
            screen.blit(center_back, rec_center_back)
            screen.blit(center_surface, rect_center)
        
        msg = 'Feliz primavera enana'
        msg_count = ''
        font = pygame.font.Font('Streetwear.otf', 48)
        for letter in msg:
            msg_count += letter
            text = font.render(msg_count, True, BLACK)
            screen.blit(text, (80, 50))
            clock.tick(8)
            pygame.display.flip()


        drawn = True

    pygame.display.flip()
    clock.tick(20)
        