import pygame

pygame.init()

# BASE SETTINGS
WIDTH, HEIGHT = 1000, 800
TOOLBAR_HEIGHT = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')
screen.fill((255, 255, 255)) 
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # White background for the canvas
clock = pygame.time.Clock()

img_icon = pygame.image.load('Labs/Lab8/Paint/pixelated_image.PNG') # Logo
pygame.display.set_icon(img_icon)


# COLORS
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colors = [colorBLACK, colorRED, colorBLUE]
curr_color = colors[0]

# TOOL SETTINGS
thicknesses = [15, 5, 5, 5]  # [Eraser, Brush, Line, Rectangle]
mod = 1  # Current tool (default is Brush)
LMBpressed = False

# Initializing mouse coordinates
mouse_x, mouse_y = pygame.mouse.get_pos()
curr_x, curr_y = mouse_x, mouse_y
prev_x, prev_y = mouse_x, mouse_y


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# FINCTION TO DRAW FIGURES
def draw_figure(figure_index, surface):
    if figure_index == 0:  # Eraser
        pygame.draw.circle(surface, colorWHITE, (curr_x, curr_y), thicknesses[0] // 2)
        pygame.draw.line(surface, colorWHITE, (prev_x, prev_y), (curr_x, curr_y), thicknesses[0])
    elif figure_index == 1:  # Brush
        pygame.draw.circle(surface, curr_color, (curr_x, curr_y), thicknesses[1] // 2)
        pygame.draw.line(surface, curr_color, (prev_x, prev_y), (curr_x, curr_y), thicknesses[1])
    elif figure_index == 2:  # Line
        pygame.draw.line(surface, curr_color, (prev_x, prev_y), (curr_x, curr_y), thicknesses[2])
    elif figure_index == 3:  # Rectangle
        pygame.draw.rect(surface, curr_color, calculate_rect(prev_x, prev_y, curr_x, curr_y), thicknesses[3])

def clear_screen():
    base_layer.fill(colorWHITE)
    screen.fill(colorWHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            curr_x, curr_y = event.pos
            prev_x, prev_y = event.pos

        if event.type == pygame.MOUSEMOTION and LMBpressed:
            if mod in [0, 1]:  # Eraser and Brush draw immediately
                prev_x, prev_y = curr_x, curr_y
                curr_x, curr_y = event.pos
                draw_figure(mod, base_layer)
            elif mod in [2, 3]:  # Line and Rectangle are temporarily drawn on the screen
                curr_x, curr_y = event.pos

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            draw_figure(mod, base_layer)   # Fix the drawing on the canvas

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_e: mod = 0  # Eraser
            if event.key == pygame.K_b: mod = 1  # Brush
            if event.key == pygame.K_l: mod = 2  # Line
            if event.key == pygame.K_r: mod = 3  # Rectangle

            if event.key == pygame.K_1: curr_color = colors[0]
            if event.key == pygame.K_2: curr_color = colors[1]
            if event.key == pygame.K_3: curr_color = colors[2]

            if event.key == pygame.K_c:  # Clear screen with 'C' key
                clear_screen()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_PLUS ] or keys[pygame.K_RIGHTBRACKET]:
            # print("increased thickness")
            if thicknesses[mod] <= 64:
                thicknesses[mod] += 1
        if keys[pygame.K_KP_MINUS]or keys[pygame.K_LEFTBRACKET]:
            # print("reduced thickness")
            if thicknesses[mod] >= 2:
                thicknesses[mod] -= 1

    screen.blit(base_layer, (0, 0))
    
    if LMBpressed and mod in [2, 3]:
        draw_figure(mod, screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
