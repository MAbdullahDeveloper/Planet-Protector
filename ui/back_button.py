import pygame

class BackButton:

    def __init__(self, x, y):

        self.image = pygame.image.load("assets/images/backButton.png")

        self.image_hover = pygame.transform.scale(self.image, (
        int(self.image.get_width() * 1.5), int(self.image.get_height() * 1.5)))

        self.rect = self.image.get_rect(topleft=(x, y))

        self.hovered = False

    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):

            self.hovered = True

            enlarged_rect = self.image_hover.get_rect(center=self.rect.center)

            surface.blit(self.image_hover, enlarged_rect)

        else:

            self.hovered = False

            surface.blit(self.image, self.rect)

    def is_clicked(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True

        return False