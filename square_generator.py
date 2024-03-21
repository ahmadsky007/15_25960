import math


class SquareGenerator:
    @staticmethod
    def generate_squares(first, last):
        if last < first:
            first, last = last, first
            print("first was > then second so switched")
        squares = [(x, math.sqrt(x)) for x in range(first, last + 1)]
        return squares