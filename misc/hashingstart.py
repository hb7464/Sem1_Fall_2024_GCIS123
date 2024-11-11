def set_hashing(aset):
    print(f'Recieved Set: {aset}')
    print(hash(34))
    for item in aset:
        print(f'{item} has hash value: {hash(item)}')

def main():
    seta = {1,34,3,21,333}
    set_hashing(seta)

if __name__ == '__main__':
    main()