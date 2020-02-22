# Keely doing homework again.
# Take a positive integer, if even divide by 2, 
# If odd, multiply by 3 and add 1,
# End program when value gets to 1.

# please enter a positive integer

# while True:
#    x=int(input('10'))
#    break
# print(x)


# well that didn't work.
#trying the below I found on stackoverflow.com


x=int(input('enter number: '))
print(x)
while x > 0:
    print ('value of x: ', x)   
    if x%2==0:
      x = x/2
    elif x>1:
      x = 3*x + 1
    else:
      break
print(x)
