from random import choices
import string


class Encrypter:
    def __init__(self, message):
        self.message = message

    # encrypt_set = string.ascii_lowercase + ' '

    def key_gen(self):
        n = len(self.message)
        return ''.join(choices(string.ascii_lowercase + ' ', k=n))

    def num_gen(self):
        encrypt_set = string.ascii_lowercase + ' '
        return []

    def encrypter(self):
        pass

    def input_tester(self):
        # a-z + szóköz
        # String
        pass