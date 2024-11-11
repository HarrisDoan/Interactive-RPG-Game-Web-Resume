import pygame
from sprites import *
from config import *
import sys

# Class that contains our Game object
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font('Arial', 32)
        self.running = True
    
    def createTilemap(self):
        for i, row, in enumerate(tilemap):
            for j, col in enumerate(row):
                if col == 'B':
                    # j = y position, i = x position
                    Block(self, j, i)
                    # j = x position, i = y position
                if col == 'P':
                    Player(self, j, i)
    
    def new(self):
        # Starting a new game
        self.playing = True

        # Store's all our sprite groups
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()
        
    
    # Game Loop: Events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    # Game Loop: Updates
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    # Game Loop: Main
    def main(self):
        # While we are playing the game
        while self.playing: 
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def game_over(self):
        pass
    
    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()