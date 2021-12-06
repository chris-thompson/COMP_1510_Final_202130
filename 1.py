"""
Define an annotated recursive function called most_vowels that accepts a possibly empty
tuple of strings and returns an integer representing the number of vowels in the
string that contains the most vowels.

For example, if passed a tuple containing the strings ‘a’, ‘eve’, and ‘applesauce’,
the function most_vowels will return 5 because the word 'applesauce' contains five vowels
and 'a' and 'eve' only contain one and two respectively.

Remember that in order to work recursively, one must identify the base case and the recursive step.

I will give you a hint. The base case is a tuple of length 0, which should return length 0.

If we haven't encountered the base case, then we must return the maximum of:

a) the number of vowels in the first string in the tuple, or
b) the integer returned from the recursive call which passes the rest of the tuple to the same
   function.

The most_vowels function must work recursively.  Iterative solutions will not receive any marks.

No docstrings are needed. Provide two useful different doctests.

This will be graded out of 6.
"""
