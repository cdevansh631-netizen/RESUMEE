import random
import string 

num=string.punctuation+string.ascii_letters+string.digits
length=random.randint(8,12)
Pass="".join(random.choice(num) for i in range(length))

print("NEW PASSWORD : ",Pass)