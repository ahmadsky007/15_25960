import math
from square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    @staticmethod
    def generate_squares(first, last):
        if last < first:
            first, last = last, first
            print("first was > then second so switched")
        cubes = [(x, x ** 3) for x in range(first, last + 1)]
        return cubes

    @staticmethod
    def generate_squares(first, last):
        if last < first:
            first, last = last, first
            raise ValueError("First was larger than last!")
        squares = [(x, math.sqrt(x)) for x in range(first, last + 1)]
        return squares