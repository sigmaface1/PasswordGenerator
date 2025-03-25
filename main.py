import random
import string


char_list = list(string.ascii_letters + string.digits)
print(len(char_list))

password = []
i = int(input("Количество символов: "))
b = i

while i < b * 2 :
    num = random.randrange(0, 62 )
    password += char_list[num]
    i += 1

print("".join(password))