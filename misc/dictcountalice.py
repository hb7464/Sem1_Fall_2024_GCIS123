def count_words():

    word_dict = {}
    filename = r'hb7464\misc\alice.txt'
    # filename = input('Enter file path:')
    with open(filename) as file:
       
        for line in file:
            words = line.split()
       
            for word in words:
                word_without_special_characters_or_digits = ''
       
                for letter in word:
       
                    if letter.lower() in 'qwertyuiopasdfghjklzxcvbnm':
                        word_without_special_characters_or_digits += letter
       
                if word_without_special_characters_or_digits in word_dict:
                    word_dict[word_without_special_characters_or_digits] += 1
       
                else:
                    word_dict[word_without_special_characters_or_digits] = 1
    
    return word_dict

def main():
    word_dict = count_words()

    for i in word_dict:
        print(f'{i}: {word_dict[i]}')

if __name__ == '__main__':
    main()