Console.WriteLine("Enter your name:"); //Asks the user for their name.
string name = Console.ReadLine(); //Applies the users input to the Name string.
Console.WriteLine("Enter your age"); //Asks the user for their age
int age = int.Parse(Console.ReadLine()); //Applies the input to the age int.
Console.WriteLine("Enter your height in meters:"); //Asks the user for their height.
double height = double.Parse(Console.ReadLine()); //Tracks their height
Console.WriteLine("Are you a student? (Yes/No):"); //Asks whether the user is a student or not
string student = Console.ReadLine(); //Records the response for line 9
bool isStudent = student == "Yes"; //If the user typed Yes, then line 9 records it as True.
Console.WriteLine($"Based on this information {name}, you are {age} years old, {height} meters tall and it is {isStudent} that you are a student. You will turn {age + 5} in 5 years.");
//Line 11: Spits out a premade message that changes multiple variables based on your inputs.
