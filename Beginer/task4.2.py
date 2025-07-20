
#add elements to 3 list
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

#let the user give the city name
city = input ("enter the city name :")

#condition checking 
if city in australia :
    print(city+" is in australia")
elif city in uae :
    print(city+" is in UAE")
elif city in india:
    print(city+" is in india")
else:
    print(city+" is not in the list ")
    
#---------------------------------------OUTPUT----------------------------------------------  
#enter the city name :Bangalore
#Bangalore is in india
