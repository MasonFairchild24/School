Console.WriteLine("Enter a Number:"); //Asks for the user to input a number
double num1 = double.Parse(Console.ReadLine()); //Saves the number the user inputting, I did double since it didn't specify it had to be whole.
Console.WriteLine("Enter another Number:"); //Asks the user for another number
double num2 = double.Parse(Console.ReadLine()); //Saves the second number. 
Console.WriteLine($"According to you inputs, your lucky numbers are {num1 + num2}, {num1 - num2}, {num1 * num2}, and {num1 / num2}");
//Line 5 is a premade message that then spits out the sum, difference, product, and quotient of the 2 numbers.