def set_hashing(aset):
    print(f'Recieved Set: {aset}')
    print(hash(34))
    for item in aset:
        print(f'{item} has hash value: {hash(item)}')

def main():
    seta = {1,34,3,21,333} #Doesn't work since the values are integers instead of literally anything else
                            #Put something like strings inside it and it will return an actual hash
    set_hashing(seta)

if __name__ == '__main__':
    main()