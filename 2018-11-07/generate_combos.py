def main():
    all_nums = [123456, 987654]
    for num in range (123456, 987654):
        all_nums.append(num)



    # all_nums = [0, 100]
    # for num in range (0, 100):
    #     all_nums.append(num)


    each_dig_unique = []
    for num in all_nums:
        # print('num: ', num)
        # Your mother recalls that she heard your uncle mention that all the digits are different.
        used_nums = {}
        okay = False
        for each_num in str(num):
            if used_nums.__contains__(each_num):
                okay = False
                break
            elif int(each_num) == 0:
                okay = False
                break
            else:
                used_nums[each_num] = 0
                okay = True
        if okay:
            each_dig_unique.append(num)


    divisible = []
    # You remember that your uncle once said that the six digit number was divisible by each of its individual digits.
    for num in each_dig_unique:
        for each_num in str(num):
            if num % int(each_num) == 0:
                used_nums[each_num] = 0
                okay = True

            else:
                okay = False
                break

        if okay:
            divisible.append(num)

    print(divisible)






    f = open('all_nums.txt', 'w')
    f.write(str(all_nums))
    f.close()


main()