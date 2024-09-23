'''def countdown(number):
  sm=0
  while number > 0:
    sm+=number
    print(number)
    number-=1
  print("Sum:"+str(sm))

def countup(number):
  c=0
  sm=0
  while c < number:
    sm+=c
    print(c)
    c+=1
  print("Sum:"+str(sm))
  
def main():
  n = int(input("Enter a number: "))
  countdown(n)
  countup(n)
  
main()'''

def printeven():
  times = 2
  while times <=10:
    if times%2 == 0:
      print(times)
    times+=1

def main():
  printeven()
  
main()