import pygame
from settings import Settings
from map import Map
from player import Player
import time 
class Game:
    def __init__(self):
        self.tries = 1
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1500,1000))
        self.enemies = pygame.sprite.Group()
        self.check_points = pygame.sprite.Group()
        pygame.display.set_caption("Platformer")
        self.map = Map(self)
        self.current_level = 1
        self._load_level()
        self.player = Player(self)
        self.running = True
        self.vertical_tracker = 0
        
        

        
    def run(self):
        while self.running:

            #Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.moving_right = True

                            
                            
                    if event.key == pygame.K_LEFT:
                        self.player.moving_left = True


                    if event.key == pygame.K_SPACE:
                        self.player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.player.moving_left = False

            #Update
            
            self.player.move(self.map)
            self.player.update(self.map)



            for enemy in self.enemies.sprites():
                enemy.update(self.map, self)
                enemy.move(self.map)
                
            self.scroll()
            


            #Draw Screen
            self.screen.fill(self.settings.bg_color)
            self.map.draw()
            self.player.draw()
            for enemy in self.enemies.sprites():
                enemy.draw()
            for cp in self.check_points.sprites():
                cp.draw()
            pygame.display.flip()
            self._check_dead()
            self._check_level_clear()
            self.clock.tick(60)

    def _load_level(self):
        self.map.load_level(self.current_level, self)

        



    def scroll(self):
        if (self.player.rect .x >= self.screen.get_rect().right - self.settings.scroll_offset)\
        and self.player.moving_right:
            self.player.rect.x -=self.settings.player_speed
            for object in self.map.map_objects:
                object.rect.x -= self.settings.player_speed
            for enemy in self.enemies:
                enemy.rect.x -=  self.settings.player_speed
            for cp in self.check_points:
                cp.rect.x -=  self.settings.player_speed

        if self.player.rect.top < self.screen.get_rect().top + self.settings.scroll_offset*2:
            self.vertical_tracker += self.player.y_acceleration
            if self.vertical_tracker < 0:
                
                self.vertical_tracker += self.player.y_acceleration
                self.player.rect.y -= self.player.y_acceleration
                for object in self.map.map_objects:
                    object.rect.y -= self.player.y_acceleration
                for enemy in self.enemies:
                    enemy.rect.y -= self.player.y_acceleration
                for cp in self.check_points:
                    cp.rect.y -= self.player.y_acceleration
            
    def _check_dead(self):
        collisions = pygame.sprite.spritecollideany(self.player, self.enemies)
        
        
        #if collisions and self.player.rect.bottom > collisio
        
        if self.player.rect.y > self.screen.get_rect().bottom + 100 or collisions:
            
            self.player.respawn(self)
            self.map.load_level(self.current_level, self)
            time.sleep(0.5)
            
    def _check_level_clear(self):
        if pygame.sprite.spritecollideany(self.player, self.check_points):
            self.current_level += 1
            self.player.respawn(self)
            self.map.load_level(self.current_level, self)


game = Game()
game.run()