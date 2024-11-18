class PythonCode:
    def __init__(self):
        self.gcis = 'GCIS123'
    
    def print_gcis(self):
        print(self.gcis)
        
def main():

    obj1 = PythonCode()
    obj2 = PythonCode()
    obj1.print_gcis()
    obj2.print_gcis()

if __name__ == '__main__':
    main()