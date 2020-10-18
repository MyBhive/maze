import pygame

pygame.init()

window_resolution = (500, 500)
black_color = (0, 0, 0)
blue_color = (90, 124, 250)

pygame.display.set_caption("Maze : McGyver")
screen = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
strike = pygame.image.load("ressource/Gardien.png")
bg = pygame.image.load("ressource/structures.png")
x = 0
y = 0
width = 34
height = 36
velocity = 5
up = False
down = False
left = False
right = False
walkcount = 0
clock = pygame.time.Clock()

def game_window():
    global walkcount

    screen.blit(bg, [0, 0])
    if walkcount + 1 >= 27:
        walkcount = 0
    if up or down or left or right:
        screen.blit(strike, [x, y])
        walkcount += 1
    else:
        walkcount = 0

    pygame.display.update()

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        if keys[pygame.K_DOWN] and y < 480 - width - velocity:
            y += velocity
        if keys[pygame.K_LEFT] and x > velocity:
            x -= velocity
            left = True
            right = False
        if keys[pygame.K_RIGHT] and x < 640 - width - velocity:
            x += velocity
            left = False
            right = True

    game_window()


