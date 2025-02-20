import pygame
import random

def menu_inicial(screen, fundo, texto, x, y):
    screen.blit(fundo, (0,0))
    screen.blit(texto, (x, y))
    pygame.display.flip()
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                esperando = False

class MeninaSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        menina_img = pygame.image.load('menina.png').convert_alpha()
        menina_img = pygame.transform.scale(menina_img, (200, 200))
        self.image = menina_img
        self.rect = menina_img.get_rect()
        self.rect.topleft = (210, 270)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocidade = 4
        self.direcao = 0

    def p_esquerda(self):
        if self.direcao == 0:
            self.direcao = 1
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x -= self.velocidade
        if self.rect.x < -56:
            self.rect.x = -56

    def p_direita(self):
        if self.direcao == 1:
            self.direcao = 0
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x += self.velocidade
        if self.rect.x > 497:
            self.rect.x = 497

class MacaSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        maca_img = pygame.image.load('maca.png')
        maca_img = pygame.transform.scale(maca_img, (90, 90))
        self.image = maca_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.choice([50, 150, 250, 350, 450, 550]), 70)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocidade = 2

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y >= 658:
            self.rect.y = 70

class MacaPodre(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        macapodre_img = pygame.image.load('macapodre.png')
        macapodre_img = pygame.transform.scale(macapodre_img, (90, 90))
        self.image = macapodre_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.choice([50, 150, 250, 350, 450, 550]), 70)
        self.velocidade = 3

    def update(self):
        self.rect.y += self.velocidade

def criar_macas(numero):
    macas = []
    for i in range(numero):
        macas.append(MacaSprite())
    return macas

def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)
    pygame.display.set_caption("Colheita")
    fundo_img = pygame.image.load('fundo.png')
    texto = font.render("Pressione ENTER para jogar!", True, 'white')
    x, y = 210, 12

    while True:
        menu_inicial(screen, fundo_img, texto, x, y)
        menina = MeninaSprite()
        macas = criar_macas(1)
        all_sprites = pygame.sprite.Group([menina] + macas)
        sprites_macas = pygame.sprite.Group(macas)
        sprites_macas_podres = pygame.sprite.Group()
        num = 0
        vidas = 3
        prox_maca_podre = 10
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                menina.p_esquerda()
            if keys[pygame.K_RIGHT]:
                menina.p_direita()
            pygame.mouse.set_visible(False)
            hit_list = pygame.sprite.spritecollide(menina, sprites_macas, True, pygame.sprite.collide_mask)
            hit_list_2 = pygame.sprite.spritecollide(menina, sprites_macas_podres, True, pygame.sprite.collide_mask)
            all_sprites.update()

            if num >= prox_maca_podre:
                prox_maca_podre += 10 if num < 50 else 5 if num <= 100 else 2 if num <= 150 else 1
                macapodre = MacaPodre()
                sprites_macas_podres.add(macapodre)
                all_sprites.add(macapodre)
            
            if hit_list:
                num += len(hit_list)
            if hit_list_2:
                vidas -= 1
                for maca in hit_list_2:
                    sprites_macas_podres.remove(maca)
                if vidas <= 0:
                    texto = font.render("Ah não, você perdeu! Pressione ENTER para tentar novamente.", True, 'white')
                    x, y = 80, 12
                    running = False

            if len(sprites_macas) < 2:
                macas = criar_macas(1)
                sprites_macas.add(macas)
                all_sprites.add(macas)

            screen.fill((255, 255, 255))
            screen.blit(fundo_img, (0, 0))
            all_sprites.draw(screen)
            texto_1 = font.render(f"Maçãs: {num}", True, 'white')
            screen.blit(texto_1, (20, 12))
            texto_2 = font.render(f"Vidas: {vidas}", True, 'white')
            screen.blit(texto_2, (560, 12))
            pygame.display.flip()
            clock.tick(60)

game_loop()
