from collections import defaultdict
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

        # if not start in translators.keys():
        #     translators[start] = (end, cost)
        # else:
        #     translators[start] = translators[start].append((end, cost))

    print(goal_langs)
    print(translators)
    return goal_langs, translators


def determine(target_langs):
    pass


def helper():
    pass


determine(read())