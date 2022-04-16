import string


def decoder(word, encrypted_message_word_s, encrypted_message_other):
    message_1 = word + ' '
    key = piece_teller(message_1, encrypted_message_word_s)
    piece = piece_teller(key, encrypted_message_other)
    word_list = word_guesser(piece)
    message_2 = ''.join(piece)
    print(decoding_cycle(piece, word_list, message_2, encrypted_message_word_s, encrypted_message_other))


def decoding_cycle(piece, word_list, message_lesser_known, encrypted_message_more, encrypted_message_less):
    for x in word_list:
        inner_message_2 = message_lesser_known + x.replace(''.join(piece), '') + ' '
        inner_key = piece_teller(inner_message_2, encrypted_message_less)
        inner_message_1 = ''.join(piece_teller(inner_key, encrypted_message_more))
        inner_piece = ''.join([i for i in inner_message_1.split(' ')[-1]])
        inner_word_list = word_guesser(inner_piece)
        if len(inner_key) == len(encrypted_message_less):
            return inner_key, inner_message_1, inner_message_2.strip()
        else:
            if not inner_word_list:
                pass
            else:
                decoding_cycle(inner_piece, inner_word_list, inner_message_1, encrypted_message_less, encrypted_message_more)


def word_guesser(word_piece):
    vocabulary = open('words.txt', 'r')
    wordlist = []
    for i in vocabulary:
        if i.startswith(word_piece):
            wordlist.append(i.strip())
    return wordlist


def piece_teller(m_k, encrypted_message):
    char_set = string.ascii_lowercase + ' '
    encrypted_message_num = num_gen(encrypted_message)
    message_num = num_gen(m_k)
    new_message_num = [(encrypted_message_num[i] - message_num[i]) % 27 for i in range(len(message_num))]
    return [char_set[i] for i in new_message_num]


def num_gen(text):
    char_set = string.ascii_lowercase + ' '
    return [char_set.index(i) for i in text]
