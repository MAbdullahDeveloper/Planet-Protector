import pygame

from config import LEVEL1, LEVEL2, LEVEL3, LEVEL4, BLACK, GREEN, MENU, font, hoverFont
from ui.back_button import BackButton


# Creating the levels page
class Gameplay:
    def __init__(self):
        self.buttons = [
            {"text": "1", "action": LEVEL1, "rect": None, "hovered": False},
            {"text": "2", "action": LEVEL2, "rect": None, "hovered": False},
            {"text": "3", "action": LEVEL3, "rect": None, "hovered": False},
            {"text": "4", "action": LEVEL4, "rect": None, "hovered": False},
        ]
        self.background = pygame.image.load("assets/images/background.png").convert()
        self.back_button = BackButton(10, 10)


    def draw(self, screen):
        # Draw the background
        screen.blit(self.background, (0, 0))
        title = font.render("Levels page", True, BLACK)
        title_rect = title.get_rect(center=(500, 50))
        screen.blit(title, title_rect)
        self.back_button.draw(screen)



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
                    center=(150 + i * 150, 200))  # Slightly enlarge by adjusting position
            else:
                button_surface = font.render(button["text"], True, BLACK)  # Black text
                button_rect = button_surface.get_rect(center=(150 + i * 150, 200))  # Normal position
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
                if self.back_button.is_clicked(event):
                    return MENU
                if button["rect"] and button["rect"].collidepoint(mouse_pos):
                    return button["action"]  # Return the action for the clicked button
        return None

