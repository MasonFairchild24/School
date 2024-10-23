def main():
    welcome()
    greet_user('Mason')
    add_numbers(3, 8)
    calculate_area(5)
    find_max(6, 8, 3)
    greet_with_default()
    greet_with_default('Randy')
#Lines 2-8 just call the methods created below.


def welcome(): 
   print("Welcome to the Python Functions Lab!") #Prints the text

def greet_user(name):
    print("Hello, " + name) #Just creates a method that makes the argument a name that is then used to say hello to.


def add_numbers(num1, num2):
    print(num1 + num2) #Same as the greet_user method but adds the two inputs

def calculate_area(radius):
    print(radius*radius * 3.14159) #Multiplies the inputted radius by itself then by Pi

def find_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        largest=num1
    elif num2 >= num1 and num2 >= num3:
        largest=num2
    elif num3 >= num2 and num3 >= num1:
        largest=num3
    print(largest)
#This takes the numbers inputted and compares them to one another to see which is the largest. If 2 numbers are the largest, it will still output the largest (This is why i did >= )

def greet_with_default(name='Guest'):
    print('Hello, '+ name) #Writes out "Hello guest" unless an argument is entered which overrides the guest with the inputted argument.


main()