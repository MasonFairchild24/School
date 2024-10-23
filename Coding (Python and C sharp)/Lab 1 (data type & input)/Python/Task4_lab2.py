name = input("Enter your name:") #Asks for the user's name and saves it under the variable "name"
age = int(input("Enter your age:")) #Asks for the users age and saves it under the variable "age"
height = float(input("Enter your height in meters:")) #Asks for the users height and saves it under the "height" variable
student = input("Are you a student? (Yes/No):").lower() #Asks a yes or no question about if the user is a student, saves it under the variable student in all lowercase (.lower())
isStudent = student == "yes" #This checks their answer to "Are you a student", and puts true/false in the final statement depending on the answer.
print(f"Hello {name}, you are {height} meters tall, it is {isStudent} that you are in school. You will be {age + 5} in 5 years.")
#Prints a premade message and inserts the saved variables from above.
