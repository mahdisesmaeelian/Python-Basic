import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 100
        self.center_y = 400
        self.change_x = 0.0001
        self.texture = arcade.load_texture("img/19.png")