using System;

class Program
{
    public static void Main() //Defines the main, I will be honest this took a bit to figure out just because the Using system and class project.
    {
        Greet(); 
        GreetUser("Mason"); 
        AddNumbers(4, 3);
        CalculateArea(5);
        FindMax(1,2,3); //This should do all the decimals/float/etc aswell, didn't know if you wanted us to print the results so left it for input.
        GreetWithDefault();
        GreetWithDefault("Randy");
        //Lines 7-13 run the various methods throughout the code.
    }


public static void Greet() 
{ 
    Console.WriteLine("Hello, world!"); //Just writes hello World when called.
}

public static void GreetUser(string name)
{
    Console.WriteLine($"Hello, {name}"); //Says hello to whatever name is inputted into the argument
}

public static void AddNumbers(int num1, int num2)
{
    Console.WriteLine(num1+num2); //Adds the two numbers that are input into the argument when it is called.
}

public static void CalculateArea(float radius)
{
    Console.WriteLine((radius*radius)*3.14159); //This Multiplies the radius by itself (For squared) and then multiplies it by the simplified version of π for the circumfrence.
}

public static void FindMax(int num1, int num2, int num3)
{
    if (num1 >= num2 && num1 >= num3)
        Console.WriteLine(num1);
    else if (num2 >= num1 && num2 >= num3)
        Console.WriteLine(num2);
    else if (num3 >= num1 && num3 >= num2)
        Console.WriteLine(num3);
}
//These all determine whether the inputted numbers are greater than each other. Incase the user puts the same number twice, >= ensures the largest is still displayed
//Lines 49-102 all just allow the user to input numbers with varying amounts of decimals.
public static void FindMax(decimal num1, decimal num2, decimal num3)
{
    if (num1 >= num2 && num1 >= num3)
        Console.WriteLine(num1);
    else if (num2 >= num1 && num2 >= num3)
        Console.WriteLine(num2);
    else if (num3 >= num1 && num3 >= num2)
        Console.WriteLine(num3);
}
public static void FindMax(double num1, double num2, double num3)
{
    if (num1 >= num2 && num1 >= num3)
        Console.WriteLine(num1);
    else if (num2 >= num1 && num2 >= num3)
        Console.WriteLine(num2);
    else if (num3 >= num1 && num3 >= num2)
        Console.WriteLine(num3);
}
public static void FindMax(float num1, float num2, float num3)
{
    if (num1 >= num2 && num1 >= num3)
        Console.WriteLine(num1);
    else if (num2 >= num1 && num2 >= num3)
        Console.WriteLine(num2);
    else if (num3 >= num1 && num3 >= num2)
        Console.WriteLine(num3);
}
public static void FindMax(long num1, long num2, long num3)
{
    if (num1 >= num2 && num1 >= num3)
        Console.WriteLine(num1);
    else if (num2 >= num1 && num2 >= num3)
        Console.WriteLine(num2);
    else if (num3 >= num1 && num3 >= num2)
        Console.WriteLine(num3);
}
public static void FindMax(short num1, short num2, short num3)
{
    if (num1 >= num2 && num1 >= num3)
        Console.WriteLine(num1);
    else if (num2 >= num1 && num2 >= num3)
        Console.WriteLine(num2);
    else if (num3 >= num1 && num3 >= num2)
        Console.WriteLine(num3);
}
public static void FindMax(byte num1, byte num2, byte num3)
{
    if (num1 >= num2 && num1 >= num3)
        Console.WriteLine(num1);
    else if (num2 >= num1 && num2 >= num3)
        Console.WriteLine(num2);
    else if (num3 >= num1 && num3 >= num2)
        Console.WriteLine(num3);
}

public static void GreetWithDefault(string name = "Guest")
{
    Console.WriteLine($"Hello, {name}");
}
//This just says hello to the guest if they dont input a name and says "Hello ___" if they put their name.
}