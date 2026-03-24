print("Toady we are learning function in python")
def greet(name):
    print("hello" + name + "!")

greet("sahara")
greet("neha")

def abc(number):
    print(str( number ) + "!")

abc(2)   
abc(4) 
# function to check even or odd
def check_even_odd(number):

  if number % 2 == 0:
    print( number,"is even")    
  else:
    print(number,"is odd")   
    
check_even_odd(2)    
check_even_odd(3)

def table(n):
   for i in range(1,11):
      print(n*i)
# call a function
table(2) 
table(3) 

def square(num):
   print(num*num)
# call the function
square(3)
square(2)

def sum(a,b):
   print(a+b)

# call the function
sum(3,5)
sum(4,8)

def compare_number(a,b):
    if a>b:
       print(a," is bigger than ",b)
    elif a<b:
       print(b," is bigger than ",a)  
    else:
       print(a,"and",b,"are both equal")   
compare_number(3,3)
compare_number(9,3)        
compare_number(3,8)        

   

 