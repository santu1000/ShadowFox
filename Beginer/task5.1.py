
#given the dice is rolled atleast 20 times so give any number >=20
n_rolls=21

#now for getting the count of 6 ,1 and 2 sixes in arow , lets create a variable for them
count_6=0
count_1=0
count_6_row=0

#to check the present roll and previous roll was 6 we nned a variable to store the previous role 
p_roll=0

#now to select the number from 1 to 6 in random use the random function with for for continous loop
import random
for i in range(n_rolls):
    roll= random.randint(1,6)
    print(f"Roll{i+1}:{roll}")

#to check how many times the we got 2 six in a row 
    if roll==6:
        count_6=count_6+1
        if p_roll==6:
            count_6_row=count_6_row+1
    if roll==1:
        count_1=count_1+1
    p_roll=roll
    
print("---- THE STATSTICS OF 6 AND 1 ----")
print(f"Number of times 6 rolled:{+count_6}")
print(f"Number of times 1 rolled:{+count_1}")
print(f"Number of times two six in row is rolled:{count_6_row}")

# --------------------------------------OUTPUT--------------------------------------------------- 
# Roll1:2
# Roll2:6
# Roll3:3
# Roll4:3
# Roll5:5
# Roll6:3
# Roll7:6
# Roll8:1
# Roll9:1
# Roll10:6
# Roll11:3
# Roll12:5
# Roll13:5
# Roll14:2
# Roll15:6
# Roll16:4
# Roll17:3
# Roll18:4
# Roll19:4
# Roll20:3
# Roll21:3
# ---- THE STATSTICS OF 6 AND 1 ----
# Number of times 6 rolled:4
# Number of times 1 rolled:2
# Number of times two six in row is rolled:0
