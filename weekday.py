#Keely's homework
#Write a program that outputs whether or not today is a weekday

#import datetime

#datetime.datetime.now()

#now= datetime.datetime.now()

#print(now)

#Ok, going to try for real now. Not just fooling around with datetime

# Attempting below code taken from https://tinyurl.com/v3l8wfx

#week_days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

#l=list(map(int, input("Enter date \n eg: 02/22/2020 \n\n").split('/')))
#day=datetime.date(l[2],l[1],l[0]).weekday()

#print(week_days [day])

#Ok, weird that the date didn't change from the example since I changed the date from 05/05/2019 to 22/02/2020

#print(week_days [day])
#Better. Needed to input American format for the date.

#Trying the below from https://tinyurl.com/r9htt78
#Numbers 0-6 represent days of the week starting with Monday

import datetime


weekno = datetime.datetime.today().weekday()

if weekno<5:
    print ("Weekday")
else:
    print ("Weekend")

    