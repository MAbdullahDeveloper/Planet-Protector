import pygame

from config import GREEN, BLACK, hoverFont, smallFont, MENU
from ui.back_button import BackButton

# Creating the settings
class Settings:
    def __init__(self):
        self.buttons = [
            {"text": "Game Volume", "action": "volume", "rect": None, "hovered": False},
            {"text": "ON", "action": "sound", "rect": None, "hovered": False},
            {"text": "OFF", "action": "sound", "rect": None, "hovered": False}
        ]
        self.background = pygame.image.load("assets/images/background.png").convert()
        self.back_button = BackButton(10, 10)

    def draw(self, screen):
        # Draw the background
        screen.blit(self.background, (0, 0))
        self.back_button.draw(screen)
        # Draw button
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
            if self.back_button.is_clicked(event):
                return MENU
            for button in self.buttons:
                if button["rect"] and button["rect"].collidepoint(mouse_pos):
                    return button["action"]  # Return the action for the clicked button
        return None