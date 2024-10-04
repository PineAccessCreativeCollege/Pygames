import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("My Simple Game")

clock = pygame.time.Clock()

BACKGROUND_COLOR = (255, 255, 255)

#screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0.05
camera_offset_x = 0
camera_offset_y = 0

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

player_x = 0
player_y = 0

#screenWidth = pygame.Vector2(screen.get_width)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2 + camera_offset_x)
#camera_offset_x = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == pygame.KEYDOWN:
            print("keydowns")
            if events.key == pygame.K_LEFT:
                camera_offset_x -= dt
                print("coff -=")
            if events.key == pygame.K_RIGHT:
                print("coff +=")
                camera_offset_x += dt

    screen.fill("white")

    pygame.draw.circle(screen, "red", player_pos, 10)
    
    
    #player_circle = player_circle.move(camera_offset_x, 0)
    #pygame.draw.circle(screen, "red", player_pos, 40)
    #player_circle_pos = pygame.draw.circle(screen, "red", camera_offset_x, 0) 
    #player_circle_pos = C1.move(camera_offset_x, 0)
    #pygame.draw.rect(screen, "red", player_pos, player_circle_pos)
    
    

    keys = pygame.key.get_pressed()  
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    camera_offset_x = screen.get_width() // 2 - player_x - 10 // 2
    camera_offset_y = screen.get_width() // 2 - player_y - 10 // 2

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()