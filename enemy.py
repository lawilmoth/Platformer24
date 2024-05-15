from player import Player
import math

class Enemy(Player):
    def __init__(self,game, x, y):
        super().__init__(game)

        self.x = x
        self.y = y
        self.color = "Red"
        self.rect.topleft = (x, y)
        self.moving_left = True
        self.speed = 2
        
    def follow(self, game):
        if math.fabs(self.rect.x - game.player.rect.x) < 400:
            if game.player.rect.x > self.rect.x:
                self.moving_left = False
                self.moving_right = True
            if game.player.rect.x < self.rect.x:
                self.moving_left = True
                self.moving_right = False
        else:
            self.moving_left = self.moving_right = False

    def update(self, map, game):
        self.follow(game)
        if self.falling:
            self.rect.y += self.y_acceleration

            self.y_acceleration += 1
        self._check_collisions(map)
    