def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    bmi = weight / (height * height)

    if (bmi < 18.5):
        print("User is underweight")
    elif (bmi > 25):
        print ("User is overweight")
    else:
        print("User is normal weight")
#Add code here to display calculate BMI
    print("BMI = " + str(bmi))
calculate_bmi(weight=57, height=1.73)