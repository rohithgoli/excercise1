"""
From given text, make a dictionary containing different word lengths as keys
and list of words with corresponding length as values it should not count
period/comma/question mark
"""

def get_dict_with_available_word_lengths(words_list):
    desired_dict = {}
    for each_word in words_list:
        each_word_length = len(each_word)
        if each_word_length not in desired_dict:
            desired_dict[each_word_length] = [each_word]
        else:
            desired_dict[each_word_length].append(each_word)
    return desired_dict
            

print("Enter the text:")
text_by_user = input()

list_of_all_words = text_by_user.split()

list_of_all_words = list(map(lambda word: word.strip(",.?"), list_of_all_words))

unique_words_set = set(list_of_all_words)
unique_words_list = list(unique_words_set)

word_length_dict = get_dict_with_available_word_lengths(unique_words_list)

for key,value in word_length_dict.items():
    print("{} : {}".format(key,value))


