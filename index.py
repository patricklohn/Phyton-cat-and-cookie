import pygame
import random


pygame.init()

LARGURA, ALTURA = 700, 600
TAMANHO_CELULA = 100
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cat Labirinto")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

posicao_cat = (4, 2)
posicao_bolacha = (5, 6)

movimentos = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}

def desenha_grade():
    for linha in range(6):
        for coluna in range(7):
            rect = pygame.Rect(coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            pygame.draw.rect(TELA, PRETO, rect, 1)

def gera_obstaculos():
    obstaculos = []
    while len(obstaculos) < 10:
        obstaculo = (random.randint(0, 5), random.randint(0, 6))
        if obstaculo != posicao_cat and obstaculo != posicao_bolacha and obstaculo not in obstaculos:
            obstaculos.append(obstaculo)
    return obstaculos

# def desenha_cat_e_bolacha(cat_pos, bolacha_pos):
#     # Desenha o cat
#     cat_img = pygame.transform.scale(cat_img, (TAMANHO_CELULA, TAMANHO_CELULA))
#     cat_rect = pygame.Rect(cat_img, (cat_pos[1] * TAMANHO_CELULA, cat_pos[0] * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
#     pygame.draw.rect(TELA, AZUL, cat_rect)
    
#     # Desenha a bolacha
#     bolacha_rect = pygame.Rect(bolacha_pos[1] * TAMANHO_CELULA, bolacha_pos[0] * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
#     pygame.draw.rect(TELA, VERDE, bolacha_rect)

cat_img = pygame.image.load('img/cat.png')  
cat_img = pygame.transform.scale(cat_img, (TAMANHO_CELULA, TAMANHO_CELULA)) 

bolacha_img = pygame.image.load('img/cookie.png')  
bolacha_img = pygame.transform.scale(bolacha_img, (TAMANHO_CELULA, TAMANHO_CELULA))

def desenha_cat_e_bolacha(cat_pos, bolacha_pos):
    TELA.blit(cat_img, (cat_pos[1] * TAMANHO_CELULA, cat_pos[0] * TAMANHO_CELULA))
    
    TELA.blit(bolacha_img, (bolacha_pos[1] * TAMANHO_CELULA, bolacha_pos[0] * TAMANHO_CELULA))

#def desenha_obstaculos(obstaculos):
#    for obstaculo in obstaculos:
#        obstaculo_rect = pygame.Rect(obstaculo[1] * TAMANHO_CELULA, obstaculo[0] * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
#        pygame.draw.rect(TELA, VERMELHO, obstaculo_rect)
bomb_img = pygame.image.load('img/bomb.png')
bomb_img = pygame.transform.scale(bomb_img, (TAMANHO_CELULA, TAMANHO_CELULA))

def desenha_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        TELA.blit(bomb_img, (obstaculo[1] * TAMANHO_CELULA, obstaculo[0] * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

def move_cat(cat_pos, direcao, obstaculos):
    nova_pos = (cat_pos[0] + movimentos[direcao][1], cat_pos[1] + movimentos[direcao][0])
    if 0 <= nova_pos[0] < 6 and 0 <= nova_pos[1] < 7 and nova_pos not in obstaculos:
        return nova_pos
    return cat_pos

def main():
    cat_pos = posicao_cat
    bolacha_pos = posicao_bolacha
    obstaculos = gera_obstaculos()
    
    rodando = True
    while rodando:
        TELA.fill(BRANCO)
        desenha_grade()
        desenha_cat_e_bolacha(cat_pos, bolacha_pos)
        desenha_obstaculos(obstaculos)
        
        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cat_pos = move_cat(cat_pos, 'UP', obstaculos)
                elif event.key == pygame.K_DOWN:
                    cat_pos = move_cat(cat_pos, 'DOWN', obstaculos)
                elif event.key == pygame.K_LEFT:
                    cat_pos = move_cat(cat_pos, 'LEFT', obstaculos)
                elif event.key == pygame.K_RIGHT:
                    cat_pos = move_cat(cat_pos, 'RIGHT', obstaculos)

        if cat_pos == bolacha_pos:
            print("Você venceu!")
            rodando = False
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
