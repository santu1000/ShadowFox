
#2 simple formal one is to find the area and other is find the total water the area of circle is pi r^2 and just multiply it with the water per sq meter to find the total water 

def pond_water_volume(r):
    pi =3.14
    water_per_sqm =1.4
    
    area= pi*r*r
    total_water= area*water_per_sqm
    return int(total_water)

result=pond_water_volume(84)
print("Total Water is:",result)

#---------------------------------------OUTPUT---------------------------------------------- 
#Total Water is: 31018
