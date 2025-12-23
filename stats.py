def count_words(string):
    list_of_string = string.split()
    return len(list_of_string)

def count_characters(string):
    lowered_string = string.lower()
    char_dict = {}
    for lowered in lowered_string:
        if lowered not in char_dict:
            char_dict[lowered] = 0
        char_dict[lowered] += 1
    return char_dict

def get_sorted_list(dict):
    list_of_dict = []
    for key in dict:
        list_of_dict.append({"char": key, "num": dict[key]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def sort_on(item):
    return item["num"]    
