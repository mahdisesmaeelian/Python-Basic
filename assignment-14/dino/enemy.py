import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.change_x = -7
        self.speed = 2

        self.cactus = random.choice(['1','2','3','4'])

        if self.cactus == '1':
            self.texture = arcade.load_texture("img/6.png")
        if self.cactus == '2':
            self.texture = arcade.load_texture("img/7.png")
        if self.cactus == '3':
            self.texture = arcade.load_texture("img/8.png")
        if self.cactus == '4':
            self.texture = arcade.load_texture("img/9.png")

    def move(self):
        self.center_x -=  self.speed