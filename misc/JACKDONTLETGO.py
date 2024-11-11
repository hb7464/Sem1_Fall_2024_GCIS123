adict = {'and I':2, 'EIIIIIII':3,'WILLL ALWAYYYYYYYYS':1,'LOOOOOOOOVE':5,'YOOOOOOOOU':5}

value = adict['EIIIIIII']

def check_first(adict,key):
    import time
    st= time.perf_counter_ns()
    if key in adict:
        value = adict[key]
        print(value)
    end = time.perf_counter_ns()
    print(end-st)
def main():
    check_first(adict,'EIIIIIII')
    check_first(adict,'de')

if __name__ == '__main__':
    main()