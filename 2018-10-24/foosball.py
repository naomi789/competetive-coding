import queue

data = input()

names = input().strip('/r').split(" ")

WhiteO = names[0]
BlackO = names[1]
WhiteD = names[2]
BlackD = names[3]

line = queue.Queue()

for num in range(len(names) - 4):
    line.put(names[num + 4])

feed = input().strip('/r')

for num in range(len(feed)):
    if (feed[num] == 'W'):
        WhiteO = WhiteD
