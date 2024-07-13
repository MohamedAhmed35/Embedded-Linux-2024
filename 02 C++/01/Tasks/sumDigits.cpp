#include <iostream>
#include <string>

int main (void)
{
    int num = 0;
    int sum = 0;

    std::cout << "Enter a number: ";
    std::cin >> num;

    // convert the integer to a string 
    std::string numStr = std::to_string(num);

    // calculate the sum of the digits using string manipulation
    for (char digitChar: numStr)
    {
        int digit = digitChar - '0';     // convert character to integer
        sum += digit;
    }

    std::cout << "Sum of digits of " << num << " is: " << sum << std::endl;
}