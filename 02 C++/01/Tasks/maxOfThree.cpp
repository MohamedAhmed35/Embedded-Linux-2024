#include <iostream>

int main (void)
{
    int num1;
    int num2;
    int num3;
    int max;

    std::cout << "Enter 1st number: ";
    std::cin >> num1;
    std::cout << "Enter 2nd number: ";
    std::cin >> num2;
    std::cout << "Enter 3rd number: ";
    std::cin >> num3;

    if (num1 >= num2 && num1 >= num3)
    {
        max = num1;
    }
    else if (num2 >= num1 && num2 >= num3)
    {
        max = num2;
    }
    else
    {
        max = num3;
    }
    std::cout << "Number: " << max << " is max number" << std::endl;

}