class SquareGenerator:
    @staticmethod
    def generate_squares(start, end):
        return [x ** 2 for x in range(start, end + 1)]


if __name__ == "__main__":
    square_generator = SquareGenerator()
    first_num = int(input("Enter begin num1: "))
    second_num = int(input("Enter ending num2: "))

    output = square_generator.generate_squares(first_num, second_num)

    print(output)
