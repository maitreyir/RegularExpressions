#To search if an email-address is in a string
import re
st =input("Enter string:")
result = re.search('[^@]+@[^@]+\.[^@]+',st)
if result:
    print("Found")
else:
    print("Not found")
