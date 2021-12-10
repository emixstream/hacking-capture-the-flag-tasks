#!/usr/bin/env pyhton

import collections
import string
import itertools


#lowercase = collections.deque( string.lowercase + string.digits)

message = 'ATTACKATDOWN'
key = 'LEMON'

def encrypt( message, key):
	compressed_message = message.lower()

	for punctuation in str(string.punctuation + ' '):
		compressed_message = compressed_message.replace(punctuation, '')


	cycler = itertools.cycle( key.lower())
	long_key = ''.join([ cycler.next() for _ in range(len(compressed_message))])

	coded = []
	for number in range(len(long_key)):
		cipher_letter = compressed_message[number]
		key_letter = long_key[number]
		key_index = string.lowercase.index(key_letter)
		cipher_index = string.lowercase.index(cipher_letter)

		lowercase = collections.deque(string.lowercase)
		lowercase.rotate(key_index)
		new_alphabet = ''.join(list(lowercase))
		new_character = new_alphabet[cipher_index]
		coded.append(new_character)

	return ''.join(coded)


def decrypt(message, key):
	return encrypt(message, key)

	#, 1


print decrypt(encrypt(message, key), key)







