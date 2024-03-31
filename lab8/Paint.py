import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    points = []
    mode = 'draw'
    color = (0, 0, 255)
    drawing = False
    start_pos = None
    max_radius = 100  # Maximum radius for the circle
    background_color = (255, 255, 255)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                # Color selection
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)

                # Mode selection
                if event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_s:
                    mode = 'square'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    drawing = True
                    start_pos = event.pos
                    if mode in ['draw', 'erase']:
                        points.append((mode, event.pos))

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left click
                    drawing = False
                    if mode == 'circle':
                        end_pos = event.pos
                        circle_radius = min(max_radius, int(((start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2) ** 0.5))
                        points.append((mode, color, start_pos, circle_radius))
                    elif mode == 'square':
                        end_pos = event.pos
                        points.append((mode, color, start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0] and mode in ['draw', 'erase']:
                    points.append((mode, event.pos))

        screen.fill(background_color)

        # Draw all shapes
        for item in points:
            if item[0] == 'draw':
                pygame.draw.circle(screen, color, item[1], radius)
            elif item[0] == 'erase':
                pygame.draw.circle(screen, background_color, item[1], radius)
            elif item[0] == 'circle':
                pygame.draw.circle(screen, item[1], item[2], item[3])
            elif item[0] == 'square':
                pygame.draw.rect(screen, item[1], pygame.Rect(item[2], item[3]))

        if drawing and mode in ['circle', 'square']:
            current_pos = pygame.mouse.get_pos()
            if mode == 'circle':
                temp_radius = min(max_radius, int(((start_pos[0] - current_pos[0]) ** 2 + (start_pos[1] - current_pos[1]) ** 2) ** 0.5))
                pygame.draw.circle(screen, color, start_pos, temp_radius)
            elif mode == 'square':
                pygame.draw.rect(screen, color, pygame.Rect(start_pos, (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])))

        pygame.display.flip()
        clock.tick(60)

main()

#Instructions:
#The color can be changed by pressing the 'r', 'g', or 'b' keys for red, green, and blue, respectively.
#Drawing mode is activated by pressing the 'd' key, eraser mode by pressing the 'e' key, circle mode by pressing the 'c' key, and square mode by pressing the 's' key.

#How erase:
#When drawing, the color is determined by the mode: it uses the selected color for 'draw' and the background_color for 'erase'.
#This ensures that the eraser mode effectively removes the drawings by painting over them with the background color.