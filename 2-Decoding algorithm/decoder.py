import string


def decoder(word, encrypted_message_1, encrypted_message_2):
    # char_set = string.ascii_lowercase + ' '
    # először a word az lesz, hogy early
    message_1 = word + ' '
    key = piece_teller(message_1, encrypted_message_1)  # ez most egy list
    piece = piece_teller(key, encrypted_message_2)  # ez most egy list
    # ez az első szótöredékünk
    # jelen pillanatban a 2. üzenet darabkája
    # a piece egy újraírandó lista, ami mindig ahhoz tartalmaz üzenetrészt, hogy kitaláljuk a key következő részét
    word_list = word_guesser(piece)  # megkapjuk az első potenciális szavait a 2. üzenetnek
    message_2 = ''.join(piece)


def nemtom(word_list, piece, message_1, message_2, encrypted_message_1, encrypted_message_2):
    for x in word_list:
        inner_message_2 = message_2 + x.replace(''.join(piece), '') + ' '
        inner_key = piece_teller(inner_message_2, encrypted_message_2)
        inner_message_1 = piece_teller(inner_key, encrypted_message_1)
        # ha lehet, ezt írd már át arra, hogy legyen egyenlő az utolsó szóköz utáni résszel
        inner_piece = [i for i in inner_message_1 not in message_1]
        inner_word_list = word_guesser(inner_piece)
        if len(inner_key == encrypted_message_2):
            return inner_key, inner_message_1, inner_message_2
        else:
            nemtom(inner_word_list, inner_piece, inner_message_2, inner_message_2, encrypted_message_1, encrypted_message_2)

        # adjuk vissza a kulcsot is
        # hogy adjak vissza több kulcsot?


def piece_teller(message, encrypted_message):
    char_set = string.ascii_lowercase + ' '
    encrypted_message_num = num_gen(encrypted_message) # visszaadja az encrypted message betűit számokban
    message_num = num_gen(message) # visszaadja a word betűit számokban
    new_message_num = [(encrypted_message_num[i] - message_num[i]) % 27 for i in range(len(message_num))]
    return [char_set[i] for i in new_message_num]


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



