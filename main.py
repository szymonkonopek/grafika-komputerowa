import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Line Drawing")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initial line coordinates (default)
x1, y1 = 50, 50
x2, y2 = 400, 300

def draw_line(x1, y1, x2, y2, color, delay=2):
    """Draw a line from (x1, y1) to (x2, y2) using Bresenham's Algorithm, updating each pixel visibly."""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        screen.set_at((x1, y1), color)  # Set pixel at (x1, y1)
        pygame.display.flip()  # Update screen to show the new pixel
        pygame.time.delay(delay)  # Delay for visibility
        
        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy


# Main loop
running = True
while running:
    screen.fill(BLACK)  # Clear screen before each new line draw

    # Draw the line progressively
    draw_line(x1, y1, x2, y2, WHITE)

    # Wait before redrawing the line
    pygame.time.delay(500)

    # Event handling (mouse clicks to set start and end points)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if event.button == 1:  # Left click → Set start point
                x1, y1 = mx, my
            elif event.button == 3:  # Right click → Set end point
                x2, y2 = mx, my

pygame.quit()
