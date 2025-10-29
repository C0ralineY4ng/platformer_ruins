'''# Cores do menu clicável 
COLOR_BACKGROUND = "black"
COLOR_BUTTON = "blue"
COLOR_TEXT = "white"'''

# mecanica/config.py

# Dimensões da tela
WIDTH = 800
HEIGHT = 600

# Plano de fundo / sky
BACKGROUND_IMAGE = "ruins.jpg"
SKY = "sky.png"  

# Cor alternativa (fallback)
BACKGROUND_COLOR = (209, 213, 216)

# Cores do menu
COLOR_BACKGROUND = (0, 0, 0)   # preto
COLOR_BUTTON = (0, 0, 255)     # azul
COLOR_TEXT = (255, 255, 255)   # branco

# Tiles e chão
GROUND_TILE = "ground.png"
PLATFORM_TILE = "platform.png"

# Arquivos do player
PLAYER_IDLE = "idle.png"
PLAYER_RUN = ["run1.png", "run2.png", "run3.png"]
PLAYER_JUMP = "jump.png"
PLAYER_LOW = "lowered.png"  

# Arquivos dos inimigos
GHOST = {
    "idle": ["ghost_normal.png"],
    "dead": ["ghost_dead.png"]
}

BAT = {
    "idle": ["bat.png"],
    "fly": ["bat2.png"],
}

ENEMIES = {
    "ghost": GHOST,
    "bat": BAT
}
