#Extract date
import re
st =input("Enter string:")
result = re.findall(r"\d",st)
print(result)
