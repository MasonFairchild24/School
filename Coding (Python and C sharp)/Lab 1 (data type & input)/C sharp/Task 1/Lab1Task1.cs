Console.WriteLine("Enter your name:"); //Asks for the user's name
string name = Console.ReadLine(); //Saves the username in the variable "name"
Console.WriteLine("Enter your age:"); //Asks the user for their age.
int age = int.Parse(Console.ReadLine()); //Saves the user's age as an int
Console.WriteLine("Enter your height in meters: "); //Asks the user for their height in meters
double height = double.Parse(Console.ReadLine()); //Saves the users height in meters, Double since it can be decimals.
Console.WriteLine($"Hello {name}, you are {height} meters tall and {age} years old"); //Writes a premade message with the user's inputted information.

