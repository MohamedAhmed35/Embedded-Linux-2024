#include <iostream>
#include <iomanip>

int main (void)
{
    std::cout << "ASCII code Table" << std::endl;
    std::cout << "+------+-------+" << std::endl;
    std::cout << "| char | ASCII |" << std::endl;
    std::cout << "+------+-------+" << std::endl;

    for(int i = 0; i < 128; i++)
    {
        // std::cout << '|' << std::setw(3) << (char)i << std::setw(4) << '|'
        // << std::setw(4) << i << std::setw(4) << '|' << std::endl;
        if (i < 32 or i == 127)
            std::cout << "|" << std::setw(4) << " " << "  |"
            << std::setw(4) << i << "   |" << std::endl;
        else
        {
            std::cout << "|" << std::setw(4) << static_cast<char>(i) << "  |"
            << std::setw(4) << i << "   |" << std::endl;
        }
    }
    return 0;
}