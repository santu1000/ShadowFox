
#her the fmt is teh format specifer which converts the given value into one format to another for an example a binanry fromat is indicated by the letter "b" where as the octal format is indicated by the letter "o".
def f_number(value, fmt):
    result = format(value ,fmt)
    return result 
f_result=f_number(145, 'o')
print("formatted Result:",f_result)

#---------------------------------------OUTPUT---------------------------------------------- 
#formatted Result: 221
