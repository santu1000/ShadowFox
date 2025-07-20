
#the given time is in minutes and meters so convert minutes into secounds and the speed formula is speed by time to get speed with the si unit m/s 
def speed(d_meters,t_minutes):
    t_seconds= t_minutes*60
    s=d_meters/t_seconds
    return int(s)

result= speed(490, 7)
print("Speed ==>",result,"m/s")

#---------------------------------------OUTPUT----------------------------------------------   
#Speed ==> 1 m/s
