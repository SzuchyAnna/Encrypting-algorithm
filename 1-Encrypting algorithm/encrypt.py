from random import choices
import string


class Encrypter:
    def __init__(self, message):
        self.message = message
        self.key = self.key_gen()
        self.encrypted_message = self.encrypter()

    char_set = string.ascii_lowercase + ' '

    def key_gen(self):
        n = len(self.message)
        return ''.join(choices(self.char_set, k=n))

    def num_gen(self, text):
        # char_set = string.ascii_lowercase + ' '
        return [self.char_set.index(i) for i in text]

    def encrypter(self):
        message_num = self.num_gen(self.message)
        key_num = self.num_gen(self.key)
        return [(message_num[i] + key_num[i]) % 26 for i in range(len(message_num))]

    def decrypter(self, encrypted_message, key):
        encrypted_message_num = self.num_gen(encrypted_message)
        key_num = self.num_gen(key)
        message_num = [(encrypted_message_num[i] - key_num[i]) % 26 for i in range(len(encrypted_message_num))]
        return ''.join([self.char_set[i] for i in message_num])

    def input_tester(self):
        # a-z + szóköz
        # String
        pass
