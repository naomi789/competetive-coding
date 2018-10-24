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

    # print(goal_langs)
    # print(translators)
    return goal_langs, translators


def determine(target_langs, translators):
    sum_all_costs = 0
    current_lang_cost = ('English', 0)
    # for each language that you want to get to
    for one_target_lang in target_langs:
        sum_costs = 0
        lowest_cost = 0

        # where I am starting from, going to, $$ spent so far
        cost = helper(current_lang_cost, one_target_lang, sum_costs)
        if cost != 'Impossible' and cost < lowest_cost:
            lowest_cost = cost

        sum_all_costs += lowest_cost

    return sum_all_costs



def helper(current_lang_cost, one_target_lang, sum_costs):
    found = False
    current_lang = current_lang_cost[0]
    current_cost = current_lang_cost[1]

    # base case:
    if current_lang == one_target_lang:
        return sum_costs

    # then consider each langauge that you can get to from here
    for some_lang_cost in translators[current_lang]:
        # and from that language consider each language that you can get to
        these_costs = helper(some_lang_cost, one_target_lang, sum_costs)
        if these_costs != 'Impossible':
            sum_costs += these_costs

    return 'Impossible'





goal_langs, translators = read()
print(determine(goal_langs, translators))