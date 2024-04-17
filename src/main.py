import pyglet
from game.menu import Menu

platform = pyglet.canvas.get_display().get_default_screen()
screen_width = platform.width
screen_height = platform.height

window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)

min_window_width = 1280
min_window_height = 720

if window_width < min_window_width:
    window_width = min_window_width
if window_height < min_window_height:
    window_height = min_window_height

window = pyglet.window.Window(width=window_width, height=window_height, resizable=True, caption='Geometry Dash Clone')
menu = Menu()

@window.event
def on_draw():
    window.clear()
    menu.draw()

@window.event
def on_key_press(symbol, modifiers):
    menu.on_key_press(symbol, modifiers)

pyglet.app.run()
