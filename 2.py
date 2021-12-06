"""
Define an annotated function called file_analyzer that asks a user for two file names.

The program must try to open both files.

If either file cannot be opened print an appropriate error message and then end the program
gracefully.

Do not let the program crash.

If both of the files exist, the program must open both files and return a dictionary that
contains the following information (order does not matter):

1.	A sorted tuple of all the unique words, i.e., words that only occur once in
    both files (use the string key “unique union”)
2.	A sorted tuple of all the words that appear in both files (use the string key “intersection”)
3.	A sorted tuple of the words that appear in the first file but not the second
    (use the string key “first only”)
4.	A sorted tuple of the words that appear in the second file but not the first
    (use the string key “second only”)
5.	A sorted tuple of the words that appear in the first OR the second file but NOT both
    (use the string key “symmetric diff”).

No documentation or testing is required.

This will be graded out of 6.
"""
