#include <iostream>

int main(void)
{
    int l1 = 0;
    int l2 = 0;
    int l3 = 0;

    std::cout << "Enter 1st side of triangle: ";
    std::cin >> l1;
    std::cout << "Enter 2nd side of the triangle: ";
    std::cin >> l2;
    std::cout << "Enter 3rd side of the triangle: ";
    std::cin >> l3;

    if(((l1*l1) == ((l2*l2) + (l3* l3))) || ((l2*l2) == ((l1*l1) + (l3*l3))) || ((l3*l3) == ((l1*l1) + (l2*l2))))
        std::cout << "Right angle triangle" << std::endl;
    else
    {
        std::cout << "Not right angle triangle" << std::endl;
    }
}