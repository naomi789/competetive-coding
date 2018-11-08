# Your friend and you took the same true/false exam. You know your answers, your friend’s answers, and the number of your friend’s answers that were correct.
#
# Compute the maximum possible score you could have gotten.
#
# Input
# The first line contains a single integer k, the number of correct answers on your friend’s exam.
#
# The second line contains a string of characters, the answers you wrote down. Each letter is either a ‘T’ or an ‘F’. The length of the string is the number n of exam questions.
#
# The third line also contains a string of n characters, the answers your friend wrote down. Each letter is either a ‘T’ or an ‘F’.
#
# Bounds are 0≤k≤n≤1000;1≤n.

def read():
    first_line = input()
    num_languages, num_translators = first_line.split(' ')
    num_languages = int(num_languages)
    num_translators = int(num_translators)
    all_langs = input()
    goal_langs = []
    translators = defaultdict(list)
    for lang in all_langs.split(' '):
        goal_langs.append(lang)
    for iteration in range(0, num_translators):
        start, end, cost = input().split(' ')
        cost = int(cost)

        translators[start].append((end, cost))

    # print(goal_langs)
    # print(translators)
    return goal_langs, translators

def main(read()):

    pass



main()