import pygame

from config import font, smallFont, BLACK, GREEN, RED, answerFont
from ui.back_button import BackButton
from ui.hint_button import HintBox, HintButton
from ui.input_box import InputBox
from config import screen


def level3():
    level3Title = font.render("Level 3", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    Q1 = smallFont.render("What do plants need to grow ", True, BLACK)
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correct_answers = ["sun", "sunlight", "water", "soil", "heat"]  # List of acceptable answers
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
                hint_box.update_text("from nature to help plants grow")

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
        screen.blit(level3Title, (400, 10))

        # Draw the question
        screen.blit(Q1, (100, 150))

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
            return level3Q2()

def level3Q2():
    level3Title = font.render("Level 3", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    Q2 = smallFont.render("What bag is better for the earth? ", True, BLACK)
    Q2P2 = smallFont.render("Plastic, Paper or Reusable", True, BLACK)
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correct_answers = ["reusable"]  # List of acceptable answers
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
                hint_box.update_text("You can use it again and again")

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
        screen.blit(level3Title, (400, 10))

        # Draw the question
        screen.blit(Q2, (100, 150))
        screen.blit(Q2P2,(105, 190))

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
            return level3Q3()

def level3Q3():
    level3Title = font.render("Level 3", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    Q3 = smallFont.render("What do solar panels use ", True, BLACK)
    Q3P2 = smallFont.render("to make energy", True, BLACK)
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correct_answers = ["sun", "sunlight" "the sun"]  # List of acceptable answers
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
                hint_box.update_text("helps plants grow")

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
        screen.blit(level3Title, (400, 10))

        # Draw the question
        screen.blit(Q3, (100, 150))
        screen.blit(Q3P2,(105, 190))

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