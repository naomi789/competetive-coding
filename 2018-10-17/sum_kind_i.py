def read():
    num_numbers = int(input())
    return num_numbers


def main(num_numbers):
    for iter in range(0, num_numbers):
        two_nums = input().strip('\r').split(" ")
        important_num = int(two_nums[1])
        test_name = int(two_nums[0])

        s1 = 0
        s2 = 0
        s3 = 0
        for num in range(0, important_num):
            s1 = s1 + num + 1
            s2 = s2 + 2*num + 1
            s3 = s3 + 2*num + 2

        print(test_name, s1, s2, s3)


data = read()
# print(data)
main(data)
