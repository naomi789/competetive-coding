from collections import defaultdict


def main():
    slack = ':crossed_fingers::imp::nerd_face::first_place_medal::panda_face::hankey::nerd_face::no_entry_sign::muscle::crossed_fingers::speaking_head_in_silhouette::face_with_rolling_eyes::nerd_face::first_place_medal::panda_face::hankey::nerd_face::grinning::white_check_mark::worried::nerd_face::bread::panda_face::white_check_mark::no_entry_sign::muscle::first_place_medal::nerd_face::panda_face::imp::nerd_face::no_entry_sign::muscle::worried::nerd_face::imp::pouting_cat::grinning::hushed::nerd_face::imp::crossed_fingers::white_check_mark::fire::no_entry_sign::nerd_face::first_place_medal::panda_face::hankey::nerd_face::ghost::hankey::fire::no_entry_sign::nerd_face::grinning::speaking_head_in_silhouette::fire::bread::worried::white_check_mark::nerd_face::no_entry_sign::muscle::worried::fire::worried::nerd_face::no_entry_sign::muscle::white_check_mark::worried::worried::nerd_face::broken_heart::hankey::worried::fire::no_entry_sign::crossed_fingers::panda_face::speaking_head_in_silhouette::fire::sob::nerd_face::bread::muscle::grinning::no_entry_sign::nerd_face::crossed_fingers::fire::nerd_face::first_place_medal::panda_face::hankey::nerd_face::speaking_head_in_silhouette::grinning::ghost::worried::nauseated_face::nerd_face::bread::muscle::grinning::no_entry_sign::nerd_face::crossed_fingers::fire::nerd_face::first_place_medal::panda_face::hankey::white_check_mark::nerd_face::broken_heart::hankey::worried::fire::no_entry_sign::nauseated_face::nerd_face::bread::muscle::grinning::no_entry_sign::nerd_face::crossed_fingers::fire::nerd_face::no_entry_sign::muscle::worried::nerd_face::grinning::crossed_fingers::white_check_mark::nerd_face::fire::octopus::worried::worried::sunglasses::nerd_face::eyes::worried::pouting_cat::panda_face::face_with_symbols_on_mouth::crossed_fingers::no_entry_sign::first_place_medal::nerd_face::panda_face::imp::nerd_face::grinning::speaking_head_in_silhouette::nerd_face::hankey::speaking_head_in_silhouette::pouting_cat::grinning::sunglasses::worried::speaking_head_in_silhouette::nerd_face::fire::bread::grinning::pouting_cat::pouting_cat::panda_face::bread::sob::nerd_face::first_place_medal::panda_face::hankey::white_check_mark::nerd_face::imp::pouting_cat::grinning::hushed::nerd_face::crossed_fingers::fire::clown_face::nerd_face::grinning::imp::white_check_mark::crossed_fingers::face_with_symbols_on_mouth::grinning::speaking_head_in_silhouette:_:panda_face::white_check_mark:_:worried::hankey::white_check_mark::panda_face::octopus::worried::grinning::speaking_head_in_silhouette:_:fire::bread::grinning::pouting_cat::pouting_cat::panda_face::bread:_:bread::panda_face::bread:_:no_entry_sign::muscle::worried::white_check_mark::worried::fire:_:grinning:_:sunglasses::crossed_fingers::imp::imp::worried::white_check_mark::worried::speaking_head_in_silhouette::face_with_symbols_on_mouth::worried::nerd_face:'
    emoji = '🤞👿🤓🥇🐼💩🤓🚫💪🤞🗣🙄🤓🥇🐼💩🤓😀✅😟🤓🍞🐼✅🚫💪🥇🤓🐼👿🤓🚫💪😟🤓👿😾😀😯🤓👿🤞✅🔥🚫🤓🥇🐼💩🤓👻💩🔥🚫🤓😀🗣🔥🍞😟✅🤓🚫💪😟🔥😟🤓🚫💪✅😟😟🤓💔💩😟🔥🚫🤞🐼🗣🔥😭🤓🍞💪😀🚫🤓🤞🔥🤓🥇🐼💩🤓🗣😀👻😟🤢🤓🍞💪😀🚫🤓🤞🔥🤓🥇🐼💩✅🤓💔💩😟🔥🚫🤢🤓🍞💪😀🚫🤓🤞🔥🤓🚫💪😟🤓😀🤞✅🤓🔥🐙😟😟😎🤓👀😟😾🐼🤬🤞🚫🥇🤓🐼👿🤓😀🗣🤓💩🗣😾😀😎😟🗣🤓🔥🍞😀😾😾🐼🍞😭🤓🥇🐼💩✅🤓👿😾😀😯🤓🤞🔥🤡🤓😀👿✅🤞🤬😀🗣_🐼✅_😟💩✅🐼🐙😟😀🗣_🔥🍞😀😾😾🐼🍞_🍞🐼🍞_🚫💪😟✅😟🔥_😀_😎🤞👿👿😟✅😟🗣🤬😟🤓'
    slack = slack.replace('::', ': :')
    slack = slack.split(' ')
    emojis = []
    for an_emoji in emojis:
        print(an_emoji)
        emojis.append(an_emoji)

    # emojis = emojis.split()
    print(emojis)
    # print(slack)
    return (slack, emojis)


def see_counts(letters):
    # print(letters)
    freq = defaultdict()
    for letter in letters:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    for item, frequency in freq.items():
        print("{} ({})".format(item, frequency))
    return freq


slack, emojis = main()
freq = see_counts(slack)

pip install uncompyle6