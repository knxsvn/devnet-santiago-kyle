"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Santiago Kyle]
Date: [9/27/26]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow allows a program to make decisions based on
different conditions. The if, elif, and else statements tell
Python what to do depending on whether a condition is true or
false.

For example, a program can check a student's grade. If the grade
is 90 or higher, it can say "Excellent." If it is 75 or higher,
it can say "Passed." Otherwise, it can say "Failed." This allows
the program to automatically choose what action to perform.

============================================
KEY VOCABULARY
============================================
- condition: A rule that evaluates to True or False
- if / elif / else: Statements that control the flow of a program based on conditions
- comparison operator: Used to compare two values (e.g., ==, !=, <, >, <=, >=)
- boolean expression: An expression that evaluates to True or False
- if: Runs a block of code when its condition is True.
- elif: Checks another condition if the previous if condition
  was False.
- else: Runs when none of the previous conditions are True.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# # Student grade checker

grade = 87

if grade >= 90:
    print("Excellent!")
elif grade >= 75:
    print("Passed!")
else:
    print("Failed!")



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is using = instead of == when
comparing values. A single = is used to assign a value to a
variable, while == checks if two values are equal.

I also need to make sure that thr conditions are in the correct order beacause Python 
check the condition from top to botttom and runs the firs condition that is True.  


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
