"""
You have a web server log file. It's the simplest log format ever, with 2 columns: user_id and page. The rows are written chronologically.

Here's an example...

ts user_id    page_link
1 a-3b7622e /home (1)
2 b-128a9d7 /home (b1)
a-3b7622e /deals/spa (2)
b-128a9d7 /deals/car_wash (b2)
c-7f8e61a /deals/seattle
b-128a9d7 /home (b3)
d-d682a11 /deals/car_wash
a-3b7622e /buy (3)
b-128a9d7 /deals/spa (b4)
c-7f8e61a /deals/coffee
b-128a9d7 /buy (b5)
c-7f8e61a /buy

b -> b1 b2 b3 b4 b5
-> b1 b2 b3
-> b2 b3 b4
-> b3 b4 b5 

a-3b7622e -> [/home /deals/spa /buy /home/ /deals/things-to-do]
Find the most common (popular) 3 page sequence. For example: In the log file above, the answer is /home --> /deals/spa --> /buy because that path has been followed twice (once by a-3b7622e and once by b-128a9d7).

"""

input = ['a-3b7622e /home',
         'b-128a9d7 /home',
         'a-3b7622e /deals/spa',
         'b-128a9d7 /deals/car_wash',
         'c-7f8e61a /deals/seattle',
         'b-128a9d7 /home',
         'd-d682a11 /deals/car_wash',
         'a-3b7622e /buy',
         'b-128a9d7 /deals/spa',
         'c-7f8e61a /deals/coffee',
         'b-128a9d7 /buy',
         'c-7f8e61a /buy']

def find_3_page_seq(input):
    # write your coding
    # assert chronologically sorted
    user_to_pages = {} # {a-3b7622e ['/home', '/deals/spa', '/buy'], ....} 
    for item in input:
        key_and_value = item.split(' ')
        key = key_and_value[0] # user id
        value = key_and_value[1] # page
        if key not in user_to_pages:
            user_to_pages[key] = [value]
        else: 
            user_to_pages[key].append(value)
            
    three_page_sequences = {}      
    for single_user_to_page in user_to_pages.values():
        if len(single_user_to_page) < 3: # didn't visit enough pages
            continue
        for page_num in range(0, len(single_user_to_page)):
            if page_num + 2 < len(single_user_to_page):
                three_pages = single_user_to_page[page_num] + ' ' + single_user_to_page[page_num + 1] +  ' ' + single_user_to_page[page_num + 2]
                if three_pages not in three_page_sequences:
                    three_page_sequences[three_pages] = 1
                else:
                    three_page_sequences[three_pages] += 1
                    
    # see which key has the biggest value in three_page_sequences
    biggest_yet = 0
    matching_pages = ''
    for key, value in three_page_sequences.items():
        if value > biggest_yet:
            biggest_yet = value
            matching_pages = key
        #   
    return matching_pages

    
            
print(find_3_page_seq(input))
        



