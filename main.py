import pygame
from settings import Settings
from map import Map

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1500,1000))
        pygame.display.set_caption("Platformer")
        self.map = Map()
        self._load_level()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #Draw Screen
            self.screen.fill(self.settings.bg_color)
            self.map.draw()
            pygame.display.flip()

    def _load_level(self):
        self.map.load_level(1, self)

game = Game()
game.run()