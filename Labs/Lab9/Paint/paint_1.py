import pygame

pygame.init()

# BASE SETTINGS
WIDTH, HEIGHT = 1000, 800
TOOLBAR_HEIGHT = 100
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
colorYELLOW = (255, 255, 0)
colorPURPLE = (128, 0, 128)
colorORANGE = (255, 165, 0)
colorPINK = (255, 192, 203)
colors = [colorBLACK, colorRED, colorGREEN, colorBLUE, colorWHITE, colorYELLOW, colorPURPLE, colorORANGE, colorPINK]
curr_color = colors[0]

# TOOL SETTINGS
thicknesses = [15, 5, 5, 5, 5, 5, 5, 5]  # [Eraser, Brush, Line, Rectangle, Circle, Diamond, R_triangle, E_Triangle]
mod = 1  # Current tool (default is Brush)
LMBpressed = False

# TOOLBAR (tools and colors)
tools = ["Eraser", "Brush", "Line", "Rectangle","Circle", "Diamond", "R_Triangle", "E_Triangle"] 

tool_buttons = [pygame.Rect(10 + i * 90, 5, 80, 40) if i <=3 else pygame.Rect(10 + (i-4) * 90, 55, 80, 40) for i in range(len(tools))]
color_buttons = [pygame.Rect(WIDTH - 300 + i * 60, 5, 50, 40) if i <=4 else pygame.Rect(WIDTH - 300 + (i-5) * 60, 55, 50, 40) for i in range(len(colors))]

# Initializing mouse coordinates
mouse_x, mouse_y = pygame.mouse.get_pos()
curr_x, curr_y = mouse_x, mouse_y
prev_x, prev_y = mouse_x, mouse_y


# Calculate rectangle coordinates from two points
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# Calculate the four points of a diamond/rhombus
def calculate_diamond_points(x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    width = abs(x2 - x1) // 2
    height = abs(y2 - y1) // 2
    return [
        (center_x, center_y - height),  # Top
        (center_x + width, center_y),   # Right
        (center_x, center_y + height),  # Bottom
        (center_x - width, center_y)    # Left
    ]

# Calculate points for a right-angled triangle (right angle at start point)
def calculate_right_triangle_points(x1, y1, x2, y2):
    return [
        (x1, y1),  # Right angle vertex
        (x1, y2),  # Vertical leg
        (x2, y2)   # Horizontal leg
    ]

# Calculate points for an equilateral triangle
def calculate_equilateral_triangle_points(x1, y1, x2, y2):
    side_length = max(abs(x2 - x1), abs(y2 - y1))
    height = ((3**0.5)/2) * side_length
    
    # Determine direction
    if x2 < x1:
        side_length = -side_length
    
    return [
        (x1, y1),  # Top vertex
        (x1 + side_length/2, y1 + height),  # Bottom right
        (x1 - side_length/2, y1 + height)   # Bottom left
    ]

# FINCTION TO DRAW FIGURES
def draw_figure(figure_index, surface):
    if figure_index == 0:  # Eraser
        pygame.draw.circle(surface, colorWHITE, (curr_x, curr_y), thicknesses[0] // 2)
        pygame.draw.line(surface, colorWHITE, (prev_x, prev_y), (curr_x, curr_y), thicknesses[0])
    elif figure_index == 1:  # Brush
        pygame.draw.circle(surface, curr_color, (curr_x, curr_y), thicknesses[1] // 2)
        pygame.draw.line(surface, curr_color, (prev_x, prev_y), (curr_x, curr_y), thicknesses[1])
    elif figure_index == 2:  # Line
        pygame.draw.circle(surface, curr_color, (prev_x, prev_y), thicknesses[2] // 2)
        pygame.draw.circle(surface, curr_color, (curr_x, curr_y), thicknesses[2] // 2)
        pygame.draw.line(surface, curr_color, (prev_x, prev_y), (curr_x, curr_y), thicknesses[2])
    elif figure_index == 3:  # Rectangle
        pygame.draw.rect(surface, curr_color, calculate_rect(prev_x, prev_y, curr_x, curr_y), thicknesses[3])
    elif figure_index == 4:
        radius = int(((curr_x - prev_x)**2 + (curr_y - prev_y)**2)**0.5)
        pygame.draw.circle(surface, curr_color, (prev_x, prev_y), radius, thicknesses[4])
    elif figure_index == 5:
        points = calculate_diamond_points(prev_x, prev_y, curr_x, curr_y)
        pygame.draw.polygon(surface, curr_color, points, thicknesses[5])
        pygame.draw.circle(surface, curr_color, points[1], thicknesses[5] // 2)
        pygame.draw.circle(surface, curr_color, points[0], thicknesses[5] // 2)
        pygame.draw.circle(surface, curr_color, points[2], thicknesses[5] // 2)
        pygame.draw.circle(surface, curr_color, points[3], thicknesses[5] // 2)
    elif figure_index == 6:
        points = calculate_right_triangle_points(prev_x, prev_y, curr_x, curr_y)
        pygame.draw.polygon(surface, curr_color, points, thicknesses[6])
        pygame.draw.circle(surface, curr_color, points[0], thicknesses[6] // 2)
        pygame.draw.circle(surface, curr_color, points[1], thicknesses[6] // 2)
        pygame.draw.circle(surface, curr_color, points[2], thicknesses[6] // 2)

    elif figure_index == 7:
        points = calculate_equilateral_triangle_points(prev_x, prev_y, curr_x, curr_y)
        pygame.draw.polygon(surface, curr_color, points, thicknesses[7])
        pygame.draw.circle(surface, curr_color, points[0], thicknesses[7] // 2)
        pygame.draw.circle(surface, curr_color, points[1], thicknesses[7] // 2)
        pygame.draw.circle(surface, curr_color, points[2], thicknesses[7] // 2)

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
    screen.blit(thickness_text, (WIDTH // 2-10, 30))

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
            elif mod in [2, 3, 4, 5, 6, 7]:  # Line and Rectangle are temporarily drawn on the screen
                curr_x, curr_y = event.pos

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            draw_figure(mod, base_layer)  # Fix the drawing on the canvas

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_e: mod = 0  # Eraser
            if event.key == pygame.K_b: mod = 1  # Brush
            if event.key == pygame.K_l: mod = 2  # Line
            if event.key == pygame.K_r: mod = 3  # Rectangle
            if event.key == pygame.K_c: mod = 4  # Circle
            if event.key == pygame.K_d: mod = 5  # Diamond
            if event.key == pygame.K_t: mod = 6  # Right triangle
            if event.key == pygame.K_y: mod = 7  # Equilateral triangle

            if event.key == pygame.K_1: curr_color = colors[0] # Black
            if event.key == pygame.K_2: curr_color = colors[1] # Red
            if event.key == pygame.K_3: curr_color = colors[2] # Green
            if event.key == pygame.K_4: curr_color = colors[3] # Blue
            if event.key == pygame.K_5: curr_color = colors[4] # White
            if event.key == pygame.K_6: curr_color = colors[5] # Yellow
            if event.key == pygame.K_7: curr_color = colors[6] # Purple
            if event.key == pygame.K_8: curr_color = colors[7] # Orange
            if event.key == pygame.K_9: curr_color = colors[8] # Pink

            if event.key == pygame.K_z:  # Clear screen with 'C' key
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
    
    if LMBpressed and mod in [2, 3, 4, 5, 6, 7]:
        draw_figure(mod, screen)

    draw_toolbar()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
