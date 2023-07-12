# Daniel De Oliveira

def encode(password):
    encoded_password = ''
    for i in password:
        encoded_password += str(int(i) + 3)
    return encoded_password

def decode(encoded_password):
    ...

def main():
    menu_str = '\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n'

    menu_choice, decoded_password, encoded_password = '', '', ''
    while menu_choice != '3':
        print(menu_str)
        menu_choice = input('Please enter an option: ')
        
        if menu_choice == '1':
            encoded_password = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!\n')
        elif menu_choice == '2':
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')


if __name__ == '__main__':
    main()