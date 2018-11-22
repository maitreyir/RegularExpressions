#Split the string
import re
st =input("Enter string:")
result =re.split(r"a",st)
print(result)

#Max split
import re
st1 =input("Enter string:")
result =re.split(r"a",st1,maxsplit=1)
print(result)

#Replace with new sub  string
import re
st2 =input("Enter string:")
result =re.sub(r"java","python",st2)
print(result)





