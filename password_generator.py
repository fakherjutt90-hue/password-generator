import random
import string




p1 = string.ascii_letters + string.punctuation + string.digits

random_password = ""

for i in range(10):

   random_password += random.choice(p1)

print("your suggested strong password : " + random_password)

   

    
    



