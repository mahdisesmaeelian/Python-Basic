import random
import arcade

class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self,x,y):
            super().__init__()
            self.stand_left_textures = [arcade.load_texture("img/4.png")]
            
            self.walk_left_textures = [arcade.load_texture("img/4.png"),
                                        arcade.load_texture("img/5.png")]
            self.center_x = x
            self.center_y = random.randint(150,320)
            self.speed = 5
            self.change_x = -5