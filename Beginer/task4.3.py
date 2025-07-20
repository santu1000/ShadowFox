
# same 3 list from 4.2
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# get two cities input from user
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

#creat a function g_c to reduce code size 
def g_c(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

# Get countries for both cities
country1 = g_c(city1)
country2 = g_c(city2)

# Compare and see is the condition is met
if country1 and country2:
    if country1 == country2:
        print("Both cities are in "+country1)
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in our list")

#---------------------------------------OUTPUT----------------------------------------------  
#Enter the first city: Bangalore
#Enter the second city: Delhi
#Both cities are in India

