def get_num_words(text):
    book = text
    words = []
    words = book.split()
    return len(words)
def get_num_characters(text):
    book = text.lower()
    character_count = {}
    for i in book:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
    return character_count
def sort_dict(dictionary):
    def sort_on(items):
        return items["count"]
    unsorted = []
    temp_dictionary = {}
    for entry in dictionary:
        if entry.isalpha():
            temp_dictionary = {"character": entry, "count": dictionary[entry]}
            unsorted.append(temp_dictionary)
    unsorted.sort(reverse=True, key=sort_on)
    return unsorted