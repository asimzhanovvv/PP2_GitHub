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

img_icon = pygame.image.load('Labs/Lab9/Paint/pixelated_image.PNG') # Logo
pygame.display.set_icon(img_icon)


# COLORS
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colors = [colorBLACK, colorRED, colorGREEN, colorBLUE, colorWHITE]
curr_color = colors[0]

# TOOL SETTINGS
thicknesses = [15, 5, 5, 5]  # [Eraser, Brush, Line, Rectangle]
mod = 1  # Current tool (default is Brush)
LMBpressed = False

# TOOLBAR (tools and colors)
tools = ["Eraser", "Brush", "Line", "Rectangle"]
tool_buttons = [pygame.Rect(10 + i * 90, 5, 80, 40) for i in range(len(tools))]
color_buttons = [pygame.Rect(WIDTH - 300 + i * 60, 5, 50, 40) for i in range(len(colors))]

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
        # pygame.draw.circle(surface, curr_color, (prev_x, prev_y), thicknesses[2] // 2)
        # pygame.draw.circle(surface, curr_color, (curr_x, curr_y), thicknesses[2] // 2)
        pygame.draw.line(surface, curr_color, (prev_x, prev_y), (curr_x, curr_y), thicknesses[2])
    elif figure_index == 3:  # Rectangle
        pygame.draw.rect(surface, curr_color, calculate_rect(prev_x, prev_y, curr_x, curr_y), thicknesses[3])

# FINCTION TO CLEAN CANVA
def clear_screen():
    base_layer.fill(colorWHITE)
    screen.fill(colorWHITE)

# TOOLBAR DRAWING
def draw_toolbar():
    # Draw toolbar background
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, TOOLBAR_HEIGHT))
    
    # Draw tool buttons
    for i, rect in enumerate(tool_buttons):
        color = (100, 100, 100) if mod == i else (150, 150, 150)
        pygame.draw.rect(screen, color, rect, 0 , 7)
        font = pygame.font.SysFont('Arial', 14)
        text = font.render(tools[i], True, colorBLACK)
        screen.blit(text, (rect.x + 5, rect.y + 12))
    
    # Draw color buttons
    for i, rect in enumerate(color_buttons):
        pygame.draw.rect(screen, colors[i], rect, 0, 7)
        if curr_color == colors[i]:
            pygame.draw.rect(screen, (100, 100, 100), rect, 2, 7)  # Highlight the selected color

    # Show thickness
    thickness_font = pygame.font.SysFont('Arial', 16)
    thickness_text = thickness_font.render(f"Thickness: {thicknesses[mod]}", True, colorBLACK)
    screen.blit(thickness_text, (WIDTH // 2, 15))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            # Checking tool buttons clicks
            for i, button in enumerate(tool_buttons):
                if button.collidepoint(event.pos):
                    mod = i
                    break
        
            # Checking color button clicks
            for i, button in enumerate(color_buttons):
                if button.collidepoint(event.pos):
                    curr_color = colors[i]
                    break


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
            draw_figure(mod, base_layer)  # Fix the drawing on the canvas

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_e: mod = 0  # Eraser
            if event.key == pygame.K_b: mod = 1  # Brush
            if event.key == pygame.K_l: mod = 2  # Line
            if event.key == pygame.K_r: mod = 3  # Rectangle

            if event.key == pygame.K_1: curr_color = colors[0] # Black
            if event.key == pygame.K_2: curr_color = colors[1] # Red
            if event.key == pygame.K_3: curr_color = colors[2] # Green
            if event.key == pygame.K_4: curr_color = colors[3] # Blue
            if event.key == pygame.K_5: curr_color = colors[4] # White

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

    draw_toolbar()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
