def e_squares(begin, end):
    squares = [x ** 2 for x in range(begin, end + 1)]
    return squares


if __name__ == "__main__":
    first_num = int(input("Enter begin num1: "))
    second_num = int(input("Enter ending num2: "))

    output = e_squares(first_num, second_num)

    print(output)
