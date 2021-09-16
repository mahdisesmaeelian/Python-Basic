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
        for i in self.snakebody_list:
            arcade.draw_circle_filled(i[0],i[1],self.r,self.color)
           
    def move(self):
        for i in range(len(self.snakebody_list)-1, 0, -1):
                self.snakebody_list[i][0] = self.snakebody_list[i-1][0]
                self.snakebody_list[i][1] = self.snakebody_list[i-1][1]
                
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        
        if self.snakebody_list:
            self.snakebody_list[0][0] += self.speed * self.change_x
            self.snakebody_list[0][1] += self.speed * self.change_y

    def eat(self):
        self.snakebody_list.append([self.center_x,self.center_y])
        self.score += 1   
        
# class Apple(arcade.Sprite):
#     def __init__(self, w, h):
#         arcade.Sprite.__init__(self)
#         self.color = arcade.color.RED
#         self.width = 16
#         self.height = 16
#         self.center_x = random.randint(0, w)
#         self.center_y = random.randint(0, h)
#         self.r = 8

#     def draw(self):
#         arcade.draw_circle_filled(
#             self.center_x, self.center_y, self.r, self.color)

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("img/apple.png")
        self.width = 25
        self.height = 30
        self.center_x = random.randint(0, w)
        self.center_y = random.randint(0, h)


class Pear(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("img/pear.png")
        self.width = 35
        self.height = 35
        self.center_x = random.randint(0, w)
        self.center_y = random.randint(0, h)  

class Poop(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__("img/poop.png")
        self.width = 35
        self.height = 35
        self.center_x = random.randint(0, w)
        self.center_y = random.randint(0, h) 


class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 700, 550, "snake game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(700, 550)
        self.apple = Apple(700, 550)
        self.pear = Pear(700,550)
        self.poop = Poop(700,550)

    def on_draw(self):
        arcade.start_render()

        if self.snake.score > -1 :
            self.apple.draw()
            self.snake.draw()
            self.pear.draw()
            self.poop.draw()
            arcade.draw_text(f"Score: {self.snake.score}",570,20,arcade.color.WHITE,25)
        else:
            arcade.draw_text('Game Over', 160, 250, arcade.color.BLACK, width=400,font_size = 45, align='center')     
         

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

        if arcade.check_for_collision(self.snake,self.pear):
            self.pear = Pear(700, 550)    
            self.snake.score+=2

        if arcade.check_for_collision(self.snake,self.poop):
            self.poop = Poop(700, 550)    
            self.snake.score-=1    

        if (self.snake.center_x < 0) or (self.snake.center_x > 700) or (self.snake.center_y < 0) or (self.snake.center_y > 550) : 
            self.snake.score = -1   

game = Game()
arcade.run()