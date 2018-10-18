# problem: https://open.kattis.com/contests/dt5jiu/problems/rationalsequence2

def read():
    num_rows = int(input())

    numer_denom = 0
    all_pairs = []
    for iteration in range(0, num_rows):
        case_numer_denom = input().strip('\r')
        case,numer_denom = case_numer_denom.split(" ")
        numer, denom = numer_denom.split("/")
        all_pairs.append((int(case), int(numer), int(denom)))

    # print(all_pairs)
    return all_pairs


def main(all_pairs):
    pass


main(read())