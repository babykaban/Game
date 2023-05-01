import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the clock
clock = pygame.time.Clock()
fps = 33

# Set up the key flag
key_pressed = False

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            # Ignore key presses if a key is already pressed
            if not key_pressed:
                key_pressed = True
                # Handle the key press here

        elif event.type == pygame.KEYUP:
            key_pressed = False

    # Update the game state here

    # Draw the screen here

    # Limit the frame rate

    print(clock.tick(fps))
