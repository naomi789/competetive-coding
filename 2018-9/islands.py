def read():
    height, width = input().split(" ")
    height = int(height)
    width = int(width)
    print(height, width)
    array = []

    # for columns in range(0, width):

    for rows in range(0, height):  # a number bw 0 and
        row = input() # all the characters
        counter = 0
        for letter in row:
            print(letter, rows, counter)
            # array[rows][counter]
            counter += 1

        # array.append(row)
            # array[columns][row] =

    print(array)
    # for iteration in range(0, num_numbers):
    #     numbers.append(int(input()))

    # print(numbers)
    return array

def main(data):
    pass


data = read()
main(data)
