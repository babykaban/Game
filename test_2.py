import pygame

pygame.init()

font = pygame.font.Font(None, 36)
text_surface = font.render("Your text here", True, (0, 0, 0))

text_width = text_surface.get_width()
text_height = text_surface.get_height()

line_surface = pygame.Surface((text_width, int(text_height)))
line_surface.fill((200, 200, 200))

line_surface.blit(text_surface, (0, 0))

screen = pygame.display.set_mode((800, 600))
screen.blit(line_surface, (100, 100))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()