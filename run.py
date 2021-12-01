# import files
from main import *
import os
# Create Game() Object
game = Game()
# then Initialize it
game.__init__()
# Show the init Screen
game.show_start_screen()
# Start New game as long as The Window Runs
while game.running:
    game.new()
# Quit The Game
p.quit()
