"""
Given a paragraph, Return a dict with characters(only alphabets) as keys
and their count as values
"""

def get_character_count(text):
    dict_of_characters = {}
    for character in text:
        if character.isalpha()==True:
            dict_of_characters[character] = dict_of_characters.get(character,0)+1
    return dict_of_characters


print("Enter the text:")
text_by_user = input()
modified_text = text_by_user.lower()

character_dict = get_character_count(modified_text)

for key,value in character_dict.items():
    print("{} : {}".format(key,value))

