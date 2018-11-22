#validate name
import re
name =input("Enter Name:")
result = re.match("[A-Za-z]*$",name)
if result == None:
    print("Invalid name")
else:
    print(name)

#Match a string to a numberic sequennce of exactly five
import re
st =input("Enter string:")
result = re.match('\d{5}\z',st)
if result:
    print("True")
else:
    print("False")
    
