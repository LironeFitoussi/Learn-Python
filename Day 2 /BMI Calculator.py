weight = int(input("Type Your Weight in KG:"));
height = float(input("Type Ypur Heigh in meters"));
bmi = weight / float(height**2);
print(f"Your BMI is {round(bmi, 2)}")