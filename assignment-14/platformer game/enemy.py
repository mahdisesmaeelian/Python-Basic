import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(":resources:images/space_shooter/meteorGrey_med2.png")

        self.center_x = random.randint(0,700)
        self.center_y = 500
        self.speed = 5
        self.change_x = random.choice([-1,1])
        self.width=50
        self.height=50
