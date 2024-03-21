from square_generator import SquareGenerator
from cubic_generator import CubicGenerator


if __name__ == "__main__":
    first_num = int(input("Enter begin num1: "))
    second_num = int(input("Enter ending num2: "))

    output = SquareGenerator.generate_squares(first_num, second_num)
    output_cubic = CubicGenerator.generate_squares(first_num, second_num)

    print(output)
    print(output_cubic)

