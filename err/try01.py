#!/usr/bin/python3

# Start with an infinite loop
while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.\n")
        break
    except:
        print("Error with that file name! Try again...")

