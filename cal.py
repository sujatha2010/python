def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return int(bmi)

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi_result = calculate_bmi(weight, height)
print("BMI:", bmi_result)
