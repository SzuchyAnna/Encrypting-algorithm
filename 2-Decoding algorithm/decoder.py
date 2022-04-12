import string


def decoder(word, encrypted_message_1, encrypted_message_2):
    # char_set = string.ascii_lowercase + ' '
    # először a word az lesz, hogy early
    key = piece_teller(word, encrypted_message_1)  # ez most egy list
    piece = piece_teller(key, encrypted_message_2)  # ez most egy list
    # ez az első szótöredékünk
    # a piece egy újraírandó lista, ami mindig ahhoz tartalmaz üzenetrészt, hogy kitaláljuk a key következő részét
    word_list = word_guesser(piece)  # megkapjuk az első potenciális szavait a 2. üzenetnek


def nemtom(word_list, piece, encrypted_message_1, encrypted_message_2):
    for x in word_list:
        piece = x.replace(''.join(piece), '') + ' '
        key_piece = piece_teller(piece, encrypted_message_1)
        piece = piece_teller(key_piece, encrypted_message_2)
        inner_word_list = word_guesser(piece)
        # ha vége az üzeneteknek, akkor lépjünk ki
        # adjuk vissza a kulcsot is 


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



