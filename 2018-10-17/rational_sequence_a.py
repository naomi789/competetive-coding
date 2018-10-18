# problem: https://open.kattis.com/contests/dt5jiu/problems/rationalsequence2

def read():
    num_rows = int(input())

    numer_denom = 0
    all_pairs = []
    for iteration in range(0, num_rows):
        case_numer_denom = input()
        case,numer_denom = case_numer_denom.split(" ")
        numer, denom = numer_denom.split("/")
        print(case, numer, denom)
        # numbers.append(int(input()))

    return all_pairs


def main(all_pairs):
    pass


main(read())