def ascii_codes(a_string):
    
    L = []
    
    for character in a_string:
        print(f'{character}: {ord(character)}')
        L.append(ord(character))
    
    print(f'List of codes for the given string: {L}')
    
    s = ''
    
    for code in L:
        s += chr(code)  
    
    print(f'The original string is: \'{s}\'')

def main():
    ascii_codes(input('Enter a string: '))

if __name__ == '__main__':
    main()