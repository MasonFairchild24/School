Console.WriteLine("Enter your age:"); //Asks the user for their age
int age = int.Parse(Console.ReadLine()); //inputs the users age as the variable "Age"
bool isAdult = age >= 18; //Checks to see if the user is above 18
Console.WriteLine($"It is {isAdult} that you are legally an adult.");
// Line 4 spits out a premade message that changes from True to false depending on whether "isAdult" is true or false.
