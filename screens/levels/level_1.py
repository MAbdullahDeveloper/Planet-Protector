import pygame

from config import font, smallFont, BLACK, GREEN, RED, answerFont
from ui.back_button import BackButton
from ui.hint_button import HintBox, HintButton
from ui.input_box import InputBox
from config import screen


def level1():
    # Load assets
    level1Title = font.render("Level 1", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)  # Create an instance of InputBox
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    RecycleImage = pygame.image.load("assets/images/Recycle_processed.png")  # Question 1 - Image
    Q1 = smallFont.render("What does this symbol mean?", True, BLACK)

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correctQ1 = ["recycle", "recycling", "recyclable"]
    is_correct = False
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")
    back_button = BackButton(10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"  # Return control to the main loop
            input_box.handle_event(event)  # Handle events for the input box
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.is_clicked(event):
                    return "PLAY"
            if hint_button.is_clicked(event):
                hint_box.update_text("It's about reusing material")

            # Check for Enter key press
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                user_input = input_box.get_text().strip().lower()  # Get and clean the input

                print(f"User input: '{user_input}'")  # Debugging: Print the input

                if user_input in correctQ1 and not is_correct:
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
        screen.blit(level1Title, (400, 10))

        # Draw the question and image
        screen.blit(Q1, (170, 150))
        screen.blit(RecycleImage, (400, 200))

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

        # If the answer is correct, wait for a few seconds and then move to the next question
        if is_correct:
            pygame.time.wait(1000)  # Wait for 1 second
            return question2()  # Move to the next question



def question2():
    # Load assets
    level1Title = font.render("Level 1", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)  # Create an instance of InputBox
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    Q2 = smallFont.render("Can you name one material you can", True, BLACK)
    Q2P2 = smallFont.render("recycle?", True, BLACK)
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correct_answers = ["plastic", "paper", "glass", "metal"]  # List of acceptable answers
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
                hint_box.update_text("It comes from a bottle or can")


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
        screen.blit(level1Title, (400, 10))

        # Draw the question
        screen.blit(Q2, (100, 150))
        screen.blit(Q2P2, (300, 190))

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
            return question3()  # Move to question 3


def question3():
    # Load assets
    level1Title = font.render("Level 1", True, BLACK)  # Page Title
    background = pygame.image.load("assets/images/background.png").convert()
    input_box = InputBox(370, 400, 200, 40)  # Create an instance of InputBox
    answerbox = answerFont.render("Answer Box:", True, BLACK)
    Q3 = smallFont.render("Which bin is used for recycling?", True, BLACK)
    recycleBin = pygame.image.load("assets/images/Recyclingbin_processed.png")
    optrecycleBin = font.render("A", True, BLACK)  # option a for teh user to pick
    otherbin = pygame.image.load("assets/images/Otherbin_processed.png")
    optother = font.render("B", True, BLACK)  # option for user to pick

    # Variables for feedback and correctness
    feedback_text = ""
    feedback_color = BLACK
    correct_answers = "a"  # List of acceptable answers
    is_correct = False
    hint_button = HintButton(800, 10, 150, 50, "Hint")
    hint_box = HintBox(250, 450, 550, 100, (200, 200, 255), "")

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
                hint_box.update_text("Look at the symbol on the bin!")

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
        screen.blit(level1Title, (400, 10))

        # Draw the question
        screen.blit(Q3, (100, 150))
        screen.blit(recycleBin, (250, 230))
        screen.blit(otherbin, (470, 230))
        screen.blit(optrecycleBin, (230, 240))
        screen.blit(optother, (450, 240))

        # Draw the hint box
        hint_box.draw(screen)
        hint_button.draw(screen)

        # Draw the answer box label
        screen.blit(answerbox, (170, 400))

        # Draw the input box
        input_box.draw(screen)

        # Draw feedback text
        feedback_surface = answerFont.render(feedback_text, True, feedback_color)
        screen.blit(feedback_surface, (370, 450))
        # Draw the back button
        back_button.draw(screen)
        # Update the display
        pygame.display.flip()
        # If the answer is correct, wait for a few seconds and then return to the levels page
        if is_correct:
            pygame.time.wait(1000) # Wait for 1 second
            return "PLAY"  # Return to the levels page
