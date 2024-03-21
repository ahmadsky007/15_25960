import math


class SquareGenerator:
    @staticmethod
    def generate_squares(first, last):
        if last < first:
            first, last = last, first
            print("first was > then second so switched")
        squares = [(x, math.sqrt(x)) for x in range(first, last + 1)]
        return squares


if __name__ == "__main__":
    square_generator = SquareGenerator()
    first_num = int(input("Enter begin num1: "))
    second_num = int(input("Enter ending num2: "))

    output = square_generator.generate_squares(first_num, second_num)

    print(output)
