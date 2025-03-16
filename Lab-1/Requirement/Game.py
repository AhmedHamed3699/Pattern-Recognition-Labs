import numpy as np
from typing import Tuple, List

# TODO [1]: implement the guessing_game function


def guessing_game(max: int, *, attempts: int) -> Tuple[bool, List[int], int]:
    """
    Play a number guessing game where the user has to guess a randomly generated number within a specified range.
    Args:
        max (int): The upper limit for the random number generation (exclusive).
        attempts (int): The number of attempts the user has to guess the correct number.
    Returns:
        Tuple[bool, List[int], int]: A tuple containing:
            - A boolean indicating whether the user guessed the correct number.
            - A list of integers representing the user's guesses.
            - The correct number that was to be guessed.
    """
    correct_number: int = np.random.randint(1, max)
    guesses: List[int] = []
    while attempts > 0:
        try:
            user_number: int = int(input("Enter your guess: "))
            guesses.append(user_number)
            if user_number > correct_number:
                print("Too High!")
            elif user_number < correct_number:
                print("Too Low!")
            else:
                print("Correct", flush=True)
                return True, guesses, correct_number
            attempts -= 1
            print(f"{attempts} attempts left...", flush=True)
        except ValueError:
            print("Invalid input", flush=True)
    return False, guesses, correct_number

# TODO [2]: implement the play_game function


def play_game() -> None:
    """
    Starts and manages a guessing game.
    The game allows the user to guess a number within a specified range
    and a limited number of attempts. The maximum value for the guessing
    range and the number of attempts are predefined within the function.
    Returns:
        None
    """
    print("----------------------", flush=True)
    print("Starting a new game...", flush=True)
    max_value: int = 20
    attempts: int = 5
    result, guesses, chosen_int = guessing_game(max_value, attempts=attempts)
    if result:
        assert chosen_int in guesses, "There is something wrong with the program"
        print(f"Your guesses: {guesses}")
        print("Congratulations! You guessed the correct number.")
    else:
        assert chosen_int not in guesses, "There is something wrong with the program"
        print(f"Your guesses: {guesses}")
        print(f"Sorry, you've failed. The correct number was {chosen_int}")
        print("Do you wanna play again?", flush=True)
        if input().lower() == "yes":
            play_game()
        else:
            print("Goodbye!")
