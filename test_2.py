import pygame

pygame.init()

# Set up the Pygame display surface
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Define the arrow's dimensions and position
arrow_x, arrow_y = 100, 100
arrow_width, arrow_height = 50, 20

# Create a list of points for the arrow's polygon shape
arrow_points = [(arrow_x, arrow_y),
                (arrow_x + arrow_width, arrow_y),
                (arrow_x + arrow_width, arrow_y + arrow_height // 2),
                (arrow_x + arrow_width * 2, arrow_y + arrow_height // 2),
                (arrow_x + arrow_width * 2, arrow_y + arrow_height),
                (arrow_x, arrow_y + arrow_height)]

# Draw the arrow on the screen
arrow_color = (255, 0, 0)  # Red
pygame.draw.polygon(screen, arrow_color, arrow_points)

# Update the display
pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
