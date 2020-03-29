# Keely's homework again.
# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.8.
# Now, time to figure out how to get the square root of 14.5

#import math

#math.sqrt(14.5)

#print( "math.sqrt(14.5)", math.sqrt(14.5))

#Trying Newton Method.
#Found code here: https://tinyurl.com/v9ob6nm

# Function to return the square root of  
# a number using Newtons method  
def squareRoot(n, l) : 
  
    # Assuming the sqrt of n as n only  
    x = n  
  
    # To count the number of iterations  
    count = 0  
  
    while (1) : 
        count += 1  
  
        # Calculate more closed x  
        root = 0.5 * (x + (n / x))  
  
        # Check for closeness  
        if (abs(root - x) < l) : 
            break  
  
        # Update root  
        x = root 
  
    return root  
  
# Driver code  
if __name__ == "__main__" :  
  
    n = 14.5  
    l = 0.00001  
  
    print(squareRoot(n, l))





