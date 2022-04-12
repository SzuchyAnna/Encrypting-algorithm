import string


def decoder(word, encrypted_message_1, encrypted_message_2):
    # char_set = string.ascii_lowercase + ' '
    # először a word az lesz, hogy early
    key = piece_teller(word, encrypted_message_1)  # ez most egy list
    word_2 = piece_teller(key, encrypted_message_2)  # ez most egy list
    message_2 = ''.join(word_2)  # ez most viszont string
    word_list = word_guesser(message_2)  # megkapjuk az első szavát az üzenetnek
    


def piece_teller(word, encrypted_message):
    char_set = string.ascii_lowercase + ' '
    encrypted_message_num = num_gen(encrypted_message) # visszaadja az encrypted message betűit számokban
    word_num = num_gen(word) # visszaadja a word betűit számokban
    new_word_num = [(encrypted_message_num[i] - word_num[i]) % 27 for i in range(len(word_num))]
    return [char_set[i] for i in new_word_num]


def word_guesser (word):
    vocabulary = open('words.txt', 'r')
    wordlist = []
    for i in vocabulary:
        if i.startswith(word):
            wordlist.append(i.strip())
    return wordlist


def num_gen(text):
    char_set = string.ascii_lowercase + ' '
    return [char_set.index(i) for i in text]



