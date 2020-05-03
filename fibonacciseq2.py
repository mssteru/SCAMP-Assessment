# This code would print the numbers that occur in the sequence based on the number entered by the user.
def fibonaccisequence():
    nseries = int (input('Enter a number'))
    x, y = 0, 1
    count = 0
    if nseries <= 0:
       print("Please enter a positive number")
    elif nseries == 1:
       print(x)
    else:
        while count < nseries:
            print(x) 
            f = x + y
            x = y
            y = f
            count += 1
            
fibonaccisequence()