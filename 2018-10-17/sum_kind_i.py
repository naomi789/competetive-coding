def read():
    num_numbers = int(input())
    return num_numbers

# (didn't use this, but for future reference, it was Gussian: https://en.wikipedia.org/wiki/Gauss_sum)
# https://open.kattis.com/problems/sumkindofproblem

def main(num_numbers):
    for iter in range(0, num_numbers):
        two_nums = input().strip('\r').split(" ")
        n = int(two_nums[1])
        test_name = int(two_nums[0])

        s1 = int(n * (n + 1) / 2)
        s2 = int(s1 * 2 - n)
        s3 = int(s1 * 2)

        print(test_name, s1, s2, s3)


data = read()
# print(data)
main(data)
