from random import choices
import string

n = 20
encrypt_set = string.ascii_lowercase + ' '
# encrypt_set TÍPUSA STRING

# print("'" + encrypt_set + "'")
# print("'" + ''.join(choices(encrypt_set, k=n)) + "'")
# print ("this is a string with 'quotes'")
# print('this is a string with "quotes"')

# IGEN, A SZÓKÖZT IS BELERAKJA
# print("'" + ''.join(choices(string.ascii_lowercase + ' ', k=n)) + "'")

message = 'ahello world'
# print([i for i in message])
# print([i in encrypt_set for i in message])
print([encrypt_set.index(i) for i in message])
# print(encrypt_set[message[2]])
