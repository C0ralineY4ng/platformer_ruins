# mecanica/config.py

# Dimensões da tela
WIDTH = 800
HEIGHT = 600

# Arquivo da imagem de fundo
BACKGROUND_IMAGE = "ruins.jpg"
SKY = "sky"
# Cor alternativa (fallback, caso a imagem não seja encontrada)
BACKGROUND_COLOR = (209, 213, 216)


# Cores do menu clicável 
COLOR_BACKGROUND = "black"
COLOR_BUTTON = "blue"
COLOR_TEXT = "white"

# Tiles e chão
GROUND_TILE = "ground.png"
PLATFORM_TILE = "platform.png"

# Arquivo da imagem do player
PLAYER_IDLE = "idle.png"
PLAYER_RUN = ["run1.png,run2.png,run3.png"]
PLAYER_JUMP = "jump.png"
PLAYER_LOW = "lowrered.png"


# Arquivo da imagem dos enemies

GHOST = {
    "idle": ["ghost_normal.png"],  # lista para expandir animações
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