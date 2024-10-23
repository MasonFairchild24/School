name = input("Please enter your name: ") #Prompts the user to enter their name and saves it under "Name"
age = int(input("Enter your age: ")) #Saves the user's name/input under "age"
height = float(input("Enter your height in meters: ")) #Saves the users height under "height" allowing them to put a decimal in the number.
isStudent = input("Are you a student? (Yes/No):") #Asks the user if they are a student (yes or No) and saves the response.
if isStudent.lower() == "yes": #This checks the previous answer (yes/No) and lowercases it. If it is "yes" it prints line 6.
    print(f"Hello {name}, you are a student that is {age} years old and you stand at {height} meters tall") #prints out the premade message with the inputs from the user.
elif isStudent.lower() == "no": #This checks the answer on line 4 and lowercases it. If it is "no" it prints line 8
    print(f"Hello {name}, you are {age} years old, stand at {height} meters tall, and you are not a student.") #prints out the premade message with the inputs from the user.
    
    
#Both the If/Elif and .lower were learnt on StackOverflow https://stackoverflow.com/questions/26695649/creating-if-else-statements-dependent-on-user-input#
# Attempted to make this using the lab sheet, however I did not understand the boolean part and couldn't get it to work which led to the If and Elif statements. 