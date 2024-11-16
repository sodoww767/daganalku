import pygame

window = pygame.display.set_mode((700,500))
pygame.display.set_caption("Доганялки")

forest = pygame.transform.scale(pygame.image.load("forest.png"), (700,500))

sp_1 = pygame.transform.scale(pygame.image.load("1.png"), (260,180))
sp_2 = pygame.transform.scale(pygame.image.load("2.png"), (250,250))

running = True
clock = pygame.time.Clock()
fps = 60

sp1_x = 100
sp1_y = 100

sp2_x = 200
sp2_y = 200

speed = 10

while running:
    window.blit(forest,(0,0))
    window.blit(sp_1,(sp1_x , sp1_y))
    window.blit(sp_2,(sp2_x , sp2_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #1 спрайт
    if keys[pygame.K_w] and sp1_y > 5:
        sp1_y -= speed 
    if keys[pygame.K_s] and sp1_y < 495:
        sp1_y += speed
    if keys[pygame.K_a] and sp1_x > 5:
        sp1_x -= speed 
    if keys[pygame.K_d] and sp1_x < 695:
        sp1_x += speed

    #2 спрайт
    if keys[pygame.K_UP] and sp2_y > 5:
        sp2_y -= speed 
    if keys[pygame.K_DOWN] and sp2_y < 495:
        sp2_y += speed
    if keys[pygame.K_LEFT] and sp2_x > 5:
        sp2_x -= speed 
    if keys[pygame.K_RIGHT] and sp2_x < 695:
        sp2_x += speed


    pygame.display.update()
    clock.tick(fps)
pygame.quit()

