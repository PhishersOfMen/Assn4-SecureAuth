import os
def test(filename):
    newfile = "test.txt"
    with open(newfile) as file:
        file.write(filename)
        file.write(os.getcwd)