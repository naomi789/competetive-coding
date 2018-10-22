import string

def read_asci():
    file = 'test.txt'
    text_file = open(file, 'r')
    ascii = text_file.read()
    # print(ascii)
    data = ascii.replace(':', '')
    data = data.replace(' ', '')
    # data = data.replace('\n', '')
    return data


def read_ascii_art(data):
    answer = ''
    # print('\n\n', data)
    for loc in range(0, len(data)):
        if loc == len(data) - 1:
            break
        if data[loc] != data[loc + 1]:
            answer += data[loc]
    print(answer)

# read_ascii_art(read_asci())


def make_four_letter_combos():
    combos = set()
    for first_letter in string.ascii_lowercase:
        for second_letter in string.ascii_lowercase:
            for third_letter in string.ascii_lowercase:
                for four_letter in string.ascii_lowercase:
                    word = first_letter + second_letter + third_letter + four_letter
                    combos.add(word)
                    print(word)




make_four_letter_combos()