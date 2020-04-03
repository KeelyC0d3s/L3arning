#Homework. PLaying with matplotlib.

#Write a program that displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 
#in the range [0, 4] on the one set of axes.


import numpy as np

import matplotlib.pyplot as plt

#Going to play with plotting first
#Trying example from the video

#l=np.arange(0.0, 10.0, 0.5)

#print(l)

#plt.plot(l , l**2)
#plt.show()

#Ok, now for the homework. 

x=np.arange(0.0, 4.0)

print(x)

plt.plot(x, x)
plt.plot(x, x**2)
plt.plot(x, x**3)
plt.show()

#Essentially what I did was assume each function f(x), f(g), f(h) was
#its own plot. I then used the same program as demonstrated in the video
#but using the values given in the homework assignment.



