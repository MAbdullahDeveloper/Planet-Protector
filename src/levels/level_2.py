import pygame

from src.ui.back_button import BackButton
from src.ui.hint_button import HintBox, HintButton
from src.ui.input_box import InputBox
from config import screen
from src.utils.colors import BLACK, GREEN, RED
from assets.fonts.font import font, smallFont, answerFont


def level2():
    # Load assets
    level2Title = font.render("Level 2", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    Q1 = smallFont.render("what type of pollution happens ", True, BLACK)
    Q1P2 = smallFont.render("people throw trash on the ground", True, BLACK)
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correct_answers = ["land", "land pollution"]  # List of acceptable answers
    is_correct = False

    # Create back button instance
    back_button = BackButton(10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"  # Return control to the main loop
            input_box.handle_event(event)  # Handle events for the input box

            # Handle back button click
            if back_button.is_clicked(event):
                return "PLAY"  # Go back to the levels page
            if hint_button.is_clicked(event):
                hint_box.update_text("It affects the ground and soil")

            # Check for Enter key press
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                user_input = input_box.get_text().strip().lower()  # Get and clean the input
                if user_input in correct_answers:
                    feedback_text = "Correct!"
                    feedback_color = GREEN
                    is_correct = True
                else:
                    feedback_text = "Incorrect!"
                    feedback_color = RED
                    is_correct = False

        # Clear the screen
        screen.blit(background, (0, 0))

        # Draw the level title
        screen.blit(level2Title, (400, 10))

        # Draw the question
        screen.blit(Q1, (100, 150))
        screen.blit(Q1P2, (90, 190))

        # Draw the answer box label
        screen.blit(answerbox, (150, 400))

        # Draw the input box
        input_box.draw(screen)

        # Draw the hint box
        hint_box.draw(screen)
        hint_button.draw(screen)

        # Draw feedback text
        feedback_surface = answerFont.render(feedback_text, True, feedback_color)
        screen.blit(feedback_surface, (370, 450))

        # Draw the back button
        back_button.draw(screen)

        # Update the display
        pygame.display.flip()

        # If the answer is correct, wait for a few seconds and then move to question 3
        if is_correct:
            pygame.time.wait(2000)  # Wait for 2 seconds
            return level2Q2()


def level2Q2():
    level2Title = font.render("Level 2", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    Q2 = smallFont.render("What do cars give off that ", True, BLACK)
    Q2P2 = smallFont.render("cause air pollution", True, BLACK)
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correct_answers = ["smoke", "gas"]  # List of acceptable answers
    is_correct = False

    # Create back button instance
    back_button = BackButton(10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"  # Return control to the main loop
            input_box.handle_event(event)  # Handle events for the input box

            # Handle back button click
            if back_button.is_clicked(event):
                return "PLAY"  # Go back to the levels page
            if hint_button.is_clicked(event):
                hint_box.update_text("it comes out of the exhaust pipe")

            # Check for Enter key press
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                user_input = input_box.get_text().strip().lower()  # Get and clean the input
                if user_input in correct_answers:
                    feedback_text = "Correct!"
                    feedback_color = GREEN
                    is_correct = True
                else:
                    feedback_text = "Incorrect!"
                    feedback_color = RED
                    is_correct = False

        # Clear the screen
        screen.blit(background, (0, 0))

        # Draw the level title
        screen.blit(level2Title, (400, 10))

        # Draw the question
        screen.blit(Q2, (100, 150))
        screen.blit(Q2P2, (105, 190))

        # Draw the answer box label
        screen.blit(answerbox, (150, 400))

        # Draw the input box
        input_box.draw(screen)

        # Draw the hint box
        hint_box.draw(screen)
        hint_button.draw(screen)

        # Draw feedback text
        feedback_surface = answerFont.render(feedback_text, True, feedback_color)
        screen.blit(feedback_surface, (370, 450))

        # Draw the back button
        back_button.draw(screen)

        # Update the display
        pygame.display.flip()

        # If the answer is correct, wait for a few seconds and then move to question 3
        if is_correct:
            pygame.time.wait(2000)  # Wait for 2 seconds
            return level2Q3()

def level2Q3():
    level2Title = font.render("Level 2", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    Q3 = smallFont.render("What can we use instead of cars", True, BLACK)
    Q3P2 = smallFont.render(" to reduce pollution", True, BLACK)
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correct_answers = ["walk", "ride", "bike", "ride a bike"]  # List of acceptable answers
    is_correct = False

    # Create back button instance
    back_button = BackButton(10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"  # Return control to the main loop
            input_box.handle_event(event)  # Handle events for the input box

            # Handle back button click
            if back_button.is_clicked(event):
                return "PLAY"  # Go back to the levels page
            if hint_button.is_clicked(event):
                hint_box.update_text("you use your feet or pedals")

            # Check for Enter key press
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                user_input = input_box.get_text().strip().lower()  # Get and clean the input
                if user_input in correct_answers:
                    feedback_text = "Correct!"
                    feedback_color = GREEN
                    is_correct = True
                else:
                    feedback_text = "Incorrect!"
                    feedback_color = RED
                    is_correct = False

        # Clear the screen
        screen.blit(background, (0, 0))

        # Draw the level title
        screen.blit(level2Title, (400, 10))

        # Draw the question
        screen.blit(Q3, (100, 150))
        screen.blit(Q3P2, (105, 190))

        # Draw the answer box label
        screen.blit(answerbox, (150, 400))

        # Draw the input box
        input_box.draw(screen)

        # Draw the hint box
        hint_box.draw(screen)
        hint_button.draw(screen)

        # Draw feedback text
        feedback_surface = answerFont.render(feedback_text, True, feedback_color)
        screen.blit(feedback_surface, (370, 450))

        # Draw the back button
        back_button.draw(screen)

        # Update the display
        pygame.display.flip()

        # If the answer is correct, wait for a few seconds and then move to question 3
        if is_correct:
            pygame.time.wait(2000)  # Wait for 2 seconds
            return "PLAY"
