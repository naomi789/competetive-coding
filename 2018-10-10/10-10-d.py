data = input()

list = []
for letter in data:
    list.append(letter)
k = 0
for i in range(1, len(list)+1):
    if(k == 0 and len(list)%i == 0):
        works = True
        for period in range(len(list)):
            if(list[period] != list[((period)-int(period/i)) % i]):
                works = False
        if(works == True):
            k = i

if (k == 0):
    k = len(list)
print(k)