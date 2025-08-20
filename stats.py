def get_book_word_count(text):
        return len(text.split())

def get_stats(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict

def get_sorted(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)