import random


class ComplimentGenerator:
    def __init__(self):
        pass

    @staticmethod
    def get_girlfriend_compliment():
        random.seed(None)
        x = random.randint(1, 18)
        # Example...
        compliment = 'You are Beautiful.'
        with open("helper_library/compliments.txt", "r") as compliment_file:
            for i in range(x):
                compliment = compliment_file.readline()
        return compliment
