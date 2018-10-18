def get_data():
    data = input()
    clean = []
    for letter in data:
        clean.append(letter.lower())
    return clean


def start(data):
    num = []
    # print(data)
    for letter in data:
        temp = ord(letter)
        # print(temp)
        num.append(temp % 97)

    # print(num)

    total = 0
    stopping_point = int(len(num) / 2)
    first_stopping_point = stopping_point
    for temp in range(0, stopping_point):
        # print(num[temp])
        total += num[temp]

    # print(total)

    for temp in range(0, stopping_point):
        num[temp] += total
        num[temp] = num[temp] % 26
    # print(num)







    # second half:

    # print(total)
    total = 0
    for temp in range(stopping_point, len(num)):
        # print(num[temp])
        total += num[temp]

    # print(total)

    for temp in range(stopping_point, len(num)):
        num[temp] += total
        num[temp] = num[temp] % 26
    # print(num)


    #  next step
    for temp in range(0, first_stopping_point):
        num[temp] = num[temp] + num[temp + first_stopping_point]
        num[temp] = num[temp] % 26
        num[temp] += 97

    # print(num)


    word = ""

    for temp in range(0, first_stopping_point):
        word = word + chr(num[temp])

    print(word.upper())





data = get_data()
number_answer = start(data)


