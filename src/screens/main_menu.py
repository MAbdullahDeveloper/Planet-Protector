import pygame

from config import MENU, PLAY, SETTINGS
from assets.fonts.font import font, smallFont, hoverFont
from src.utils.colors import BLACK, GREEN


class MainMenu:
    def __init__(self):
        self.buttons = [
            {"text": "Play", "action": PLAY, "rect": None, "hovered": False},
            {"text": "Settings", "action": SETTINGS, "rect": None, "hovered": False},
            {"text": "Quit", "action": "quit", "rect": None, "hovered": False}
        ]
        self.background = pygame.image.load("assets/images/background.png").convert()

    def draw(self, screen):
        # Draw the background
        screen.blit(self.background, (0, 0))
        # Draw the title
        title = font.render("Planet Protectors", True, BLACK)
        title_rect = title.get_rect(center=(500, 50))
        screen.blit(title, title_rect)

        # Draw buttons
        for i, button in enumerate(self.buttons):
            # Check if the mouse is hovering over the button
            mouse_pos = pygame.mouse.get_pos()
            if button["rect"] and button["rect"].collidepoint(mouse_pos):
                button["hovered"] = True
            else:
                button["hovered"] = False
            # Change button size and color if hovered
            if button["hovered"]:
                button_surface = hoverFont.render(button["text"], True, GREEN)  # Green text
                button_rect = button_surface.get_rect(
                    center=(500, 200 + i * 100))  # Slightly enlarge by adjusting position
            else:
                button_surface = smallFont.render(button["text"], True, BLACK)  # Black text
                button_rect = button_surface.get_rect(center=(500, 200 + i * 100))  # Normal position

            # Draw the button
            screen.blit(button_surface, button_rect)
            # Store the rect for click detection
            button["rect"] = button_rect

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button["rect"] and button["rect"].collidepoint(mouse_pos):
                    return button["action"]  # Return the action for the clicked button
        return None