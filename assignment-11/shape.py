import arcade

class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.GREEN
        self.width = 16
        self.height = 16
        self.center_x = w//2
        self.center_y = h//2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 700, 550, "snake game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(700, 550)
        

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()        

game = Game()
arcade.run()            