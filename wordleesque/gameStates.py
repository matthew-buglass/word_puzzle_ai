
import os

class GameState(object):
    """
    Holds the game state of a Wordle Puzzle
    """
    def __int__(self):
        """
        Creates a Wordle puzzle

        :return: A Wordle puzzle
        """

        # word = os.getenv()
        # Guesses are marked as -1 for no guess, and 0-25 for letters A-Z
        guesses = [[-1] * 5] * 6

        # Guess results are marked as
        #   -1 for no guess,
        #   0 for wrong letter,
        #   1 for right letter wrong place, and
        #   2 for right letter right place
        guess_results = [[-1] * 5] * 6

print(os.environ.get('ROOT_DIR'))