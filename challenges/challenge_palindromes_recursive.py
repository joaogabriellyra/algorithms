def is_palindrome_recursive(word, low_index, high_index):
    if low_index == high_index or low_index + 1 == high_index:
        return word[low_index] == word[high_index]

    if not word or word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
