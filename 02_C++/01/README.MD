# C++ Programming Language
## Difference between C and C++
- C:
  - Procedural programming language.
  - Focuses on functions and procedures to operate on data.
  - No built-in support for OPP (Object-Oriented Programming).
  - Does not support function overloading.
  - No support for generic programming (templates).
  - Uses **stdio.h** for input and output.
- C++:
  - Support both procedural and object-oriented programming.
  - Emphasizes objects and data abstraction.
  - Supports function overloading and operator overloading.
  - Provides templates for generic programming.
  - Uses **iostream** for input and output.

## Introduction and Usage
C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language. It is widely used in system/software development, game development, drivers, client-server applications, and embedded firmware.

## Main Features
- **OOP (Object-Oriented Programming)**: Support classes, objects, inheritance, polymorphism, encapsulation, and 
  abstraction.
- **Statically Typed Language**: Type checking is performed at compile-time.
- **STL (Standard Template Library)**: Provides a set of common classes and interfaces for data structures and 
  algorithms.

## C++ Standards and Popular Features
- C++98:
  - Introduced the Standard Template Library (STL).
  - Basic support for templates, strings, and I/O streams.
- C++11:
  - Move semantics, auto keywords, lambda expressions, and threading.
  - **nullptr**, ranged-based loop, and smart pointers.
- C++14:
  - Reader-writer locks, generic lambda expressions.
- C++17:
  - Fold expressions, **if constexpr**, structured bindings.
  - **std::string_view**, parallel algorithms, and filesystem library.
  - **std::any**, **std::optional**, and **std::variant**.
- C++20:
  - Coroutines, modules, concepts, ranges library.
- C++23:
  - Deducing **this**, modularized standard library, **std::print**, and **std::println**.
  - Flat associative containers, **std::expected**, imporved ranges.
  - **std::mdspan**, **std::generator**.

## Hello World Example
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

## Comments
- Single-line: // This is a comment
- Multi-line:  /* This is a multi-line commnet */

## Display (Output)
```cpp
#include <iostream>
int main (void)
{
  std::cout << "Output text" << std::endl;
  return 0;
} ```
- std::cout: standard character output stream.
- std::endl: Ends the line and flushes the buffer.

## Data Types in C++
- Primitive Types: int, char, float, double, bool.
- Derived Types: Arrays, pointers, references.
- User-defined Types: Classes, structures, unions, enumerations.

## Input
```cpp
#include <iostream>
{
  int num;
  std::cout << "Enter a number: ";
  std::cin >> num;
  std::cout << "You entered: " << num << std::endl;
  return 0;
} ```

## Manipulators
```cpp
#include <iostream>
#include <iomanip>

int main() {
    int num = 255;
    std::cout << std::hex << num << std::endl; // Outputs in hexadecimal
    std::cout << std::dec << num << std::endl; // Outputs in decimal
    return 0;
} ```
- std::hex: Manipulator to format output in hexadecimal.
- std::dec: Manipulator to format output in decimal.

## Global VS. Local Variables
- **Global Variables**: Declared outside all functions and accessible from any function.
- **Local Variables**: Declared within a function and accessible only within that function.

## Operators
- Arithmetic operators: +, -, *, /, %.
- Relational operators: ==, !=, <, >, <=, >=.
- Logical operators: &&, ||, !.
- Bitwise operators: &, |, <<, >>.
- Assignment operators: =, +=, -=, *=, /=, %=.


## Conditional Statements (if/switch)

### if Statements:
```cpp
int main() {
    int num = 10;
    if (num > 5) {
        std::cout << "Number is greater than 5" << std::endl;
    } else {
        std::cout << "Number is 5 or less" << std::endl;
    }
    return 0;
} ```

### switch Statements:
```cpp
int main() {
    int num = 2;
    switch (num) {
        case 1:
            std::cout << "Number is 1" << std::endl;
            break;
        case 2:
            std::cout << "Number is 2" << std::endl;
            break;
        default:
            std::cout << "Number is not 1 or 2" << std::endl;
            break;
    }
    return 0;
} ```

## Loops
### For Loop:
```cpp
int main() {
    for (int i = 0; i < 5; ++i) {
        std::cout << i << std::endl;
    }
    return 0;
} ```
### While Loop:
```cpp
int main() {
    int i = 0;
    while (i < 5) {
        std::cout << i << std::endl;
        ++i;
    }
    return 0;
} ```
### do-while Loop:
```cpp
int main() {
    int i = 0;
    do {
        std::cout << i << std::endl;
        ++i;
    } while (i < 5);
    return 0;
} ```
### Range-Based Loop:
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    for (int num : vec) {
        std::cout << num << std::endl;
    }
    return 0;
} ```
- Iterates over elements of a container (like array, vectors, or string).
