import random
import string


def generate_password():
    char_list = list(string.ascii_letters + string.digits)
    char_list_len = len(char_list)

    password = []
    symbols_count = int(input("Количество символов: "))
    symbols_count_2 = symbols_count

    while symbols_count > 0:
        num = random.randrange(0, char_list_len)
        password += char_list[num]
        symbols_count -= 1

    print("".join(password))

if __name__ == "__main__":
    generate_password()