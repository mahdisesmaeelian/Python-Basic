import random
import time
import arcade
from arcade.key import X

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture("img/20.png")

        self.center_x = 100
        self.center_y = 140
        
        self.width = 70
        self.height = 85

class Enemy(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.center_x = x
        self.center_y = y
        self.speed = 5
        self.change_x = -4

        self.cactus = random.choice(['1','2','3','4'])

        if self.cactus == '1':
            self.texture = arcade.load_texture("img/6.png")
        if self.cactus == '2':
            self.texture = arcade.load_texture("img/7.png")
        if self.cactus == '3':
            self.texture = arcade.load_texture("img/8.png")
        if self.cactus == '4':
            self.texture = arcade.load_texture("img/9.png")


class Ground(arcade.Sprite):
    def __init__(self , x, y):
        super().__init__()

        self.texture = arcade.load_texture("img/15.png")

        self.center_x = x
        self.center_y = y

        self.change_x = -4
        self.change_y = 0   

class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 500
        super().__init__(self.w , self.h ,"My Game")
        arcade.set_background_color(arcade.color.WHITE)
        self.t1 = 2
        self.gravity = 0.5
        self.cactustime = 2

        self.player = Player()
        self.enemy_list = []
        self.ground_list = []
        self.my_physics_engine = []

    def on_draw(self):
        arcade.start_render() 

        for enemy in self.enemy_list:
            enemy.draw()

        for ground in self.ground_list:
            ground.draw()

        self.player.draw()
        
    

    def on_update(self, delta_time: float):
     
        self.player.update()
        
        for my in self.my_physics_engine:
            my.update()


        self.t2 = time.time() 
        if self.t2 - self.t1 > 2:
            new_ground = Ground(self.w , self.h//5)
            self.ground_list.append(new_ground)
            self.my_physics_engine.append(arcade.PhysicsEnginePlatformer(self.player,self.ground_list,gravity_constant= self.gravity))
            self.t1 = time.time()

        if time.time() - self.t1 > self.cactustime:
            self.enemy_list.append(Enemy(self.w, self.h//3.8))
            self.t1 = time.time()
 
        for enemy in self.enemy_list:
            enemy.update()
            if enemy.center_x < 40:
                self.enemy_list.remove(enemy)

        for ground in self.ground_list:
            ground.update()
            if ground.center_x < 1:
                self.ground_list.remove(ground)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.my_physics_engine.can_jump():
                self.player.change_y = 1

    def on_key_release(self, key, modifiers):
        self.player.change_y = 0
                    
     

game = Game()
arcade.run()         