import random
import time
import arcade
from arcade.key import X
from player import Player
from bird import Bird
from enemy import Enemy
from ground import Ground
  
class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 500
        super().__init__(self.w , self.h ,"My Game")
        self.score = 0
        self.high_score = self.score
        arcade.set_background_color(arcade.color.WHITE)
        self.tcactus = time.time()
        self.tground = 1
        self.birdtime = 5
        self.gravity = 0.4
        self.cactustime = 2
        self.jump_sound = (arcade.load_sound(":resources:sounds/rockHit2.wav"))
        self.die_sound = (arcade.load_sound("sprites_die.wav"))
        self.starttime = time.time()
        self.startdinotime = time.time()
        self.flag = 0
        self.flag1 = 0
        self.game_over = False

        self.player = Player()
        self.enemy_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list,self.gravity)

    def on_draw(self):

        arcade.start_render() 
        arcade.draw_text(f"High Score:{self.high_score}    Score: {self.score}",500,450,arcade.color.BLACK,15)
    
        if self.flag == 0:
            arcade.draw_text(f"High Score:{self.high_score}    Score: {self.score}",500,450,arcade.color.BLACK,15)
        if self.flag == 1:
            arcade.draw_text(f"High Score:{self.high_score}    Score: {self.score}",500,450,arcade.color.WHITE,15)

        if self.game_over == True:
            arcade.draw_text("Game Over",self.w//2,self.h//2,arcade.color.RED,40)
            arcade.draw_text("Press space key to restart the game",self.w//2.6,self.h//2.8,arcade.color.RED,20)

        for enemy in self.enemy_list:
            enemy.draw()

        for bird in self.bird_list:
            bird.draw()

        for ground in self.ground_list:
            ground.draw()

        self.player.draw()     

        
    def on_update(self, delta_time: float):   

        if self.game_over == False:
            self.score += 1
            self.player.update()
            self.physics_engine.update()
                       
            if self.score > 1000:
                for bird in self.bird_list:
                    bird.update()
                    bird.update_animation()
                    if bird.center_x < 40:
                        self.bird_list.remove(bird)
            
            for enemy in self.enemy_list:
                enemy.update()
                enemy.move()
                if enemy.center_x < 40:
                    self.enemy_list.remove(enemy)

            for ground in self.ground_list:
                ground.update()
                if ground.center_x < 510:
                    self.ground_list.remove(ground)

        self.dinowalk = time.time()
            
        if self.dinowalk - self.startdinotime > 0.2 and self.flag1 == 0:
            self.startdinotime = time.time()
            self.player.texture = arcade.load_texture("img/19.png")
            self.flag1 = 1

        if self.dinowalk - self.startdinotime > 0.2 and self.flag1 == 1:
            self.player.texture = arcade.load_texture("img/20.png")
            self.startdinotime = time.time()
            self.flag1 = 0 
            
            self.bgcolortime = time.time()
            
            if self.bgcolortime - self.starttime > 15 and self.flag == 0:
                self.starttime = time.time()
                arcade.set_background_color(arcade.color.BLACK)
                self.flag = 1

            if self.bgcolortime - self.starttime > 15 and self.flag == 1:
                arcade.set_background_color(arcade.color.WHITE)
                self.starttime = time.time()
                self.flag = 0           

            self.t2 = time.time() 
            
            if time.time() - self.birdtime > 15:
                self.bird_list.append(Bird(self.w, self.h//2.2))
                self.birdtime = time.time()

            if self.t2 - self.tground > 2:
                self.ground_list.append(Ground(self.w , self.h//5))
                self.tground = time.time()

            if time.time() - self.tcactus > 1.9:
                self.enemy_list.append(Enemy(self.w, self.h//3.8))
                self.tcactus = time.time()
    
            for bird in self.bird_list:
                if  arcade.check_for_collision(self.player ,bird) :
                    arcade.play_sound(self.die_sound)
                    self.game_over = True
                    self.tcactus = time.time()
                    self.new_score = self.score
                    if self.new_score >= self.high_score :
                        self.high_score = self.score
                    arcade.set_background_color(arcade.color.WHITE)
                    self.score = 0
                    self.birdtime = 5
                    self.tground = 1
                    self.gravity = 0.4
                    self.cactustime = 2
                    self.starttime = time.time()
                    self.flag = 0
                    self.flag1 = 0
                    self.player = Player()
                    self.enemy_list = arcade.SpriteList()
                    self.ground_list = arcade.SpriteList()
                    self.bird_list = arcade.SpriteList()
                    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list,self.gravity)
                                    
                    
            for cactus in self.enemy_list:
                if arcade.check_for_collision(self.player ,cactus):
                    arcade.play_sound(self.die_sound)
                    self.game_over = True
                    self.tcactus = time.time()
                    self.new_score = self.score
                    if self.new_score >= self.high_score :
                        self.high_score = self.score
                    arcade.set_background_color(arcade.color.WHITE)
                    self.score = 0
                    self.birdtime = 5
                    self.tground = 1
                    self.gravity = 0.4
                    self.cactustime = 2
                    self.starttime = time.time()
                    self.flag = 0
                    self.flag1 = 0
                    self.player = Player()
                    self.enemy_list = arcade.SpriteList()
                    self.ground_list = arcade.SpriteList()
                    self.bird_list = arcade.SpriteList()
                    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list,self.gravity)
                       
    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.texture = arcade.load_texture("img/19.png")
                arcade.play_sound(self.jump_sound)
                self.player.change_y = 10

        if key == arcade.key.DOWN:
            self.player.texture = arcade.load_texture("img/17.png")
            self.player.width = 100
            self.player.height = 80

        if key == arcade.key.SPACE:
            self.game_over = False        

    def on_key_release(self, key, modifiers):
        self.player.change_y = 0
        self.player.texture = arcade.load_texture("img/20.png")
        self.player.width = 80
        self.player.height = 100                          

game = Game()
arcade.run()         