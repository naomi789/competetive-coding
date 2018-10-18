# num_data = input()
#
# data = []
# for num in range(0, int(num_data)):
#     line = input()
#     data.append(line.rstrip().split(' '))

data = input()

# print(data)

# x = int(data[0])
# y = int(data[2])
# z = int(data[4])
data = data.split(' ')
# assert(len(data) == 3)
# print(data)
x = int(data[0])
y = int(data[1])
z = int(data[2])

# print(x, y, z)


for num in range(1, z + 1):
    # print('num', num)
    is_fizz = False
    if num % x == 0:
        is_fizz = True
    if num % y == 0:
        if is_fizz:
            print('FizzBuzz')
        else:
            print('Buzz')
    else:
        if is_fizz:
            print('Fizz')
        else:
            print(num)
