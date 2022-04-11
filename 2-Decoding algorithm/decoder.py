import string


def decoder (word, encrypted_message):
    char_set = string.ascii_lowercase + ' '
    vocabulary = open('words.txt', 'r')
    # először a word az lesz, hogy early
    word_num = [char_set.index(i) for i in word] # visszaadja a word betűit számokban


