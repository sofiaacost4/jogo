import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

fundo_img = pygame.image.load('fundo.png')
menina_img = pygame.image.load('menina.png')
menina_img = pygame.transform.scale(menina_img, (200,200))

menina_rect = menina_img.get_rect()
menina_rect.topleft = (210,270)

velocidade = 4
sentido = 1

while running:
  # Processamento de eventos (entradas de teclado e mouse)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    if sentido == 1:
     sentido = -1
     menina_img = pygame.transform.flip(menina_img, True, False)
    menina_rect.x -= velocidade
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    if sentido == -1:
     sentido = 1
     menina_img = pygame.transform.flip(menina_img, True, False)
    menina_rect.x += velocidade
  screen.fill((255, 255, 255))
  screen.blit(fundo_img,(0,0))
  screen.blit(menina_img, menina_rect.topleft)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
