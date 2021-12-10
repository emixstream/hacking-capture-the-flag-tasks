

from string import uppercase

numbers = '07271978'

flag = []
with open('message.txt') as handle:
	message = handle.read()

counter = 0
for character in message:
		character = character.upper()

		if (character in uppercase) :
			index = uppercase.index(character)
			offset =int(numbers[counter % len(numbers)])
			new_character = uppercase[index - offset]
			flag.append(new_character)
			counter += 1
		else:
			flag.append(character)

print ''.join(flag)
