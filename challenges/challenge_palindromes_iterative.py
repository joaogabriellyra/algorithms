def is_palindrome_iterative(word):
    if not word:
        return False
    reversed = list(word)[-1::-1]
    for index, letter in enumerate(list(word)):
        if letter != reversed[index]:
            return False
    return True
