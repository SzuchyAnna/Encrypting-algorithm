from random import choices
import string

n = 20
# encrypt_set = string.ascii_lowercase + ' '
# print("'" + encrypt_set + "'")
# print("'" + ''.join(choices(encrypt_set, k=n)) + "'")
# print ("this is a string with 'quotes'")
# print('this is a string with "quotes"')
print("'" + ''.join(choices(string.ascii_lowercase + ' ', k=n)) + "'")
