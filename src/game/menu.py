import os
import pyglet

class Menu:
    def __init__(self):
        # Construct absolute path to resources directory
        resource_dir = os.path.join(os.path.dirname(__file__), 'resources')
        
        # Load images
        self.background_img = pyglet.image.load(os.path.join(resource_dir, 'background.png'))
        self.play_button_img = pyglet.image.load(os.path.join(resource_dir, 'play_button.png'))
        self.settings_button_img = pyglet.image.load(os.path.join(resource_dir, 'settings_button.png'))
        
        # Create sprites
        self.background = pyglet.sprite.Sprite(self.background_img)
        self.play_button = pyglet.sprite.Sprite(self.play_button_img)
        self.settings_button = pyglet.sprite.Sprite(self.settings_button_img)
        
        # Set positions
        self.play_button.x = 400
        self.play_button.y = 300
        self.settings_button.x = 400
        self.settings_button.y = 200

    def draw(self):
        self.background.draw()
        self.play_button.draw()
        self.settings_button.draw()

    def on_key_press(self, symbol, modifiers):
        pass  # Implement key press handling if needed
