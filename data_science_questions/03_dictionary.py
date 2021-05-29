# Purpose: wants to add the square of even numbers to the dictionary.

num = range(10)

for i in num:
    if i % 2 == 0:
       print({i : i**2})
    else:
        print({i: i-1})

{i: i**2 for i in num if i % 2 == 0}