# Big Integer

**Description:**

1. **Objective:**
   At the end of this programming assignment, participants should be able to:
   - Understand precision limitations in Python's integer types
   - Implement classes in Python to handle large integer values
   - Convert algebraic procedures to Python algorithms
   - Parse and evaluate simple arithmetic/DMAS expressions in Python

2. **Prerequisites:**
   Before starting this programming assignment, participants should be familiar with:
   - Writing Python classes
   - Python class terminology
   - Understanding of addition & subtration algorithms; `long multiplication` and `long division` algorithms

3. **Overview & Requirements:**
   You are required to create a Python class named `BigInt` that can store integer values with unlimited precision. Your class should handle any integer value within memory constraints.

   Approach:
   - Use Python lists (or Numpy arrays) to store numerical data, i.e. store the number in the forms of digits in the list. For example, the object `BigInt('12372893472934729348234')` will store the digits as `[1, 2, 3, 7, 2, 8, 9, 3, 4, 7, 2, 9, 3, 4, 7, 2, 9, 3, 4, 8, 2, 3, 4]` in its data-member `digits`.
   - You cannot use any built-in functions of Python or any 3rd party mmodule.

   Implement the following methods in your `BigInt` class:
   1. `__init__(self, value: str)` - Constructor to initialize `BigInt` from a string.
   2. `__str__(self)` - Return a string representation of the `BigInt` object.
   3. `__add__(self, other: 'BigInt')` - Addition operator overloading.
   4. `__sub__(self, other: 'BigInt')` - Subtraction operator overloading.
   5. `__mul__(self, other: 'BigInt')` - Multiplication operator overloading.
   6. `__truediv__(self, other: 'BigInt')` - Division operator overloading.
   7. `__floordiv__(self, other: 'BigInt')` - Floor division operator overloading.

4. **Submission:**
   - Push your Python Jupyter Notenook named `Submission.ipynb` at [programming-fundamentals/Homework-4-BigInt](https://github.com/programming-fundamentals/Homework-4-BigInt); containing the `BigInt` class implementation and examples of its usage for each individual function and some simple and complex DMAS examples too.
   - Ensure your code adheres to proper Python coding standards and includes necessary comments and documentation.

Disclaimer: This assignment description is a Python adaptation of the [origical C++ assignment description](https://eecs.wsu.edu/~nroy/courses/cpts122/programming/PA8_cpts122.htm), made using ChatGPT.