import string
import random
v = ""
n = int(input("Enter number: "))
j = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
for i in range(n):
    v+=random.choice(j)
print(v)







