weight = float(input("input your weight in kg: "))
height = float(input("input your height in metres: "))

bmi = round(weight / (height * height), 2)
print("Your bmi is:" + str(bmi))
