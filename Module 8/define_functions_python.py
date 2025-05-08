# Define the function that checks if x is greater than y that will be used with our variables later on
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

# Declare variables 'a' and 'b', main part of the program
a = 10
b = 6

# Declare the 'result' variable by calling the function we first created
result = greater_than(a, b)

# Print the result in the specified format
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
