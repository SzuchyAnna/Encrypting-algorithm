The file: Feladatleírás.txt is the original description of this excercise in Hungarian. What the code does, can be found in this README in detail.


This is a Python Class that gets a message and encodes it. It can also decode a message (with method decrypter) based on the same principals (see in num_gen).


WARNING: Can be used only with English alphabetic messages that might have space in it.


constructor:

When instantiated, receives a message that it stores as an instance variable. It also generates a key and encodes the message with it using its key_gen 
(see below) and encrypter (see below) methods and stores them for later decoding.



char_set: The class has a variable called char_set. This is a string that contains all the allowed characters starting from a to space (see why in num_gen).
It is used at multiple points in the code also it won't change therefore I thought I should make it a class variable.



key_gen(self)

Generates a random key based on the characters in char_set (see above) the lenght of the message. Returns a String.



num_gen(self, text)

Generates a list of numbers modulo 27 of letters, based on char_set (see above), where a is 0, b is 1, ... z is 25 according to english lowercase letters, and space equals to 26.
It can not work with uppercase or non-English alphabetic letters or special characters, numbers  because this exercise says so. It can be used externally too if needed,
therefore one has to give it the useable text manually.



encrypter(self)

Since it calles the instance's own key, it is only useable inside the object. It gives the numeric value of both the message and the key using num_gen (see above) and then returns 
the sum of them modulo 27. The encrypted message will be a list.



decrypter(self, encrypted_message, key)

It is meant to be used on another message that has already been encrypted, therefore one has to give the message and the key too manually. It uses the same
principals as encrypter, just backwards, to give back the original message as a String.