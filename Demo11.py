import re
st =input("Enter string:")
result = re.findall(r"\w+",st)
print(result)

#Return words starts with alphabets
import re
st1 =input("Enter string:")
#returns list
result = re.findall(r"[aeiouAEIOU]\w+",st1)
print(result)
