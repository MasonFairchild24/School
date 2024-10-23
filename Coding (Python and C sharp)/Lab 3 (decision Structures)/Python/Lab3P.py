def main():
    evenOrOdd()
    greaterThan()
    posNegZer()
    letterCase()
    divisFunct()
    ageGroup()
    checkLeap()
    gradeFunct()
    rangeCheck()
    strLength()
    triangleType()
    passwordStrength()
    palindromeCheck()
    dayOfWeek()
    taxBracket()

#Some of these are inputs and some don't. I started working on this at one time then had to stop for a while so some may be coded differently just depending on what I felt was better.


def evenOrOdd():
    number = int(input("Please enter a number:"))
    if number % 2 == 0: #Checks to see if th einputted number can be evenly divided by 2, if it can it is an even number.
        print(f"{number} is even")
    else:
        print(f"{number} is odd") #if it is not divisable by 2, it states that it is an odd number.

def greaterThan():
    num1 = int(input("Please enter your first number:"))
    num2 = int(input("Please enter your second number:"))
    if num1 == num2:
        print("These numbers are equal to one another") #Just checks to see if the numbers are the exact same
    elif num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1: #Line 30 and 32 check to see if one number is greater than the other and then prints the correct response.
        print(f"{num2} is greater than {num1}")

def posNegZer():
    num1 = int(input("Please enter a number:"))
    if num1 == 0: #Just checks to see if the number is 0, if so it is neither negative or positive since it is nothing
        print("zero")
    elif num1 > 0: #Checks to see if the number is greater than 0, if so it is positive
        print(f"{num1} is positive") 
    elif num1 < 0: #Checks to see if the number is less than 0, if so it is negative
        print(f"{num1} is Negative")


def letterCase():
    letter = input("Please enter a letter:")
    if letter == letter.lower(): #Converts the letter to lowercase for half the equation to see if it matches the users input. If it does, it proves that the letter is lowercase.
        print(f"{letter} is lowercase")
    elif letter == letter.upper(): #Does the same as line 45, however checks to see if it is uppercase.
        print(f"{letter} is uppercase")
    else:
        print(f"{letter} is neither upper or lowercase.") #This is used just incase a user inputs a value that is not a letter.

def divisFunct():
    num1 = int(input("Please enter a number: "))
    while num1 == 0:
        num1 = int(input("Please enter another number: ")) #This ensures that the user does not put 0, prevents divide by 0.
    if num1 % 3 == 0 and num1 % 5 == 0:
        print(f"{num1} is evenly divisable by 3 and 5") #This checks to see if the number can be divided by 3 and 5 without a remainder.
    elif num1 % 3 == 0:
        print(f"{num1} is evenly divisable by 3") #If it can not be divided by both 3 and 5 evenly, lines 58 and 60 check to see if it can be divided by one or the other without a remainder.
    elif num1 % 5 == 0:
        (f"{num1} is evenly divisable by 5")
    else:
        print(f"{num1} is unable to be divided by 3 or 5 evenly.")

def ageGroup(): #This function just recieves an age and then uses if statements to see if it falls between varying ranges. It then displays a message depending on the range it is in.
    age = int(input("Please enter your age:"))
    if age >= 65:
        print("You are a senior.")
    elif age >= 20:
        print("You are an adult.")
    elif age >= 18:
        print("You are a teenager and an adult.")
    elif age >= 13:
        print("You are a teenager.")
    elif age >= 0:
        print("You are a child.")
    else:
        print("You haven't been born yet.")

def checkLeap():
    Leapyear = int(input("Please enter a year:"))
    if Leapyear % 4 == 0: #This takes the users input and divides it by four since every year can be divided by 4.
        print(f"{Leapyear} is a leapyear")
    else:
        print(f"{Leapyear} is not a leapyear")

grade = "F"
def gradeFunct():
    grade = float(input("Enter your current number grade: ")) #This entire function is basically the same as the age function. It just checks the highest and goes down the line to determine the maximum range it can fit in.
    if grade >= 90 and grade <= 100:
        print("Your grade is an A")
    elif grade >= 80:
        print("Your grade is a B")
    elif grade >= 70:
        print("Your grade is a C")
    elif grade >= 60:
        print("Your grade is a D")
    elif grade >=0:
        print("Your grade is an F")



def rangeCheck():
    lowerRange = float(input("Enter your lower range: "))
    upperRange = float(input("Enter your upper range: "))
    number = float(input("Enter the number you want to check: ")) #Lines 102-104 just ask the user for the lower range, upper range, and number they want to check
    if number >= lowerRange and number <= upperRange: #This just checks to see if the number is between input 1 and input 2 (The lower and upper ranges)
        print(f"{number} is between {lowerRange} and {upperRange}") 
    else:
        print(f"{number} is not between {lowerRange} and {upperRange}")


