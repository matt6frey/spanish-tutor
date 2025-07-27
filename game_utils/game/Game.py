from game_utils.verbs.ar_verbs import ar_verbs as ar
from game_utils.verbs.er_verbs import er_verbs as er
from game_utils.verbs.ir_verbs import ir_verbs as ir
from game_utils.functions import *
import random

class Game:
    player = None
    verbs = [*ar, *er, *ir]
    number_of_questions = 0
    current_question = 0
    correct_answers = 0
    questions = []
    
    def __init__(self, number_of_questions, player, language_to="english", language_from='spanish'):
        self.number_of_questions = number_of_questions
        self.player = player
        self.language_to = language_to
        self.questions = self.get_random_verbs(number_of_questions)
    
    def play(self):
        while self.current_question != self.number_of_questions:
            self.display_score(False)
            self.ask(self.questions[self.current_question], self.current_question + 1)
            
            self.current_question += 1
        self.display_score()
    
    def display_score(self, verbose=True):
        if not verbose:
            player_tab = f"{self.player.name.capitalize()}'s Score: {self.correct_answers}/{self.number_of_questions}"
            divider = "="*len(player_tab)
            print(player_tab)
            print(f"{divider}\n")
        else:
            print(f"You answered {self.correct_answers} out of a total {self.number_of_questions} questions, correct.\n")
    
    def ask(self, word, question_num):
        self.answer = ''
        while self.answer == '':
            self.answer = input(f"Question {question_num}> What does {word} mean in {self.language_to.capitalize()}?\nAnswer> ")
        expected = translate_word(word)
        if check_answer(self.answer, word):
            self.correct_answers += 1
            print("That's correct! +1 points!\n")
        else:
            print(f"Oops! That's incorrect. The correct answer is {expected}...\n")
    
    def get_random_verbs(self, num):
        """
        Return a random number of elements from a list.
        
        Args:
        - lst: List from which to select elements.
        - num: Number of elements to randomly select.
        
        Returns:
        - A list of randomly selected elements.
        """
        # If num is greater than the list size, return the whole list or handle differently
        num = min(num, len(self.verbs))
        
        # Select and return num random elements from the list
        return random.sample(self.verbs, num)