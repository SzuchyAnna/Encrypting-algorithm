import string


char_set = string.ascii_lowercase + ' '


def decoder(word, words_encrypted_message, other_encrypted_message):
    message_1 = word + ' '
    key = piece_teller(message_1, words_encrypted_message)
    piece = piece_teller(key, other_encrypted_message)
    word_list = word_guesser(piece)
    message_2 = ''.join(piece)
    print(decoding_cycle(piece, word_list, message_2, words_encrypted_message, other_encrypted_message))


def decoding_cycle(piece, word_list, lesser_known_message, encrypted_message_more_known, encrypted_message_lesser_known):
    for x in word_list:
        inner_message_2 = lesser_known_message + x.replace(''.join(piece), '') + ' '
        inner_key = piece_teller(inner_message_2, encrypted_message_lesser_known)
        inner_message_1 = ''.join(piece_teller(inner_key, encrypted_message_more_known))
        inner_piece = ''.join([i for i in inner_message_1.split(' ')[-1]])
        inner_word_list = word_guesser(inner_piece)
        if len(inner_key) == len(encrypted_message_lesser_known):
            return inner_key, inner_message_1, inner_message_2.strip()
        else:
            if not inner_word_list:
                pass
            else:
                decoding_cycle(inner_piece, inner_word_list, inner_message_1, encrypted_message_lesser_known, encrypted_message_more_known)


def word_guesser(word_piece):
    vocabulary = [i.strip() for i in open('words.txt', 'r')]
    wordlist = []
    for i in vocabulary:
        if i.startswith(''.join(word_piece)):
            wordlist.append(i)
    return wordlist


def piece_teller(m_or_k_piece, encrypted_message):
    encrypted_message_num = num_gen(encrypted_message)
    message_num = num_gen(m_or_k_piece)
    new_message_num = [(encrypted_message_num[i] - message_num[i]) % 27 for i in range(len(message_num))]
    return [char_set[i] for i in new_message_num]


def num_gen(text):
    return [char_set.index(i) for i in text]
