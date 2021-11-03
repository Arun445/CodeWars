def find_letter_upper(number):
    for times in range(13):
        if number < 90:
            number += 1
        else:
            number = 65
    return number


def find_letter_lower(number):
    for times in range(13):
        if number < 122:
            number += 1
        else:
            number = 97
    return number


def rot13(message):
    rot13_message = []
    message_split = [(letter) for letter in message]
    for letter in message_split:
        letter_to_number = ord(letter)
        if letter_to_number >= 65 and letter_to_number <= 90:
            if letter_to_number + 13 >= 90:

                rot13_message.append(chr(find_letter_upper(letter_to_number)))
            else:
                rot13_message.append(chr(letter_to_number+13))
        elif letter_to_number >= 97 and letter_to_number <= 122:
            if letter_to_number + 13 >= 122:

                rot13_message.append(chr(find_letter_lower(letter_to_number)))
            else:

                rot13_message.append(chr(letter_to_number+13))
        else:
            rot13_message.append(letter)

    return ''.join(rot13_message)
