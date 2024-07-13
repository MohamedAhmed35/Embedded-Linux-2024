#include <iostream>
#include <bitset>

int main (void)
{
    int num = 0;
    std::string binaryStr;

    std::cout << "Enter a decimal number: ";
    std::cin >> num;
    std::bitset<8> bits(num);
    std::cout << "Binary representation: " << bits.to_string() << std::endl;

    std::cout << "Enter a binary number: ";
    std::cin >> binaryStr;
    std::bitset<8> dec(binaryStr);
    std::cout << "Decimal representation: " << dec.to_ulong() << std::endl;


    // int num = 0;
    // int binaryNum[8] = {0};
    // char i = 0;

    // std::cout << "Enter a decimal number: ";
    // std::cin >> num;
    
    // while(num > 0)
    // {
    //     binaryNum[i++] = num % 2;
    //     num = num / 2;
    // }

    // Printing the binary array ins reverse order
    // std::cout << "Binary representation: ";
    // for(int j = i - 1; j >= 0; j--)
    // {
    //     std::cout << binaryNum[j];
    // }
    // std::cout << std::endl;

    return 0;
}