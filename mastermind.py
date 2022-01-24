"""In this game we have 6 colors and 10 tries"""
import copy,random

guess = None

class MasterMind:
    """The main MasterMind game Process"""

    def __init__(self, solution=None):
        if solution is None:
            self.solution = self.get_random_solution()
        else:
            self.solution = solution
        print("Solution:       ",self.solution)
        print('─' * 45)  # U+2500, Box Drawings Light Horizontal

    def get_random_solution(self):
        """Returns a random "solution" to be the hidden code"""
        solution = []
        for i in range(4):
            solution.append(random.randrange(0,6))
        return solution

    def check_guess(self):
        """Returns the nb of "correct" and nb of "misplaced" guess"""
        correct = self.get_correct_colors(guess)
        misplaced = self.get_misplaced_colors(guess, correct)

        print("Correct   -> {}\nMisplaced -> {}".format(correct.count(True), misplaced.count(True)))
        print("Check Guess:",correct)
        print('─' * 45)  # U+2500, Box Drawings Light Horizontal
        # print("Solution: ",self.solution)
        return correct.count(True), misplaced.count(True)

    def get_correct_colors(self):
        """Returns the "correct" colors"""
        correct_list = []
        for g, s in zip(guess, self.solution):
            if g == s:
                correct_list.append(True)
            else:
                correct_list.append(False)
        return correct_list
        

    def get_misplaced_colors(self):
        """Returns the "misplaced" colors"""
        mock_solution = copy.copy(self.solution)
        misplaced_list = []
        for index, (status, g, s) in enumerate(zip(correct_list, guess, mock_solution)):
            if status == True:
                guess[index] = -1
                mock_solution[index] = -1
            # print(guess)  ->this show the coorect color by -1 and misplace by 1
        for color in guess:
            if color == -1:
                misplaced_list.append(False)
            elif color in mock_solution:
                misplaced_list.append(True)
                mock_solution.remove(color)
            else:
                misplaced_list.append(False)       
        return misplaced_list



    def is_won(self):
        """Verify that the guess is correct according to the solution"""
        for g, s in zip(guess, self.solution):
            if g != s:
                return False
        return True