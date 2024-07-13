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
'''cpp
#include <iostream>

int main(void)
{
  std::cout << "Hello, World!" << std::endl;
  return 0;
}
