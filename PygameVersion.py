import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 3840, 2160  # 2180p approximation
FPS = 120
FONT_NAME = "comicsansms"
BG_COLOR = (255, 200, 255)
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (100, 200, 255)
BUTTON_HOVER = (150, 250, 255)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("This or That Game")
clock = pygame.time.Clock()

# Load font
font = pygame.font.SysFont(FONT_NAME, 80)
small_font = pygame.font.SysFont(FONT_NAME, 60)

# Fade effect
def fade_text(text, y, duration=1000):
    alpha = 0
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
    fade_clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    while alpha < 255:
        elapsed = pygame.time.get_ticks() - start_time
        alpha = min(255, int((elapsed / duration) * 255))
        screen.fill(BG_COLOR)
        temp_surface = text_surface.copy()
        temp_surface.set_alpha(alpha)
        screen.blit(temp_surface, text_rect)
        pygame.display.update()
        fade_clock.tick(FPS)

# Button class
class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.Rect(x, y, 600, 150)
        self.color = BUTTON_COLOR

    def draw(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BUTTON_HOVER, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        text_surface = small_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]

# Game questions
questions = [
    ("Would you rather have the ability to fly or be invisible?", "Fly", "Invisible"),
    ("Would you rather live in the mountains or by the beach?", "Mountains", "Beach"),
    ("Would you rather have a pet dragon or a pet unicorn?", "Dragon", "Unicorn"),
    ("Would you rather speak all languages or play all instruments?", "Languages", "Instruments"),
    ("Would you rather travel to the past or the future?", "Past", "Future"),
    ("Messi or Ronaldo?", "Messi", "Ronaldo")
]

# Main game loop
def main():
    fade_text("Hello and welcome to This or That!", HEIGHT // 4)
    fade_text("Let's get started!", HEIGHT // 2)

    for q_text, opt1, opt2 in questions:
        answered = False
        while not answered:
            screen.fill(BG_COLOR)
            question_surface = font.render(q_text, True, TEXT_COLOR)
            question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
            screen.blit(question_surface, question_rect)

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            btn1 = Button(opt1, WIDTH // 4 - 300, HEIGHT // 2)
            btn2 = Button(opt2, WIDTH * 3 // 4 - 300, HEIGHT // 2)

            btn1.draw(mouse_pos)
            btn2.draw(mouse_pos)

            if btn1.is_clicked(mouse_pos, mouse_pressed):
                fade_text(f"You chose {opt1}!", HEIGHT * 3 // 4)
                answered = True
            elif btn2.is_clicked(mouse_pos, mouse_pressed):
                fade_text(f"You chose {opt2}!", HEIGHT * 3 // 4)
                answered = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            clock.tick(FPS)

    fade_text("Thanks for playing!", HEIGHT // 2)
    pygame.time.wait(2000)
    pygame.quit()

main()