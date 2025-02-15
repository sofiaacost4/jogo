import pygame
import random

class MeninaSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        menina_img = pygame.image.load('menina.png').convert_alpha()
        menina_img = pygame.transform.scale(menina_img, (200, 200))
        self.image = menina_img
        self.rect = menina_img.get_rect()
        self.rect.topleft = (210, 270)
        self.velocidade = 4
        self.direcao = 0  # 0 - direita | 1 - esquerda

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

class MaçãSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        maçã_img = pygame.image.load('maca.png')
        maçã_img = pygame.transform.scale(maçã_img, (90, 90))
        self.image = maçã_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.choice([50, 150, 250, 350, 450, 550]), 70)
        self.velocidade = 2
        self.posicao = 0

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y >= 658:
            self.rect.y = 70

class MaçãPodre(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        maçãpodre_img = pygame.image.load('macapodre.png')
        maçãpodre_img = pygame.transform.scale(maçãpodre_img, (90, 90))
        self.image = maçãpodre_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.choice([50, 150, 250, 350, 450, 550]), 70)
        self.velocidade = 3
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y >= 658:
            self.rect.y = 70
        

#gera as maçãs
def criar_maçãs(numero):
    maçãs = []
    for i in range(numero):
        maçãs.append(MaçãSprite())
    return maçãs

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

#fonte
font = pygame.font.Font(None, 24)

#cria os sprites e grupos de sprites
menina = MeninaSprite()
maçãs = criar_maçãs(1)
all_sprites = pygame.sprite.Group([menina] + maçãs)
sprites_maçãs = pygame.sprite.Group(maçãs)
sprites_maçãs_podres = pygame.sprite.Group()
fundo_img = pygame.image.load('fundo.png')

#variaveis
num = 0
vidas = 3
x = 1
y = 2

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        menina.p_esquerda()
    if keys[pygame.K_RIGHT]:
        menina.p_direita()

    #verifica a colisão
    hit_list = pygame.sprite.spritecollide(menina, sprites_maçãs, True)
    hit_list_2 = pygame.sprite.spritecollide(menina, sprites_maçãs_podres, True)
  
    all_sprites.update()
    
    #adiciona a maçã podre no jogo quando o jogador coletar 10 maçãs
    if num >= 10 and len(sprites_maçãs_podres) == 0:
     maçãpodre = MaçãPodre()
     sprites_maçãs_podres.add(maçãpodre)
     all_sprites.add(maçãpodre)
    
    #verifica se o jogador colidiu com uma maçã podre
    if hit_list_2:
        vidas -= 1
        if vidas <= 0:
            running = False


    #adiciona novas maçãs quando o jogador coleta uma determinada quantidade de maçãs
    if len(sprites_maçãs) < y:
        maçãs = criar_maçãs(x)
        if num >= 25:
            x = 2
            y = 3
        if num >= 80:
            x = 3
            y = 4
        sprites_maçãs.add(maçãs)
        all_sprites.add(maçãs)
   
    if hit_list:
        num += len(hit_list)

    # Atualiza a tela
    screen.fill((255, 255, 255))
    screen.blit(fundo_img, (0, 0))
    all_sprites.draw(screen)

    # Exibe o texto de quantidade de maçãs
    texto = font.render(f"Maçãs: {num}", True, 'white')
    screen.blit(texto, (20, 12))
    texto = font.render(f"Vidas: {vidas}", True, 'white')
    screen.blit(texto, (560, 12))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
