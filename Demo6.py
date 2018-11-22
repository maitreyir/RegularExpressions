# Extract each word 
import re
st = input("Enter string:")
result =re.findall(r"^\w+",st)
print(result)
