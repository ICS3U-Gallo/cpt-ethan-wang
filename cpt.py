# Minute Collect

import arcade
import random
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Minute Collect"
MOVEMENT_SPEED = 5
ENEMYBALL_COUNT = 100

class Ball:
    def __init__(self, position_x, position_y, radius, color, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

class Enemyball:
    def __init__(self, center_x, center_y, radius, color, delta_x, delta_y):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.delta_x = delta_x
        self.delta_y = delta_y
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)
        
Enemyball.reset_pos()


def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

def update(self):
    global ball_x

    self.position_x += self.change_x
    self.position_y += self.change_y

    if self.position_x < self.radius:
        self.position_x = self.radius

    if self.position_x > SCREEN_WIDTH - self.radius:
        self.position_x = self.radius

    if self.position_y < self.radius:
        self.position_y = self.radius

    if self.position_y > SCREEN_HEIGHT - self.radius:
        self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super() .__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_list = None
        self.score = 0
        self.player_sprite = None
        self.set_mouse_visible(False)
        self.enemyball_list = arcade.SpriteList()

        arcade.set_background_color(arcade.color.WHITE)
        enemy_posx = random.randrange(0, SCREEN_WIDTH)
        enemy_posy = random.randrange(380, 420)

        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.BLACK)
        self.enemyball = Enemyball(enemy_posx, enemy_posy, 15, arcade.color.YELLOW)

        ENEMYBALL_COUNT = 100
        self.enemyball_list = arcade.SpriteList()

        for i in range(ENEMYBALL_COUNT):
            enemyballs = arcade.draw_circle_filled(enemy_posx, enemy_posy, 15, arcade.color.YELLOW)

    def setup(self):
        self.player_sprite_list = arcade.SpriteList()
        self.enemyball_sprite_list = arcade.SpriteList()

        self.score = 0

    def on_draw(self):
        arcade.start_render()

        self.ball.draw()
        self.enemyballs.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.BLACK, 14)

    def update(self, delta_time):

        Enemyball()

        if self.top < 0:
            self.reset_pos()

        self.ball.update()
        self.enemyball_sprite_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemyball_sprite_list)

        for enemyball in hit_list:
            enemyball.kill()
            self.score += 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED

        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED

        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or arcade.key.RIGHT:
            self.ball.change_x = 0

        elif key == arcade.key.UP or arcade.key.DOWN:
            self.ball.change_y()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
