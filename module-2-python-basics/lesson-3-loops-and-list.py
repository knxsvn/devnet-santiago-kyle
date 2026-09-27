"""
Module 2 — Lesson 3: Loops & Lists
Student: [Kyle Santiago]
Date: [9/27/26]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Lists and loops are used to store and work with
multiple pieces of data. A list lets us keep many
items in one variable, while loops let us repeat
instructions for each item or while a condition is true.

============================================
KEY VOCABULARY
============================================
- list: A collection of items stored in a single variable, which can be of different data types.
- for loop: Repeats a block of code for each item in a list or other iterable.
- while loop: Repeats a block of code as long as a specified condition is true.
- index: The position of an item in a list, starting from 0 for the first item.
- iteration: One repetition of a loop, where the code block is executed for one item or one condition check.
- item: A single value stored inside a list.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
# A list of my favorite games
games = ["Call of Duty", "Roblox", "Valorant", "Mobile Legends",]

# Use a for loop to print every game
for game in games:
    print("I like playing", game)

# Use an index to access a specific item
print("My first game is", games[0])


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is forgetting that list
indexes start at 0 instead of 1. For example, games[0]
gets the first item, while games[1] gets the second item.

Another mistake is creating a while loop without making
the condition eventually become false, which can cause
an infinite loop.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
