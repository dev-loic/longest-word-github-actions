# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests

class Game:

    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if len(word) == 0:
            return False
        for letter in word:
            if letter not in self.grid:
                return False
        return self.__check_dictionary(word)
    
    # Private
    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']

if __name__=="__main__":
    game = Game()
    print(game.grid)
