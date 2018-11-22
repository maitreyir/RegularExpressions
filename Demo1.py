#find match if it occurs at start of the string

import re
string =input("Enter string:")
#return match object
result = re.match(r"Master",string)
if result == None:
    print("Match not found")
else:
    print("match found")

#find the  match any where from the string
import re 
st =input("Enter string")
#return match object
res =re.search(r"satya",st)
print(res)
print(res.group())
print(res.start())
print(res.end())


#find all matching patterns.
import re
st1 = input("Enter string:")
res=re.findall(r"Master",st1)
print(result)