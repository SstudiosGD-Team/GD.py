import pyglet
from game.menu import Menu

window = pyglet.window.Window(800, 600, caption='Geometry Dash Clone')
menu = Menu()

@window.event
def on_draw():
    window.clear()
    menu.draw()

@window.event
def on_key_press(symbol, modifiers):
    menu.on_key_press(symbol, modifiers)

pyglet.app.run()
