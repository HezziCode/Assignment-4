# My Hand written code .... Muhammad Huzaifa

# import pygame
# def eraseCanvas():


#     pygame.init()


# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Eraser Tool")


# rect = pygame.Rect(100, 100, 100, 100)
# rect_color = (255, 0, 0) 
# eraser = pygame.Rect(0, 0, 50, 50)  

# running = True


# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
#             running = False


#     screen.fill((255, 255, 255))


#     mouse_x, mouse_y = pygame.mouse.get_pos()


#     eraser.topleft = (mouse_x - eraser.width // 2, mouse_y - eraser.height // 2)

#     if eraser.colliderect(rect):
#         rect_color = (255, 255, 255) 

#     pygame.draw.rect(screen, rect_color, rect) 
#     pygame.draw.rect(screen, (0, 0, 255), eraser) 


#     pygame.display.update()

# pygame.quit()

# eraseCanvas()


# AI code 🙂

