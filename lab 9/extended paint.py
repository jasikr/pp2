import pygame
import math

def draw_right_triangle(screen, color, start_pos, end_pos):
    """Draws a right-angled triangle between two points."""
    points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
    pygame.draw.polygon(screen, color, points)

def draw_equilateral_triangle(screen, color, start_pos, end_pos):
    """Draws an equilateral triangle with one vertex at start_pos and base parallel to x-axis."""
    length = math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    height = length * math.sqrt(3) / 2
    vertex2 = (start_pos[0] + length / 2, start_pos[1] - height)
    vertex3 = (start_pos[0] - length / 2, start_pos[1] - height)
    pygame.draw.polygon(screen, color, [start_pos, vertex2, vertex3])

def draw_rhombus(screen, color, start_pos, end_pos):
    """Draws a rhombus using the line between start_pos and end_pos as one of its diagonals."""
    dx = (end_pos[0] - start_pos[0]) / 2
    dy = (end_pos[1] - start_pos[1]) / 2
    vertex1 = (start_pos[0] + dx, start_pos[1] + dy)
    vertex2 = (start_pos[0] - dy, start_pos[1] + dx)
    vertex3 = (start_pos[0] - dx, start_pos[1] - dy)
    vertex4 = (start_pos[0] + dy, start_pos[1] - dx)
    pygame.draw.polygon(screen, color, [vertex1, vertex2, vertex3, vertex4])

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Use keys R, G, B to change color; D, E, C, S, T, Q, H for shapes")
    clock = pygame.time.Clock()

    radius = 15
    points = []
    mode = 'draw'
    color = (0, 0, 255)
    drawing = False
    start_pos = None
    max_radius = 100
    background_color = (255, 255, 255)

    print("Instructions:")
    print("R, G, B - Change colors to Red, Green, Blue respectively.")
    print("D - Draw mode. E - Erase mode.")
    print("C - Circle mode. S - Square mode.")
    print("T - Right triangle mode. Q - Equilateral triangle mode. H - Rhombus mode.")
    print("Press ESC or close window to exit.")

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
                elif event.key == pygame.K_t:
                    mode = 'right_triangle'
                elif event.key == pygame.K_q:
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True
                start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False
                if mode in ['circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                    end_pos = event.pos
                    points.append((mode, color, start_pos, end_pos))

            if event.type == pygame.MOUSEMOTION and drawing and mode in ['draw', 'erase']:
                points.append((mode, color, event.pos))

        screen.fill(background_color)

        for item in points:
            if item[0] == 'draw':
                pygame.draw.circle(screen, item[1], item[2], radius)
            elif item[0] == 'erase':
                pygame.draw.circle(screen, background_color, item[2], radius)  
            elif item[0] == 'circle':
                circle_radius = min(max_radius, int(math.hypot(item[2][0] - item[3][0], item[2][1] - item[3][1])))
                pygame.draw.circle(screen, item[1], item[2], circle_radius)
            elif item[0] == 'square':
                pygame.draw.rect(screen, item[1], pygame.Rect(item[2], (item[3][0] - item[2][0], item[3][1] - item[2][1])))
            elif item[0] == 'right_triangle':
                draw_right_triangle(screen, item[1], item[2], item[3])
            elif item[0] == 'equilateral_triangle':
                draw_equilateral_triangle(screen, item[1], item[2], item[3])
            elif item[0] == 'rhombus':
                draw_rhombus(screen, item[1], item[2], item[3])

        if drawing and mode in ['circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
            current_pos = pygame.mouse.get_pos()
            if mode == 'circle':
                temp_radius = min(max_radius, int(math.hypot(start_pos[0] - current_pos[0], start_pos[1] - current_pos[1])))
                pygame.draw.circle(screen, color, start_pos, temp_radius)
            elif mode == 'square':
                pygame.draw.rect(screen, color, pygame.Rect(start_pos, (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])))
            # Temporary shapes for new modes
            elif mode == 'right_triangle':
                draw_right_triangle(screen, color, start_pos, current_pos)
            elif mode == 'equilateral_triangle':
                draw_equilateral_triangle(screen, color, start_pos, current_pos)
            elif mode == 'rhombus':
                draw_rhombus(screen, color, start_pos, current_pos)

        pygame.display.flip()
        clock.tick(60)

main()
