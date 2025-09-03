import pgzrun
from pygame import Rect
from mecanica import config

# Configurações da janela
WIDTH = 800
HEIGHT = 600
COLOR_BACKGROUND = (WIDTH // 2, HEIGHT // 2)
# Definição dos botões
buttons = [
    {"text": "Jogar", "x": 300, "y": 100, "width": 50, "height": 25, "action": "play"},
    {"text": "Ligado", "x": 225, "y": 150, "width": 50, "height": 25, "action": "options"},
    {"text": "Desligado", "x": 375, "y": 150, "width": 50, "height": 25, "action": "options"},
    {"text": "Ligado", "x": 225, "y": 200, "width": 50, "height": 25, "action": "options"},
    {"text": "Desligado", "x": 375, "y": 200, "width": 50, "height": 25, "action": "options"},
    {"text": "Sair", "x": 300, "y": 250, "width": 50, "height": 25, "action": "quit"},
]

def draw(screen):
    screen.clear()
    screen.fill(config.COLOR_BACKGROUND)
    for button in buttons:
        # Botão
        screen.draw.filled_rect(
            Rect((button["x"], button["y"]), (button["width"], button["height"])),
            config.COLOR_BUTTON
        )
        # Texto
        screen.draw.text(
            button["text"],
            center=(button["x"] + button["width"] // 2, button["y"] + button["height"] // 2),
            color=config.COLOR_TEXT,
            fontsize=14,
        )
        screen.draw.text("Música", (315, 150), fontsize=14)
        screen.draw.text("Sons", (315, 200), fontsize=14)

def on_mouse_down(pos):
    for button in buttons:
        if (
            button["x"] <= pos[0] <= button["x"] + button["width"]
            and button["y"] <= pos[1] <= button["y"] + button["height"]
        ):
            return button["action"]
    return None