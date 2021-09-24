import arcade

class Ground(arcade.Sprite):
    def __init__(self , x, y):
        super().__init__()

        self.texture = arcade.load_texture("img/15.png")

        self.center_x = x
        self.center_y = y