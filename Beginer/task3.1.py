
#defining the given list 
j_l=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]

#get number of members in list len() is used
print("total members:",len(j_l))

#add the batgirl and nightwing data to the list append() is used
j_l.append("Batgirl")
j_l.append("Nightwing")
print("justice league after adding Batgirl and Nightwing: ",j_l)

#move the wonder women to the beginning remove from the list using the remove function and using the insert function add it by declaring the index position
j_l.remove("Wonder Woman")
j_l.insert(0,"Wonder Woman")
print("justice league  after moving Wonder Woman to the beginning: ",j_l)

#seperate the flash and aquaman , add the green latern in the middle
j_l.remove("Green Lantern")
flash_index =j_l.index("Flash")
j_l.insert(flash_index+1,"Green Latern")
print("The List after the seperation is : ",j_l)

#craetion of the new justice leagu eteam/ list 
j_l=["Cyborg","Shazam", "Hawkgirl","Martian Manhunter", "Green Arrow"]
print("New Team Assemble:",j_l )

#Sort the new assembled team in the alphabetical order using the sort() function 
j_l.sort()
print("the sorted justice league team is: ",j_l)

#they are two ways to find the you can simply go with the first in the list as the team leader or use the random function for the random selection 
print("The Team Leader:",j_l[0])
import random
print("the Team Leader:",random.choice(j_l))

#---------------------------------------OUTPUT---------------------------------------------- 
# total members: 6
#justice league after adding Batgirl and Nightwing:  ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
#justice league  after moving Wonder Woman to the beginning:  ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
#The List after the seperation is :  ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Green Latern', 'Aquaman', 'Batgirl', 'Nightwing']
#New Team Assemble: ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']
#the sorted justice league team is:  ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']
#The Team Leader: Cyborg
#the Team Leader: Hawkgirl
