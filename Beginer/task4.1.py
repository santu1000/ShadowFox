
#Ask the user the height and weight of the person
height = float(input("Enter the height in meters: "))
weight = float(input("Enter the weight in kilograms: "))

#calculate the BMI weight by square of height 
bmi = weight /(height **2)

#determie the catgeory
if bmi >=30:
    print("Obesity")
elif bmi >=25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("UnderWeight")
    
#---------------------------------------OUTPUT----------------------------------------------  
# Enter the height in meters: 1.7779999
#Enter the weight in kilograms: 54
#UnderWeight
    


