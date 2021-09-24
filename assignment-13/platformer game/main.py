import time
import arcade
from player1 import Player
from enemy import Enemy
from ground import Ground

class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 500
        self.gravity = 0.3
        super().__init__(self.w , self.h ,"My Game")
        self.backeground_image = arcade.load_texture("img/background.png")

        self.t1 = time.time()
        self.player = Player()
        self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        
        self.key = arcade.Sprite(":resources:images/items/keyYellow.png")
        self.key.center_x=100
        self.key.center_y=450
        self.key.width = 50
        self.key.height=50 
        
        self.lock = arcade.Sprite(":resources:images/tiles/lockYellow.png")
        self.lock.center_x = 770
        self.lock.center_y = 90
        self.lock.width = 50
        self.lock.height=50 

        for i in range(0, 1000, 115):
            ground = Ground(i ,7)
            self.ground_list.append(ground)

        for i in range(90,330,115):
            ground = Ground(i ,240)   
            self.ground_list.append(ground) 

        for i in range(520,650,115):
            ground = Ground(i ,190)   
            self.ground_list.append(ground)     

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list,self.gravity)

        self.enemy_physics_engine_list = []

    def on_draw(self):
        arcade.start_render()    
        arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,self.backeground_image)

        try:
            self.key.draw()      
        except:
            pass    

        self.lock.draw()
 
        self.player.draw()
        for ground in self.ground_list:
            ground.draw()
        for enemy in self.enemy_list:
            enemy.draw()    

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -1 * self.player.speed
        elif key == arcade.key.RIGHT:
            self.player.change_x = 1 * self.player.speed
        elif key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 10

    def on_key_release(self, key, modifiers):
        self.player.change_x = 0           
            
    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.player.update_animation()
        for enemy in self.enemy_physics_engine_list:
            enemy.update()

        self.t2 = time.time()

        if self.t2 - self.t1 > 5 :
            new_enemy = Enemy()
            self.enemy_list.append(new_enemy)
            self.enemy_physics_engine_list.append(arcade.PhysicsEnginePlatformer(new_enemy,self.ground_list,self.gravity))
            self.t1 = time.time()
        try:
            if arcade.check_for_collision(self.player,self.key):
                self.player.pocket.append(self.key)   
                del self.key   
                print(len(self.player.pocket)) 
        except:
            pass  

        if arcade.check_for_collision(self.player,self.lock) and len(self.player.pocket)==1 :
            self.lock.texture = arcade.load_texture(":resources:images/items/star.png")            

game = Game()
arcade.run()        