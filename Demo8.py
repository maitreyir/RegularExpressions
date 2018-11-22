# Return  first two charcters of each word
import re
st =input("Enter string:")
result = re.findall(r"\w\w",st)
print(result)

#Extract consecutive two characters at start of word boundary
import re
st =input("Enter string:")
result = re.findall(r"\b\w.",st)
print(result)
