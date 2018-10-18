def read():

    numbers = []
    num_numbers = int(input())
    for iteration in range(0, num_numbers):
        numbers.append(int(input()))

    print(numbers)
    return numbers


def main(data):
    pass


data = read()

main(data)
