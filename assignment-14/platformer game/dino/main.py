import random
import time
import arcade
from arcade.key import X

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 100
        self.center_y = 400
        self.change_x = 0.001

        self.texture = arcade.load_texture("img/20.png")
              

class Enemy(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.center_x = x
        self.center_y = y
        self.speed = 5
        self.change_x = -7

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
        self.score = 0
        self.w = 800
        self.h = 500
        super().__init__(self.w , self.h ,"My Game")
        arcade.set_background_color(arcade.color.WHITE)
        self.tcactus = time.time()
        self.tground = 1
        self.gravity = 0.4
        self.cactustime = 2
        self.jump_sound = (arcade.load_sound(":resources:sounds/rockHit2.wav"))

        self.player = Player()
        self.enemy_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list,self.gravity)

    def on_draw(self):
        arcade.start_render() 

        arcade.draw_text(f"{self.score}",650,450,arcade.color.BLACK,25)

        for enemy in self.enemy_list:
            enemy.draw()


        for ground in self.ground_list:
            ground.draw()

        self.player.draw()
        
    

    def on_update(self, delta_time: float):
        
        self.score += 1
        print(self.score)
        self.player.update_animation()
        self.player.update()
        self.physics_engine.update()
        
        for enemy in self.enemy_list:
            enemy.update()
            if enemy.center_x < 40:
                self.enemy_list.remove(enemy)

        for ground in self.ground_list:
            ground.update()
            if ground.center_x < -120:
                self.ground_list.remove(ground)

        self.t2 = time.time() 

        if self.t2 - self.tground > 2:
            self.ground_list.append(Ground(self.w , self.h//5))
            self.tground = time.time()

        if time.time() - self.tcactus > 1.9:
            self.enemy_list.append(Enemy(self.w, self.h//3.8))
            self.tcactus = time.time()
 
        # for c in self.enemy_list:
        #     if arcade.check_for_collision(self.player ,c):
        #         arcade.finish_render()
        #         arcade.exit()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                arcade.play_sound(self.jump_sound)
                self.player.change_y = 10

        if key == arcade.key.DOWN:
            self.player.texture = arcade.load_texture("img/17.png")
            self.player.width = 100
            self.player.height = 80
                   

    def on_key_release(self, key, modifiers):
        self.player.change_y = 0
        self.player.texture = arcade.load_texture("img/20.png")
        self.player.width = 80
        self.player.height = 100
        
                    

game = Game()
arcade.run()         