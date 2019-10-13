# ask user for a string
hold_user_info = input(" please enter a sting to copy : ")
# convert string to upper
hold_user_info = hold_user_info.upper()

# convert string into a list
hold_user_info = hold_user_info.split()

# Cycle though the list
for words in hold_user_info:
    print(words[0], end="")
print()
