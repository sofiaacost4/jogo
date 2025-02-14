import pygame
import random

class MeninaSprite(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    menina_img  = pygame.image.load('menina.png').convert_alpha()
    menina_img = pygame.transform.scale(menina_img, (200,200))
    self.image = menina_img 
    self.rect = menina_img.get_rect()
    self.rect.topleft = (210,270)
    self.velocidade = 4
    self.direcao = 0 # 0 - direita | 1 - esquerda

  def p_esquerda(self):
    if self.direcao == 0:
      self.direcao = 1
      self.image = pygame.transform.flip(self.image, True, False)
    self.rect.x -= self.velocidade

  def p_direita(self):
    if self.direcao == 1:
      self.direcao = 0
      self.image = pygame.transform.flip(self.image, True, False)
    self.rect.x += self.velocidade

class MaçãPodre(pygame.sprite.Sprite):
  def __init__(self):
    for l in range(5):
      pygame.sprite.Sprite.__init__(self)
      maçãpodre_img = pygame.image.load('macapodre.png')
      maçãpodre_img = pygame.transform.scale(maçãpodre_img, (90,90))
      self.image = maçãpodre_img
      self.rect = self.image.get_rect()
      self.rect.topleft = (100, 70)
      self.velocidade = 8

class Maçã(pygame.sprite.Sprite):
  def __init__(self):
    for l in range(5):
      pygame.sprite.Sprite.__init__(self)
      maçã_img = pygame.image.load('maca.png')
      maçã_img = pygame.transform.scale(maçã_img, (90,90))
      self.image = maçã_img
      self.rect = self.image.get_rect()
      self.rect.topleft = (190, 70)
      self.velocidade = 3
      self.posicao = 0

  def maçã_cai(self):
    while self.posicao == 0: 
      self.posicao += self.velocidade
    self.rect.y += self.posicao
    if self.rect.y > 650:
      self.rect.y = 70

  def local(self):
    self.rect.y = 70
    x = [50, 100, 150, 200, 250, 300, 350, 400, 450]
    self.rect.x = random.choice(x)


num = 0

#game loop

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 24)

menina = MeninaSprite()
maçãpodre = MaçãPodre()
maçã = Maçã()
maçã.local()
all_sprites = pygame.sprite.Group([menina, maçãpodre, maçã])

fundo_img = pygame.image.load('fundo.png')

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  maçã.maçã_cai()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    menina.p_esquerda()
  if keys[pygame.K_RIGHT]:
    menina.p_direita()

  if menina.rect.colliderect(maçã.rect):
    num += 1
    maçã.local()

  screen.fill((255, 255, 255))

  screen.blit(fundo_img,(0,0))
  all_sprites.draw(screen)
  texto = font.render(f"Maçãs:{num}", True, 'white')
  screen.blit(texto, (400, 600))
  pygame.display.flip()
  clock.tick(60)

pygame.quit()
