# write a python program to translate the message into the code language Use the rules below
import random
import string

a = input("enter the string")

our_string = a.lower()

# this is for coding the message

# if not our_string:
#     print("please enter the string ")
#     exit()
# else:
#     if len(our_string)>3 :
#         max_index=len(our_string)
#         updated_string=our_string[1:max_index]+our_string[0]
#         print(updated_string)
#         random_chars1=''.join(random.choices(string.ascii_lowercase, k=3))
#         random_chars2=''.join(random.choices(string.ascii_lowercase, k=3))
#         updated_string=random_chars1+updated_string+random_chars2
#         print(updated_string)
#     else:
#         print(our_string[::-1])

# this is for decoding the message

if not our_string:
    print("please enter the string to decode ")
    exit()
else:
    if len(our_string) < 3:
        print(our_string[::-1])
    else:
        our_modified_string = our_string[3:-3]
        print(our_modified_string)
        last_letter = our_modified_string[-1]
        print(last_letter)
        print(last_letter + our_modified_string[:-1])
