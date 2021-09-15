import random
import arcade


class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.GREEN
        self.speed = 2
        self.width = 16
        self.height = 16
        self.center_x = w//2
        self.center_y = h//2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.snakebody_list = []

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)
        self.snakebody_list.append([self.center_x,self.center_y])
        for i in self.snakebody_list:
            arcade.draw_circle_filled(i[0],i[1],self.r,self.color)
           
    def move(self):
        self.center_x+=self.speed*self.change_x
        self.center_y+=self.speed*self.change_y

    def eat(self):
        self.score += 1   
        

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.RED
        self.width = 16
        self.height = 16
        self.center_x = random.randint(0, w)
        self.center_y = random.randint(0, h)
        self.r = 8

    def draw(self):
        arcade.draw_circle_filled(
            self.center_x, self.center_y, self.r, self.color)


class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 700, 550, "snake game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(700, 550)
        self.apple = Apple(700, 550)

    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.snake.draw()
         

    def on_key_release(self, key, modifier):
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif key == arcade.key.DOWN:
            self.snake.change_y = -1
            self.snake.change_x = 0

    def on_update(self, delta_time: float):

        self.snake.move()

        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.eat()
            self.apple = Apple(700, 550)
            print(self.snake.score)   

game = Game()
arcade.run()