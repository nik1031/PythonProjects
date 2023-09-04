# Password Generator Project
from random import choice, randint, shuffle

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordGenerator:
    def __init__(self):
        self.password = ""

        self.password_list = []

        # aggregate random elements together
        self.characters_list = [choice(LETTERS) for char in range(randint(8, 10))]
        self.symbols_list = [choice(SYMBOLS) for char in range(randint(2, 4))]
        self.numbers_list = [choice(NUMBERS) for char in range(randint(2, 4))]

        self.password_list = self.characters_list + self.symbols_list + self.numbers_list

    def make_new(self):
        shuffle(self.password_list)

        #mergign characters in a list together
        self.password = "".join(self.password_list)

        print(f"Your password is: {self.password}")
        return self.password

