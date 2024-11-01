def rgb_tuple():
    import random
    red = random.random()
    green = random.random()
    blue = random.random()
    return red,green,blue

def main():
    for i in range(3):
        print(f'{i+1}: {rgb_tuple()}')

if __name__ == '__main__':
    main()