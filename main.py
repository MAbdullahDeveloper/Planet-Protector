# Initialize Pygame
import pygame
pygame.init()


#cbuttons
from src.ui.back_button import BackButton
back_button = BackButton(10, 10)

from src.ui.hint_button import HintBox, HintButton
hint_button = HintButton(800, 10, 150, 50, "Hint")
hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

from src.ui.input_box import InputBox
input_box = InputBox(370, 400, 200, 40)

from src.screens.main_menu import MainMenu
from src.screens.settings import Settings
from src.screens.levels_page import Gameplay

from src.levels.level_1 import level1
from src.levels.level_2 import level2
from src.levels.level_3 import level3
from src.levels.level_4 import level4

from config import MENU, PLAY, SETTINGS, LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5, screen

# game audio
# pygame.mixer.music.load("assets/audio/Lobby-Time(chosic.com).mp3")




# Create a MainMenu object
main_menu = MainMenu()
# Create a Gameplay object
gameplay = Gameplay()
# Creating a Settings object
settings = Settings()
# Game state
game_state = MENU
# Main game loop
running = True

while running:

    for event in pygame.event.get():
        # pygame.mixer.music.play(-1)

        if event.type == pygame.QUIT:
            running = False

        # Handle input based on the current game state
        if game_state == MENU:
            action = main_menu.handle_input(event)
            if action == PLAY:
                game_state = PLAY
                print("Switching to PLAY state")
            elif action == SETTINGS:
                game_state = SETTINGS
                print("Switching to SETTINGS state")
            elif action == "quit":
                running = False

        elif game_state == PLAY:
            action = gameplay.handle_input(event)
            if action == MENU:
                game_state = MENU
            if action == LEVEL1:
                game_state = LEVEL1
                print("Switching to LEVEL1")
            elif action == LEVEL2:
                game_state = LEVEL2
                print("Switching to LEVEL2")
            elif action == LEVEL3:
                game_state = LEVEL3
                print("Switching to LEVEL3")
            elif action == LEVEL4:
                game_state = LEVEL4
                print("Switching to LEVEL4")
            elif action == LEVEL5:
                game_state = LEVEL5
                print("Switching to LEVEL5")
        elif game_state == SETTINGS:
            action = settings.handle_input(event)
            if action == MENU:
                game_state = MENU
        elif game_state == LEVEL1:
            action = level1().handle_input(event)
            if action == PLAY:
                game_state = PLAY

    # Draw the appropriate screen based on the game state
    if game_state == MENU:
        main_menu.draw(screen)
    elif game_state == PLAY:
        gameplay.draw(screen)
    elif game_state == SETTINGS:
        settings.draw(screen)
    elif game_state == LEVEL1:
        result = level1()
        if result == "quit":
            running = False
        elif result == "PLAY":
            game_state = PLAY
    elif game_state == LEVEL2:
        result = level2()
        if result == "quit":
            running = False
        elif result == "PLAY":
            game_state = PLAY
    elif game_state == LEVEL3:
        result = level3()
        if result == "quit":
            running = False
        elif result == "PLAY":
            game_state = PLAY
    elif game_state == LEVEL4:
        result = level4()
        if result == "quit":
            running = False
        elif result == "PLAY":
            game_state = PLAY
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()