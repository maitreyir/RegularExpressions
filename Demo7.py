import re
st =input("Enter string:")
# $ returns the word from end of the string
result = re.findall(r"\w+$",st)
print(result)
