"""
From given text, make a dictionary containing different word lengths as keys
and list of words with corresponding length as values
"""


"""
Defining function that takes list of words and
returns a dict with
word length(key) and list of words with corresponding length(values)
"""

def get_dict_with_available_word_lengths(words_list):
    desired_dict = {}
    for each_word in words_list:
        each_word_length = len(each_word)
        if each_word_length in desired_dict:
            existing_list_with_length = desired_dict[each_word_length]
            modified_list_with_length = existing_list_with_length+[each_word]
            desired_dict[each_word_length] = modified_list_with_length
        else:
            desired_dict[each_word_length] = [each_word]
    return desired_dict
            


"""Taking Input from user"""

print("Enter the text:")
text_by_user = input()
#print(text_by_user)

list_of_all_words = text_by_user.split()
unique_words_set = set(list_of_all_words)
unique_words_list = list(unique_words_set)




word_length_dict = get_dict_with_available_word_lengths(unique_words_list)

"""Printing result"""
for key,value in word_length_dict.items():
    print("{} : {}".format(key,value))


