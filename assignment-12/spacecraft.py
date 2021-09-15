import math
import random
import time
import arcade
from arcade.key import H
from arcade.window_commands import start_render


class Spacecraft(arcade.Sprite):
    def __init__(self,w):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.width = 48
        self.height = 48
        self.speed = 4
        self.center_x = w//2
        self.center_y = 35
        self.change_x = 0
        self.change_y = 0
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = []
        self.speed = 4
        self.score = 0
        

    def Rotate(self):
        self.angle += self.change_angle*self.speed  

    def move(self):
        self.center_x+=self.speed*self.change_x
        self.center_y+=self.speed*self.change_y    

    def fire(self):
        self.bullet_list.append(Bullet(self))       

class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.speed = 4
        self.center_x = random.randint(0,w)
        self.center_y = h
        self.angle = 180
        self.width = 48
        self.height = 48

    def move(self):
        self.center_y -= self.speed

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed = 4
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y

    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)    
        self.center_y += self.speed * math.cos(angle_rad)



class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        super().__init__(self.w, self.h, "SpaceCraft")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image =arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.spacecraft = Spacecraft(self.w)
        self.enemy_list= []
        self.start_time = time.time()
        self.randnum = random.randint(1,7)
        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")
        self.flag = 0
        self.heart = arcade.load_texture('img/heart.png')
        self.joon = 3
    
    def on_draw(self):
        arcade.start_render() 
        if self.joon > 0:
            arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,self.background_image)  
            self.spacecraft.draw()
            for i in range(len(self.spacecraft.bullet_list)):
                self.spacecraft.bullet_list[i].draw() 

            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()   

            arcade.draw_text(f"Score: {self.spacecraft.score}",670,15,arcade.color.WHITE,25)    

        if self.joon == 3:    
            for i in range(10,120,40):
                arcade.draw_lrwh_rectangle_textured(i , 10 , 50 , 50 , self.heart)
        elif self.joon == 2:    
            for i in range(40,120,40):
                arcade.draw_lrwh_rectangle_textured(i , 10 , 50 , 50 , self.heart) 
        elif self.joon == 1:    
            for i in range(80,120,40):
                arcade.draw_lrwh_rectangle_textured(i , 10 , 50 , 50 , self.heart)           

        else:
            arcade.draw_text('Game Over', self.w//4, self.h//2, arcade.color.WHITE, width=400,font_size = 45, align='center')   

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.spacecraft.change_angle = -1
        elif key == arcade.key.LEFT:
            self.spacecraft.change_angle = 1
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.gun_sound)
            self.spacecraft.fire()  
        elif key == arcade.key.D:
            self.spacecraft.change_x = 1   
        elif key == arcade.key.A:
            self.spacecraft.change_x = -1   
        elif key == arcade.key.W:
            self.spacecraft.change_y = 1
        elif key == arcade.key.S:
            self.spacecraft.change_y = -1            

    def on_key_release(self, key, modifiers):
        self.spacecraft.change_angle = 0
        self.spacecraft.change_x = 0
        self.spacecraft.change_y = 0
    
    def on_update(self, delta_time):

        self.end_time = time.time()    
        self.timeforspeed = time.time()

        if self.end_time - self.start_time > self.timeforspeed :
            for en in self.enemy_list:
                en.speed += 5
                print(en.speed)
            self.start_time = time.time()
               
        if self.end_time - self.start_time > self.randnum :
            self.enemy_list.append(Enemy(self.w,self.h))
            self.randnum = random.randint(1,7)
            self.start_time = time.time()

        self.spacecraft.Rotate() 
        self.spacecraft.move()

        for i in range(len(self.spacecraft.bullet_list)):
            self.spacecraft.bullet_list[i].move()                        

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()

        for en in self.enemy_list:
            for b in self.spacecraft.bullet_list:
                if arcade.check_for_collision(en,b):
                    arcade.play_sound(self.hit_sound)
                    self.enemy_list.remove(en)
                    self.spacecraft.bullet_list.remove(b)
                    self.spacecraft.score+=1

        for en in self.enemy_list:
            if en.center_y == 0:
                self.enemy_list.remove(en)
                self.joon -= 1

        for b in self.spacecraft.bullet_list:
            if (b.center_y > 600) or (b.center_x > 800) or (b.center_x < 0 ) :
                self.spacecraft.bullet_list.remove(b)       
               

game = Game()
arcade.run()        