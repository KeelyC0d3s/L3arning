# Keely's homework
# Write a program that reads in a text file and outputs the number of e's it contains.
# First attempt with help from : https://www.w3schools.com/python/python_file_open.asp

# f= open("moby dick.txt" , "r")

# print(f.read ())

# https://www.w3schools.com/python/python_file_write.asp

# f = open("moby dick.txt", "a")
# f.write("Now the file has more content!")
# f.close()

#open and read the file after the appending:
# f = open("moby dick.txt", "r")
# print(f.read())

# Going to try this now: https://www.geeksforgeeks.org/downloading-files-web-using-python/

# import requests 

# r = requests.get("http://www.gutenberg.org/files/2701/2701-h/2701-h.htm", stream = True)

# print(r)

# Ok, that didn't work. I was trying to extract the text from the URL.

f = open("moby-dick.txt", "r")

count = 0
for line in f :
  lowercase_line = line.lower()
  for character in lowercase_line:
    if character == 'e' :
        count = count + 1
f.close()
print("Moby Dick has this many e's: ", count)




