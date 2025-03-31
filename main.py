import secrets
import string


def input_symbols_count():
    symbols_count = int(input("Количество символов: "))
    return symbols_count

def check_symbols_count(symbols_count):
    if symbols_count < 8:
        print("Количество символов должно быть больше 8")
        return input_symbols_count()
    return symbols_count


def char_list():
    letters_choice = input("Использовать заглавные буквы? (y/n): ").lower()
    lower_letters_choice = input("Использовать строчные буквы? (y/n): ").lower()
    numbers_choice = input("Использовать цифры? (y/n): ").lower()
    
    chars = ""
    
    if letters_choice == "y":
        chars += string.ascii_uppercase
    if lower_letters_choice == "y":
        chars += string.ascii_lowercase
    if numbers_choice == "y":
        chars += string.digits
        
    if not chars:
        print("Выберите хотя бы один тип символов")
        return char_list()
        
    return list(chars)



def generate_password(symbols_count, char_list):
    password = []
    for _ in range(symbols_count):
        password.append(secrets.choice(char_list))
    return "".join(password)

if __name__ == "__main__":
    symbols_count = input_symbols_count()
    symbols_count = check_symbols_count(symbols_count)
    print(generate_password(symbols_count, char_list()))