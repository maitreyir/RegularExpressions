#Email validation regex
import re
st =input("Enter string:")
result = re.match('[^@]+@[^@]+\.[^@]+',st)
if result:
    print("True")
else:
    print("False")
