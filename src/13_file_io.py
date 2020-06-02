"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# cwd = os.getcwd()
# print(cwd)
# files = os.listdir(cwd)
# print(files)

# YOUR CODE HERE
foo_file = open('src/foo.txt', 'r')
foo_text = foo_file.read()
foo_file.close()
print(foo_text)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('src/bar.txt', 'x') as bar:
    bar.writelines(['Line 1', '\nLine 2', '\nLine 3'])

with open('src/bar.txt') as bar:
    print(bar.read())