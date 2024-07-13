#include <iostream>


int main (void)
{
    char ch;
    std::cout << "Enter a character: ";
    std::cin >> ch;

    for(int vowel : "aeiou")
    {
        if(ch == vowel)
        {
            std::cout << "character " << (char) ch << " is a vowel";
            return 0;
        }
    }
    std::cout << "character " << ch << " is not a vowel" << std::endl;
}