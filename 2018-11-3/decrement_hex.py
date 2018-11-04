# imports

def main():
    answer = []
    f = open('result.txt', 'a')
    with open("-.txt", 'r') as data:
        all_data = data.readline().split(' ')
        for hex in all_data:
            num = int('0x' + hex, 0) - 7
            answer.append(num)


            # out.write(num)

    for num in answer:
        # # print(num)
        # alt = type(num)
        # str(num)

        # f.write(str(num))
        # str(hex(int(num)))

        #
        # print(num.type())
        # print(hex(num))
        print(num, ' ')
        f.write(str(num) + ' ')

    print(answer)







main()