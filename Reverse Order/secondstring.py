# Doing homework

# input string that outputs every second letter in reverse order

s="The quick brown fox jumps over the lazy dog."

myList= list(s)

myList.reverse()

print(myList[0 : len(myList) -1 : 2])


