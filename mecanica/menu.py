# mecanica/menu.py
from pygame import Rect
from mecanica import config

# Botões (x,y são canto superior esquerdo)
buttons = [
    {"text": "Jogar", "x": 300, "y": 100, "width": 200, "height": 40, "action": "play"},
    {"text": "Música: On", "x": 300, "y": 160, "width": 200, "height": 40, "action": "toggle_music"},
    {"text": "Sons: On", "x": 300, "y": 220, "width": 200, "height": 40, "action": "toggle_sfx"},
    {"text": "Sair", "x": 300, "y": 280, "width": 200, "height": 40, "action": "quit"},
]

def draw(screen):
    screen.clear()
    screen.fill(config.COLOR_BACKGROUND)
    for button in buttons:
        rect = Rect((button["x"], button["y"]), (button["width"], button["height"]))
        screen.draw.filled_rect(rect, config.COLOR_BUTTON)
        screen.draw.text(
            button["text"],
            center=(button["x"] + button["width"] // 2, button["y"] + button["height"] // 2),
            color=config.COLOR_TEXT,
            fontsize=24,
        )

def on_mouse_down(pos):
    for button in buttons:
        bx, by, bw, bh = button["x"], button["y"], button["width"], button["height"]
        if bx <= pos[0] <= bx + bw and by <= pos[1] <= by + bh:
            return button["action"]
    return None
