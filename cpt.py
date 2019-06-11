# Infinity Shoot

import arcade
import random
import os

# Still need to figure out how to get more than one enemy ball to spawn, how to shoot bullets, and record score, and collisions

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Infinity Shoot"
MOVEMENT_SPEED = 3
BULLET_SPEED = 2
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.player_list = None
        self.bullet_list = None

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):
    bullet = arcade.draw_lrtb_rectangle_filled(10, 10, 10, 10, arcade.color.YELLOW)



    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.AMAZON)
        self.current_state = INSTRUCTIONS_PAGE_0

        self.player_list = None
        self.coin_list = None
        self.score = 0
        self.player_sprite = None

        self.instructions = []
        texture = arcade.draw_text("Instructions/Move is left and right arrows < >/Shoot is [space]", 200, 440, arcade.color.BLACK)
        self.instructions.append(texture)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)


        arcade.set_background_color(arcade.color.WHITE)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.BLACK)
        enemy_posx = random.randrange(0, SCREEN_WIDTH)
        enemy_posy = random.randrange(380, 420)

        self.enemyball= Ball(enemy_posx, enemy_posy, 0, -1, 15, arcade.color.RED)


    def setup(self):
        self.player_list = arcade.SpriteList()

        self.score = 0

    def draw_instructions_page(self):
        page_texture = self.instructions
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.BLACK, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.BLACK, 24)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.enemyball.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.BLACK, 14)

    def update(self, delta_time):
        self.ball.update()
        self.enemyball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            pass
            # The image points to the right, and we want it to point up. So
            # rotate it.


            # Give the bullet a speed
            self.bullet.change_y = BULLET_SPEED

            # Position the bullet
            self.bullet.center_x = self.ball.center_x
            self.bullet.bottom = self.ball.top

            # Add the bullet to the appropriate lists
            self.bullet.update()


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0



def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
