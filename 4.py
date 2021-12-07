"""
The Caesar cipher is one of the earliest known and simplest ciphers. It is a type of substitution
cipher in which each letter in a plaintext message is 'shifted' a certain number of places down the
alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

One way to make a Caesar cipher a bit harder to break is to use different shifts at different
positions in the message. For example, we could shift the first character by 5, the second by 12,
the third by 7, and the fourth by 20. Then we repeat the pattern, shifting the fifth character by 5,
the sixth by 12, and so on, until we reach the end of the message we are encrypting.

Such a scheme is called a Vigenère cipher and it is about 400 years old.

Implement a function called vigenere which accepts the name of a plaintext file (a string),
a non-empty tuple of positive integers that are all in the range [0, 25] and a boolean called
encode.

The vigenere function must open the file for reading only. If the file does not exist, raise
a suitable exception that contains a suitable message, and end the program gracefully.

If the file does exist, you must:
 a) encrypt the message in the file using the Vigenere cipher if the boolean encode is True
 b) decrupt the message in the file using the Vigenere cipher if the boolean encode is False.

The vigenere function must store the shifted message in a new file whose name is
the original file appended with _shifted. For example, passing a file called 'message' to the
vigenere function will shift the text in message and write it to a file called 'message_shifted'.

Prove this function works.

Remember to add any additional test files to git and push them to the cloud so I can see your work.

This will be graded out of 6.
"""
