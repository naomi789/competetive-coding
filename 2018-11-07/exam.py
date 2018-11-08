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


def main():
    friends_high_score = int(input())
    my_scores = list(input())
    friends_scores = list(input())

    exam_length = len(my_scores)

    friends_mistakes = exam_length - friends_high_score

    my_mistakes = 0
    matches = 0

    for mine, theirs in zip(my_scores, friends_scores):
        if mine == theirs and matches < friends_high_score:
            matches += 1
        elif mine != theirs and my_mistakes < friends_mistakes:
            my_mistakes += 1

    print(matches + my_mistakes)

    # print(matches, disagrees)

main()