def read():
    # numbers = []
    # num_numbers = int(input())
    # for iteration in range(0, num_numbers):
    #     numbers.append(int(input()))
    #
    # # print(numbers)
    numbers = [4, 4, 4, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 4, 4]
    return numbers

def helper(numbers, starting_spot):
    record = 0
    previousUp = False
    previousDown = False

    for iterator in range(starting_spot, len(numbers)):
        if iterator == 0:
            continue

        if numbers[iterator - 1] > numbers[iterator]:
            # decrease
            if previousDown:  # can't zig twice in a row
                return record
            else:
                previousDown = True
                previousUp = False
                record += 1

        elif numbers[iterator - 1] < numbers[iterator]:
            # increase
            if previousUp:
                return record
            else:
                previousDown = False
                previousUp = True
                record += 1
        else:
            return record

    return record


def main(numbers):
    best_record = 0

    for iterator in range(0, len(numbers)):
        newest_record = helper(numbers, iterator)
        if newest_record > best_record:
            best_record = newest_record
    return best_record + 1






numbers = read()
print(main(numbers))
