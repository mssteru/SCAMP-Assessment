# This code would print the numbers in the fibonacci sequence that are less than the number entered by user.
def fibbonaciseq():
    nseries = int (input('Enter a number'))
    x = 0
    y = 1
    if nseries <= 0:
       print("Please enter a positive number")
    elif nseries == 1:
       print(x)
    else:
        f = 0
        while f < nseries:
            print(f)
            f = (x + y)
            y = x
            x = f
            
fibbonaciseq()