def strLength():
    stringOne = input("Please type anything: ")
    stringTwo = input("Please type something else: ")
    if len(stringOne) > len(stringTwo): #Len takes the length of each variable, which is then compared to one another in both if statements. Learnt on https://stackoverflow.com/questions/4967580/how-to-get-the-size-length-of-a-string-in-python
        print(f"'{stringOne}' is larger than '{stringTwo}'")
    elif len(stringTwo) > len(stringOne):
        print(f"'{stringTwo}' is larger than '{stringOne}'")

def triangleType():
    sideOne = float(input("Please enter the length of side 1: "))
    sideTwo = float(input("Please enter the length of side 2: "))
    sideThree = float(input("Please enter the length of side 3: "))
    if sideOne + sideTwo > sideThree and sideOne + sideThree > sideTwo and sideTwo + sideThree > sideOne: #In order to determine if the sides make a triangle, the code uses the Triangle Inequality Theorem (a+b>c, a+c>b< etc)
        if sideOne != sideTwo and sideOne != sideThree and sideTwo != sideThree: #Since a scalene triangle has no equal sides, this line checks to see if they are all the different
            print("These measurements create a scalene triangle")
        elif sideOne == sideTwo and sideOne == sideThree and sideTwo == sideThree: #This line just checks to see if they are all the same since equilateral triangles must have equal sides
            print("These measurements create an equilateral triangle")
        else:
            print("These measurements create an isosceles triangle.") #Since it was already confirmed to be a triangle, it has to be an isosceles if it is not equilateral or scalene.
    else:
        print("These measurements can not make a triangle.")

def passwordStrength():
    password = input("Please enter a password: ")
    number = any(char.isdigit() for char in password)  #https://stackoverflow.com/questions/41117733/validation-of-a-password-python
    alphabet = any(char.isalpha() for char in password) 
    special = any(not char.isalnum() for char in password) #Lines 135-137 check the characters of the password string. 
    if len(password) >= 8 and alphabet and number and special: #This determines if the password has 8 or more characters, a number, letter, and a special character.
        print("This is a strong password")
    elif (len(password) >= 6 and ((alphabet and number) or (alphabet and special) or (special and number))): #I used chatgpt on  this one just to see what an error was, just told me that I was missing a set of parenthesis.
        print("This is a moderate password.") #Line 140 checks to see if the password has atleast 6 characters and includes atleast one set of 2 differing characters.
    else:
        print("This is a weak password.")
    #https://www.w3schools.com/python/ref_string_isalpha.asp    I used W3 to figure out the .isalpha, isdigit, and isalnum.

def palindromeCheck():
    palindrome = input("Please enter a word to see if it is a palindrome:")
    if palindrome.lower() == palindrome.lower()[::-1]: #https://www.w3schools.com/python/python_howto_reverse_string.asp All this does is reverse the palindrome to see if it is the same.
        print(f"{palindrome.lower()} is a palindrome")
    else:
        print(f"{palindrome.lower()} is not a palindrome")

def dayOfWeek():
    import datetime
    dateQuest = input("Please enter a date(MM-DD-YYYY format):")  #For this one, I read like 20 different websites and chatGPT to try to understand it and I still don't completely understand it. 
    date = datetime.datetime.strptime(dateQuest, "%m-%d-%Y").date() #https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/ This was the most useful website
    dayName = date.strftime("%A")
    print(f"{dateQuest} is a {dayName}")

    
                

def taxBracket():
    bracket = int(input("Please insert your amount of income: $"))
    print("Based on the 2023 Federal Income Tax Brackets:")
    if bracket >= 578126:
        print("Your tax rate is 37% and you owe $", bracket * 0.37)  #Lines 169-181 just determine whether the amount of income fits between the certain tax brackets. When it finds what tax bracket it is in, it prints a response saying what percent you owe and the total amount you owe.
    elif bracket >= 231251:
        print("Your tax rate is 35% and you owe $", bracket * 0.35)
    elif bracket >= 182101:
        print("Your tax rate is 32% and you owe $", bracket * 0.32)
    elif bracket >= 95376:
        print("Your tax rate is 24% and you owe $", bracket * 0.24)
    elif bracket >= 44726:
        print("Your tax rate is 22% and you owe $", bracket * 0.22)
    elif bracket >= 11001:
        print("Your tax rate is 12% and you owe $", bracket * 0.12)
    elif bracket >= 0:
        print("Your tax rate is 10% and you owe $", bracket * 0.10)
main()
