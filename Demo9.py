#Return domain type of give email-ids
import re
st =input("Enter string:")
result = re.findall(r"@\w+",st)
print(result)


import re
st =input("Enter string:")
result = re.findall(r"@\w+.\w+",st)
print(result)

#Etract domains only
import re
st3 =input("Enter string:")
result = re.findall(r"@\w+.(\w+)",st3)
print(result)
