# https://open.kattis.com/contests/m32krs/problems/cups

# stacking cups
from collections import OrderedDict

num_data = input()
# # file = 'test.txt'  # sys.args[0]
# # file = input()
# # file = open(file, 'r')
# data = []
# print(input())
#
# for line in file:
#     data.append(line.rstrip().split(' '))
# data.pop(0)  # removes number of following rows
# # print("data:", data)
data = []
for num in range(0, int(num_data)):
    line = input()
    data.append(line.rstrip().split(' '))

# print(data)



val_color = {}
for first, second in data:
    if first.isdigit():  # diameter color
        val_color[int(first) / 2] = second
    else:  # color radius
        val_color[int(second)] = first

# print(val_color)
val_color = OrderedDict(sorted(val_color.items()))

for key in val_color:
    print(val_color[key])



