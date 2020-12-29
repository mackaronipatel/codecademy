alphabet_soup = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! '"
nikhil_message = "y belu dyaxyb q bej, qdt y adem xu yi co fuhied veh uluh qdt uluh."
decoded_message = ''

for letter in nikhil_message:
    if not letter in punctuation:
        letter_value = alphabet_soup.find(letter)
        decoded_message += alphabet_soup[(letter_value + 10) % 26]
    else:
        decoded_message += letter
print(decoded_message)

mack_message = "i love nikhil a lot, and i know he is my person for ever and ever."
alphabet_soup = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! '"
sappy_message_coded = ' '

for letter in mack_message:
    if not letter in punctuation:
        letter_value = alphabet_soup.find(letter)
        sappy_message_coded += alphabet_soup[(letter_value - 10) % 26]
    else:
        sappy_message_coded += letter
print(sappy_message_coded)