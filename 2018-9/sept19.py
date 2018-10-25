# /problems/3dprinter/file/statement/en/img-0001.jpg
# Picture by Ariosvaldo Gonzáfoles, cc-by
# You have a single 3D printer, and would like to use it to produce n statues. However, printing the statues one by one on the 3D printer takes a long time, so it may be more time-efficient to first use the 3D printer to print a new printer. That new printer may then in turn be used to print statues or even more printers. Print jobs take a full day, and every day you can choose for each printer in your possession to have it print a statue, or to have it 3D print a new printer (which becomes available for use the next day).
#
# What is the minimum possible number of days needed to print at least n statues?
#
# INPUT:
# The input contains a single integer n (1≤n≤10000), the number of statues you need to print.
#
# OUTPUT:
# Output a single integer, the minimum number of days needed to print at least n statues.

import sys
import math

def main():
    try:
        needed_statues = int(input('Input:'))
    except ValueError:
        print("Not a number")

    num_printers = 1
    time_passed = 0
    time_used = use_printer(needed_statues, num_printers,  time_passed)
    print(time_used)


def use_printer(needed_statues, num_printers, time_passed):
    if needed_statues == 0:
        return time_passed

    # if num_printers >= needed_statues:
    # if math.log(needed_statues) <= num_printers:
        # make statue
        needed_statues -= needed_statues
        time_passed += 1
    else:
        # make printer
        num_printers += 1
        time_passed += 1

    return use_printer(needed_statues, num_printers, time_passed)


main()
