import pygame
from config import BLACK, GREEN, answerFont

class InputBox:
    def __init__(self, x, y, width, height):
        self.text = ""
        self.rect = pygame.Rect(x, y, width, height)
        self.border_color = BLACK  # Border color of the input box
        self.text_color = BLACK  # Color of the text
        self.active = False
        self.txt_surface = answerFont.render(self.text, True, self.text_color)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if the input box is clicked
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change the border color if active
            self.border_color = GREEN if self.active else BLACK
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # Print the text to the console


                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]  # Remove the last character
                else:
                    self.text += event.unicode  # Add the new character
                # Re-render the text (always in black)
                self.txt_surface = answerFont.render(self.text, True, self.text_color)

    def draw(self, screen):
        # Draw the input box border
        pygame.draw.rect(screen, self.border_color, self.rect, 2)
        # Draw the text (always in black)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        """Returns the current text in the input box."""
        return self.text
