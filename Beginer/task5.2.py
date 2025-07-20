
#I am just making the chat box like the solo leveling anime this task is just a simple loop if the requirement is meet the loop should break and output should be displayed 
total_jj=100
#intially the jumps done is zero
jj_done=0
print(f"Lets Begin the Daily Quest\n ")
while jj_done<total_jj:
    print(f" DO 10 JUMPING JACKS\n")
    jj_done =jj_done+10;
    
    if jj_done>=total_jj:
        print("Congratulations on Completing The Daily Quest\n Consistency Is The Key For Sucess")
        break
    
    t=input("Are you Tierd? Will You Give up now\n Yes[Y] or No[N]\n").strip().lower()
    
    if t in ["yes","y"]:
        s=input("Do you want to skip the training and Go on the easy path \n Yes[Y] or No[N]\n").strip().lower()
        if s in ["yes","y"]:
            print(f"\n You have COMPLETED a total of {jj_done} jumping jacks.\n")
            break
        else:
            print(f"{total_jj-jj_done} jumping jacks remaning. PUSH PASS YOU LIMITS!!\n")
    elif t in ["no","n"]:
        print(f"{total_jj-jj_done} jumping jacks remaning. PUSH PASS YOU LIMITS!!\n")
    else:
         print("Invalid input. Lets Not Waste Time Comeee Onn Continue\n")

# --------------------------------------OUTPUT---------------------------------------------------          
""" 
Lets Begin the Daily Quest
 
 DO 10 JUMPING JACKS

Are you Tierd? Will You Give up now
 Yes[Y] or No[N]
No
90 jumping jacks remaning. PUSH PASS YOU LIMITS!!

 DO 10 JUMPING JACKS

Are you Tierd? Will You Give up now
 Yes[Y] or No[N]
no
80 jumping jacks remaning. PUSH PASS YOU LIMITS!!

 DO 10 JUMPING JACKS

Are you Tierd? Will You Give up now
 Yes[Y] or No[N]
n
70 jumping jacks remaning. PUSH PASS YOU LIMITS!!

 DO 10 JUMPING JACKS

Are you Tierd? Will You Give up now
 Yes[Y] or No[N]
N
60 jumping jacks remaning. PUSH PASS YOU LIMITS!!

 DO 10 JUMPING JACKS

Are you Tierd? Will You Give up now
 Yes[Y] or No[N]
Yes
Do you want to skip the training and Go on the easy path 
 Yes[Y] or No[N]
y

 You have COMPLETED a total of 50 jumping jacks. 
 """
