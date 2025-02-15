import pygame
import random

def quant_maçãs(lista, numero,):
  if numero == 2: 
    all_sprites = pygame.sprite.Group([maçã_1, maçã_2, maçã_3, menina])
  elif numero == 15:
    all_sprites = pygame.sprite.Group([maçã_1, maçã_2, maçã_3, maçã_4, maçã_5, maçã_6, menina])
  elif numero == 30: 
    all_sprites = pygame.sprite.Group([lista, menina])

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
      self.velocidade = 4
      self.posicao = 0

class Maçã(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      maçã_img = pygame.image.load('maca.png')
      maçã_img = pygame.transform.scale(maçã_img, (90,90))
      self.image = maçã_img
      self.rect = self.image.get_rect()
      self.rect.topleft = (190, 70)
      self.velocidade = 3
      self.posicao = 0
      self.rect.topleft = (self.rect.x, self.rect.y)

  def local_x(self):
    self.rect.y = 70
    x = [50, 100, 150, 200, 250, 300, 350, 400, 450]
    self.rect.x = random.choice(x)

  def maçã_cai_y(self):
    while self.posicao == 0: 
      self.posicao += self.velocidade
    self.rect.y += self.posicao
    if self.rect.y == 658:
      self.rect.y = 70
      self.rect.x = sprites_maçãs.local_x()
    return self.rect.y


num = 0

#game loop

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 24)

#criação dos sprites
menina = MeninaSprite()
maçãpodre = MaçãPodre()
maçã_1 = Maçã()
maçã_2 = Maçã()
maçã_3 = Maçã()
maçã_4 = Maçã()
maçã_5 = Maçã()
maçã_6 = Maçã()
maçã_7 = Maçã()
maçã_8 = Maçã()
lista_maçãs = [maçã_2, maçã_3, maçã_4, maçã_5, maçã_6, maçã_7, maçã_8]
all_sprites = pygame.sprite.Group([menina, maçã_1])
sprites_maçãs = pygame.sprite.Group([maçã_1, lista_maçãs])

fundo_img = pygame.image.load('fundo.png')

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    menina.p_esquerda()
  if keys[pygame.K_RIGHT]:
    menina.p_direita()

  hit_list = pygame.sprite.spritecollide(menina, sprites_maçãs, True)
  all_sprites.remove(hit_list)
  sprites_maçãs.remove(hit_list)
  quant_maçãs(num, lista_maçãs)

  screen.fill((255, 255, 255))

  screen.blit(fundo_img,(0,0))
  all_sprites.draw(screen)
  texto = font.render(f"Maçãs: {num}", True, 'white')
  screen.blit(texto, (20, 12))
  pygame.display.flip()
  clock.tick(60)

pygame.quit()
