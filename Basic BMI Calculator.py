print("BMI CALCULATOR")
weight = int(input('Enter your weight in kg here: '))
height = int(input('Enter your height in centimeters here: '))
height = height/100
bmi = weight/height ** 2

print('Your BMI is: ' + str(bmi))

underweight = 18.5
normal_weight = 24.9
overweight = 29.9
obesity = 30

if bmi < underweight:
    print('Underweight')
elif bmi > underweight and bmi < normal_weight:
    print('Normal Weight')
elif bmi > normal_weight and bmi < 30:
    print('Overweight')
elif bmi >= obesity:
    print('Obese')
