#Extract each character
import re
st1 =input("Enter string:")
result =re.findall(r".",st1)
print(result)

#To avoid space use "\w"
import re
st1 =input("Enter string:")
result =re.findall(r"\w",st1)
print(result)

