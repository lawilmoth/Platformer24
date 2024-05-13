import pygame
import pygame.sprite
from enemy import Enemy

class Object(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width=30, height=30):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(x,y, width, height)
        self.color = "Green"

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Map:
    def __init__(self, game):
        self.map_objects = pygame.sprite.Group()
        self.check_point_x = 0
        self.settings = game.settings

    def load_level(self, level, game, offset=0):
        self.map_objects.empty()
        if level == 1:

            floor2 = Object(game, 500, 600, 400, 10)
            block1 = Object(game, 900, 300, width= self.settings.player_width, height= 500)
            floor3 = Object(game, 1200, 600, 400, 10)
            self.map_objects.add(Object(game, 0, 700, 400, 10))
            self.map_objects.add(floor2)
            self.map_objects.add(block1)
            self.map_objects.add(floor3)
            self.map_objects.add(Object(game,2000, 50))
            self.map_objects.add(Object(game,1800, 300))
            self.map_objects.add(Object(game, 3000, 800, 500))

            enemy = Enemy(game, 200, 300)
            game.enemies.add(enemy)
            

            for object in self.map_objects.sprites():
                object.rect.x += offset
            
            


    def draw(self):
        for object in self.map_objects:
            object.draw()