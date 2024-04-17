import pyglet
from game.menu import Menu

# List of available resolutions
resolutions = [
    (2560, 1600),
    (2560, 1440),
    (2048, 1536),
    (1920, 1440),
    (1920, 1200),
    (1680, 1050),
    (1680, 1200),
    (1680, 1024),
    (1680, 900),
    (1366, 768),
    (1360, 768),
    (1280, 1024),
    (1280, 960),
    (1280, 800),
    (1280, 768),
    (1280, 720),
    (1152, 864),
    (1024, 768),
    (800, 600)
]

# Function to find the best available resolution
def find_best_resolution(screen_width, screen_height):
    best_resolution = (0, 0)
    best_diff = float('inf')
    for resolution in resolutions:
        diff = abs(screen_width - resolution[0]) + abs(screen_height - resolution[1])
        if diff < best_diff:
            best_diff = diff
            best_resolution = resolution
    return best_resolution

# Get the default screen and its dimensions
platform = pyglet.canvas.get_display().get_default_screen()
screen_width = platform.width
screen_height = platform.height

# Find the best available resolution
best_width, best_height = find_best_resolution(screen_width, screen_height)

# Create the window with the best found resolution
window = pyglet.window.Window(width=best_width, height=best_height, resizable=True, caption='Geometry Dash Clone')
menu = Menu()

@window.event
def on_draw():
    window.clear()
    menu.draw()

@window.event
def on_key_press(symbol, modifiers):
    menu.on_key_press(symbol, modifiers)

pyglet.app.run()
