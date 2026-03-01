import pygame
from config import BLACK, GREEN, GRAY, answerFont

class HintBox:
    def __init__(self, x, y, width, height, color, text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.border_color = BLACK
        self.border_width = 2
        self.text = text
        self.text_color = BLACK
        self.txt_surface = answerFont.render(self.text, True, self.text_color)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, self.border_color, self.rect, self.border_width)
        if self.text:
            text_rect = self.txt_surface.get_rect(center=self.rect.center)
            surface.blit(self.txt_surface, text_rect)

    def update_text(self, new_text):
        self.text = new_text
        self.txt_surface = answerFont.render(self.text, True, self.text_color)


class HintButton:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = GRAY
        self.hover_color = GREEN
        self.text_surface = answerFont.render(text, True, BLACK)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        return False