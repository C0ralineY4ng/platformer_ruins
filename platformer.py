import pgzrun 
from pgzero.actor import Actor
from mecanica import config
from mecanica import menu
from pygame import Rect
import random

# Declara as configurações globais do projeto
WIDTH = config.WIDTH
HEIGHT = config.HEIGHT

# Plano de fundo
background = Actor(config.BACKGROUND_IMAGE, (WIDTH // 2, HEIGHT // 2))


# Céu
sky = Actor(config.SKY, (WIDTH // 2, HEIGHT // 2))
bg_speed = 2
bg1_x = 0
bg2_x = WIDTH

# Chão
ground_tiles = []
TILE_SIZE = 64
for x in range(0, WIDTH, TILE_SIZE):
    ground_tiles.append(Actor(config.GROUND_TILE, (x + TILE_SIZE // 2, HEIGHT - TILE_SIZE)))

offset = 0

# Player
player = Actor(config.PLAYER_IDLE, (100, HEIGHT - 100))
player.vx = 0
player.vy = 0

PLAYER_SPEED = 5
PLAYER_ROLL_X = WIDTH // 2
GRAVITY = 0.5
JUMP_STRENGTH = -10

offset_x = 0
score = 0

# Estado do jogo
estado = "menu"


# INICIALIZAÇÃO DO JOGO

def init_game():
    global enemies, player, offset_x, score
    enemies = []
    offset_x = 0
    score = 0
    player.x = 100
    player.y = HEIGHT - TILE_SIZE
    player.vx = 0
    player.vy = 0

    # Cria 3 ghosts como exemplo
    for i in range(3):
        ghost = Actor(config.GHOST["idle"][0])
        ghost.y = HEIGHT - TILE_SIZE - 50
        ghost.x = i * 200 + 400
        ghost.angle = 90
        ghost.move_count = 0
        ghost.type = "ghost"
        ghost.vx = 2
        ghost.min_x = ghost.x - 50
        ghost.max_x = ghost.x + 50

        enemies.append(ghost)

    # Exemplo de bat
    bat = Actor(config.BAT["idle"][0])
    bat.y = HEIGHT - TILE_SIZE - 150
    bat.x = 650
    bat.move_count = 0
    bat.type = "bat"
    bat.vx = 2
    bat.vy = 1
    bat.min_x = bat.x - 80
    bat.max_x = bat.x + 80
    bat.min_y = bat.y - 50
    bat.max_y = bat.y + 50
    enemies.append(bat)

def init_enemies():
    """Inicializa os inimigos com limites de movimento e atributos extras"""
    enemies = []

    # Ghosts
    for i in range(3):
        ghost = Actor(config.GHOST["idle"], (100 + i * 200, HEIGHT - TILE_SIZE))
        ghost.type = "ghost"
        ghost.min_x = ghost.x - 50
        ghost.max_x = ghost.x + 50
        ghost.vx = 2
        ghost.move_count = 0
        enemies.append(ghost)

    # Bats
    for i in range(2):
        bat = Actor(config.BAT["fly"][0], (300 + i * 300, HEIGHT - 200))
        bat.type = "bat"
        bat.min_x = bat.x - 80
        bat.max_x = bat.x + 80
        bat.min_y = bat.y - 50
        bat.max_y = bat.y + 50
        bat.vx = 2
        bat.vy = 1
        enemies.append(bat)

    return init_enemies()

def update_enemies():
    """Atualiza a posição dos inimigos com movimento limitado"""
    for enemy in enemies:

        # Movimento aleatório apenas para variar start ou direção
        if enemy.move_count > 0:
            enemy.move_count -= 1
        else:
            choice = random.randint(0, 2)
            if choice == 0:
                enemy.move_count = 20
            elif choice == 1:
                # Troca direção horizontal
                enemy.vx *= -1
            elif choice == 2 and getattr(enemy, "vy", None) is not None:
                # Troca direção vertical se for bat
                enemy.vy *= -1

        # Movimento horizontal limitado
        enemy.x += enemy.vx
        if enemy.x < enemy.min_x or enemy.x > enemy.max_x:
            enemy.vx *= -1
            enemy.x = max(min(enemy.x, enemy.max_x), enemy.min_x)

        # Movimento vertical limitado (somente para bats)
        if enemy.type == "bat":
            enemy.y += enemy.vy
            if enemy.y < enemy.min_y or enemy.y > enemy.max_y:
                enemy.vy *= -1
                enemy.y = max(min(enemy.y, enemy.max_y), enemy.min_y)


# UPDATE
def update():
    global offset_x, bg1_x, bg2_x, score

    if estado != "game":
        return

     # Movimento do player
    PLAYER_ROLL_X = int(WIDTH * 0.6)  # ponto onde começa a rolagem

    if player.vx != 0:
        if player.vx < 0 and offset_x == 0 and player.x <= 100:
            player.x = 100
        elif player.x < PLAYER_ROLL_X or (player.vx < 0 and offset_x == 0):
            player.x += player.vx
        else:
            offset_x += player.vx
            if player.vx > 0:
                bg1_x -= player.vx
                bg2_x -= player.vx
                for tile in ground_tiles:
                    tile.x -= player.vx
            elif player.vx < 0 and offset_x > 0:
                bg1_x -= player.vx
                bg2_x -= player.vx
                for tile in ground_tiles:
                    tile.x -= player.vx

    # Gravidade
    player.vy += GRAVITY
    player.y += player.vy

    # Verifica colisão com chão
    if player.y >= HEIGHT - TILE_SIZE:
        player.y = HEIGHT - TILE_SIZE
        player.vy = 0

    # Reposiciona fundo para rolagem infinita
    if bg1_x <= -WIDTH:
        bg1_x = WIDTH
    if bg2_x <= -WIDTH:
        bg2_x = WIDTH

    # Atualiza inimigos
    update_enemies()


# Desenha tudo na na janela

def draw():
    screen.clear()
    if estado == "menu":
        menu.draw(screen)
    elif estado == "game":
        # Fundo e céu
        background.draw()
        screen.blit("sky", (bg1_x, 0))
        screen.blit("sky", (bg2_x, 0))

        # Tiles do chão
        for i in range(WIDTH // TILE_SIZE + 2):
            screen.blit("ground", (i * TILE_SIZE + offset, HEIGHT - TILE_SIZE))

        # Player
        player.draw()

        # Inimigos
        for enemy in enemies:
            if enemy.type == "ghost":
                # Se futuramente tiver animação de morto, trocar aqui
                screen.blit(enemy.image, (enemy.x - enemy.width // 2, enemy.y - enemy.height // 2))
            elif enemy.type == "bat":
                # Se tiver animação de batendo asas, pode trocar enemy.image
                screen.blit(enemy.image, (enemy.x - enemy.width // 2, enemy.y - enemy.height // 2))

        # Score
        screen.draw.text(f"Score: {score}", (10, 10), color="yellow", fontsize=32)

# Inputs

def on_mouse_down(pos):
    global estado
    if estado == "menu":
        acao = menu.on_mouse_down(pos)
        if acao == "play":
            estado = "game"
            init_game()
        elif acao == "quit":
            quit()

def on_key_down(key):
    global estado
    # ESCAPE alterna entre menu e jogo
    if key == keys.ESCAPE:  # pyright: ignore[reportUndefinedVariable]
        if estado == "menu":
            estado = "game"
            init_game()
        elif estado == "game":
            estado = "menu"

    # Controles do player
    if estado == "game":
        if key == keys.RIGHT:
            player.vx = PLAYER_SPEED
        elif key == keys.LEFT:
            player.vx = -PLAYER_SPEED
        elif key == keys.SPACE:
            if player.y >= HEIGHT - TILE_SIZE:
                player.vy = JUMP_STRENGTH

def on_key_up(key):
    if key in [keys.RIGHT, keys.LEFT]:
        player.vx = 0

pgzrun.go()
