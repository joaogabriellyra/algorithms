def is_anagram(first_string, second_string):
    first_string = merge_sort_word(list(first_string.lower()))
    second_string = merge_sort_word(list(second_string.lower()))

    anagram = first_string == second_string and (
        first_string != "" and second_string != "")
    return (first_string, second_string, anagram)


def merge_sort_word(word, start=0, end=None):
    if end is None:
        end = len(word)

    if end - start > 1:
        mid = (start + end) // 2
        merge_sort_word(word, start, mid)
        merge_sort_word(word, mid, end)
        word = merge(word, start, mid, end)

    return "".join(word)


def merge(word, start, mid, end):
    right_side = word[mid:end]
    left_side = word[start:mid]

    right_index = 0
    left_index = 0

    for index in range(start, end):
        if left_index >= len(left_side):
            word[index] = right_side[right_index]
            right_index += 1
        elif right_index >= len(right_side):
            word[index] = left_side[left_index]
            left_index += 1
        elif left_side[left_index] < right_side[right_index]:
            word[index] = left_side[left_index]
            left_index += 1
        else:
            word[index] = right_side[right_index]
            right_index += 1

    return word
