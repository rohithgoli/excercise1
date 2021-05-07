"""
Given a paragraph, Return a dict with characters as keys and their count
as values(also include spaces" " in dict)
"""
#Edit such that it should take into account only alphabets
"""Defining function that returns character dictionary"""
def get_character_count(text):
    dict_of_characters = {}
    for character in text:
        if character.isalpha()==True:
            if character in dict_of_characters:
                dict_of_characters[character] += 1
            else:
                dict_of_characters[character]= 1
    return dict_of_characters



"""Taking Input from user"""

print("Enter the text:")
text_by_user = input()
#print(text_by_user)
modified_text = text_by_user.lower()
#print(modified_text)


character_dict = get_character_count(modified_text)


"""Printing result of characters and their count"""
for key,value in character_dict.items():
    print("{} : {}".format(key,value))

