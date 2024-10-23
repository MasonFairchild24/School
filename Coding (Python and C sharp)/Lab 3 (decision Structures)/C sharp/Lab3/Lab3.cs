using System;

class Program
{
    public static void Main() 
    {
        evenOrOdd(5);
        greaterThan(1,5);
        posNegZero(333);
        letterCase("A");
        divisFunct(15);
        ageGroup(10);
        leapYear(2004);
        gradeCheck(69);
        rangeCheck(6,92,37);
        length();
        triangle();
        passwordStrength();
        palindromeCheck();
        dayOfTheWeek();
        taxBracket();






    }



public static void evenOrOdd(int num1)
{
    if (num1 % 2 == 0) //Checks to see if the number is evenly divisable by two, if it is then it is even.
        Console.WriteLine($"{num1} is an even number");
    else
    
        Console.WriteLine($"{num1} is an odd number.");
    
}

public static void greaterThan(int num1, int num2)
{
    if (num1 == num2)
        Console.WriteLine($"{num1} is the same as {num2}"); //This just checks to see if the two numbers are equal to one another. If they aren't, it checks to see which is greater.
    else if (num1 > num2)
        Console.WriteLine($"{num1} is greater than {num2}");
    else if (num2 > num1)
        Console.WriteLine($"{num2} is greater than {num1}");
}

public static void posNegZero(int num1)
{
    if (num1 == 0)
        Console.WriteLine($"{num1} is the neither positive or negative"); //Checks to see if the number is equal to zero
    else if (num1 > 0)
        Console.WriteLine($"{num1} is a positive number"); //This and line 58 just check if the number is negative or positive.
    else if (0 > num1)
        Console.WriteLine($"{num1} is a negative number");
}

public static void letterCase(string Letter)
{
    char character = char.Parse(Letter);
    if (Char.IsUpper(character)) //Changes the string to a character for later use
        Console.WriteLine($"{Letter} is Uppercase"); //IsUpper is used to change the character to upper.
    else if (Char.IsLower(character))
        Console.WriteLine($"{Letter} is Lowercase"); //Does the same as line 66 but checks to see it is lower
}

public static void divisFunct(int num1)
{
    if (num1 == 0)
        Console.WriteLine("You can not divide 0."); //Checks if the number is 0 and if so prints this message.
    else if (num1 % 3 == 0 && num1 % 5 == 0)
        Console.WriteLine($"{num1} is evenly divisable by 3 and 5."); //Line 75 checks to see if the number is divisable by both 3 & 5
    else if (num1 % 3 == 0)
        Console.WriteLine($"{num1} is evenly divisable by 3"); //Line 77 checks to see if it is divisable by 3, is not it checks if it is divisable by 5.
    else if (num1 % 5 == 0)
        Console.WriteLine($"{num1} is evenly divisable by 5");
    else
        Console.WriteLine($"{num1} is not evenly divisable by 3 or 5");
}

public static void ageGroup(int age)
{
    if (age >= 65)
        Console.WriteLine("You are a senior"); //This entire function just checks an upper range and then goes down the list. If it is caught on one step it will print that response and stop the function.
    else if (age >= 20)
        Console.WriteLine("You are an adult.");
    else if (age >= 18)
        Console.WriteLine("You are a teenager and an adult");
    else if (age >= 13)
        Console.WriteLine("You are a teenager");
    else if (age >= 0)
        Console.WriteLine("You are a child");
    else if (age < 0)
        Console.WriteLine("You haven't even been born yet.");

}

public static void leapYear(int Year)
{
    if (Year % 4 == 0)
        Console.WriteLine($"{Year} is a Leapyear"); //This just checks to see if the inputted year is divisable by 4, if it is then it is a leapyear.
    else 
        Console.WriteLine($"{Year} is not a Leapyear");

}

public static void gradeCheck(int Grade)
{
    if (Grade >= 90 && Grade <=  100) //This is very similar to the age group task, it just takes an input and determines which category it fits in.
        Console.WriteLine("You have an A");
    else if (Grade >= 80)
        Console.WriteLine("You have a B.");
    else if (Grade >= 70)
        Console.WriteLine("You have a C");
    else if (Grade >= 60)
        Console.WriteLine("You have a D");
    else if (Grade >= 0)
        Console.WriteLine("You have a F");
    else
        Console.WriteLine("The grade you inputted is invalid, 0-100.");


}


public static void rangeCheck(int Lower, int Upper, int Number)
{
    if (Upper > Number && Number > Lower ) //This takes the lower and upper input and decides if the number is greater than the lower input and less than the higher input
        Console.WriteLine($"{Number} is between {Lower} and {Upper}");
    else
        Console.WriteLine($"{Number} is not between {Lower} and {Upper}");
    
}

public static void length() //https://stackoverflow.com/questions/2843987/array-size-length-in-c-sharp
{
    Console.WriteLine("Please type something:");
    string partOne = Console.ReadLine();
    Console.WriteLine("Please type something else:"); //These both just ask for the user to input a value
    string partTwo = Console.ReadLine();
    if (partOne.Length > partTwo.Length) //.Length just takes the length of the string
        Console.WriteLine($"{partOne} is longer than {partTwo}");
    else if (partOne.Length < partTwo.Length) //These both compare the lengths to see which is larger.
        Console.WriteLine($"{partTwo} is longer than {partOne}");
    else
        Console.WriteLine($"{partOne} and {partTwo} are equal in length.");
}

public static void triangle()
{
    Console.WriteLine("Please enter the length of side 1:");
    string sideOneString = Console.ReadLine();
    int sideOne = int.Parse(sideOneString);
    Console.WriteLine("Please enter the length of side 2:");
    string sideTwoString = Console.ReadLine();
    int sideTwo = int.Parse(sideTwoString);
    Console.WriteLine("Please enter the length of side 3:");
    string sideThreeString = Console.ReadLine();
    int sideThree = int.Parse(sideThreeString);
    if ((sideOne + sideTwo > sideThree) && (sideOne + sideThree > sideTwo) && (sideTwo + sideThree > sideOne)) //In order to determine if the sides make a triangle, the code uses the Triangle Inequality Theorem (a+b>c, a+c>b< etc)
        if ((sideOne != sideTwo) && (sideOne != sideThree) && (sideTwo != sideThree))//Since a scalene triangle has no equal sides, this line checks to see if they are all the different
            Console.WriteLine("These measurements create a scalene triangle.");
        else if ((sideOne == sideTwo) && (sideTwo == sideThree) && (sideOne == sideThree)) // This line just checks to see if they are all the same since equilateral triangles must have equal sides
            Console.WriteLine("These measurements create an equilateral triangle");
        else
            Console.WriteLine("These measurements create an isosceles triangle");  //Since it was already confirmed to be a triangle, it has to be an isosceles if it is not equilateral or scalene.
    else
        Console.WriteLine("These measurements can not make a triangle");

}

public static void passwordStrength()
{
    
    Console.WriteLine("Please enter a password:");
    string password = Console.ReadLine();

    int passwordLength = password.Length; 
    
        if ((passwordLength >= 8) && (password.Any(char.IsLetter)) && (password.Any(char.IsDigit)) && password.Any(c => !char.IsLetterOrDigit(c))) //I used ChatGPT for the Lambda function.
            {//#This determines if the password has 8 or more characters, a number, letter, and a special character.
               Console.WriteLine("This is a strong password");
            }
        else if ((passwordLength >= 6) && ((password.Any(char.IsLetter)) && (password.Any(char.IsDigit))) || ((password.Any(c => !char.IsLetterOrDigit(c))) && (password.Any(char.IsDigit))) || (password.Any(c => !char.IsLetterOrDigit(c)) && (password.Any(char.IsLetter))))
            {//This determines if the password has atleast 6 characters and 2 different characters.
                Console.WriteLine("This is a moderate password");
            }
        else
        {
           Console.WriteLine("This is a weak password");
        }
}

public static void palindromeCheck()
{
    Console.WriteLine("Please enter a word to see if it is a palindrome:");
    string palindrome = Console.ReadLine(); //https://wellsb.com/csharp/beginners/string-manipulation-reverse-string-csharp/
    string palin2 = palindrome.ToLower(); //https://www.programiz.com/csharp-programming/library/string/join
    char[] palArray = palin2.ToCharArray();
    
    Array.Reverse(palArray); //This reverses the array 

    if (palin2 == (string.Join("", palArray))) //Checks to see if the reversed array is the same as palin2, which is the original input but all lowercase.
        Console.WriteLine($"{palin2} is a palindrome");
    else
        Console.WriteLine($"{palin2} is not a palindrome");

}

public static void dayOfTheWeek()
{
    Console.WriteLine("Enter the day (00)"); // https://code-maze.com/csharp-datetime-format/
    string dayString = Console.ReadLine(); //I used this website and chat GPT to figure this out, still don't really know how it works.
    int day = int.Parse(dayString);
    Console.WriteLine("Enter the month (00)");
    string monthString = Console.ReadLine();
    int month = int.Parse(monthString);
    Console.WriteLine("Enter the year (0000)");
    string yearString = Console.ReadLine();
    int year = int.Parse(yearString);
    var datetime = new DateTime(year, month, day);
    Console.WriteLine(datetime.ToString("D")); 
}

public static void taxBracket()
{
    Console.WriteLine("Please enter your income:$");
    string incomeString = Console.ReadLine();
    int income = int.Parse(incomeString);
    if (income >= 578126)
        Console.WriteLine("Your tax rate is 37%"); //Lines 235-247 just determine whether the amount of income fits between the certain tax brackets.
    else if (income >= 231251)
        Console.WriteLine("Your tax rate is 35%");
    else if (income >= 182101)
        Console.WriteLine("Your tax rate is 32%");
    else if (income >= 95376)
        Console.WriteLine("Your tax rate is 24%");
    else if (income >= 44726)
        Console.WriteLine("Your tax rate is 22%");
    else if (income >= 11001)
        Console.WriteLine("Your tax rate is 12%");
    else if (income >= 0)
        Console.WriteLine("Your tax rate is 10%");
    else
        Console.WriteLine("This is an invalid amount");
}







}





