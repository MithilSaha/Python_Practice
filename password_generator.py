import random

user_char = int(input("Enter number of characters:\t"))
user_num = int(input("Enter numbers:\t"))
user_syb = int(input("Enter number of sysmbols:\t"))

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nums = ["0","1","2","3","4","5","6","7","8","9"]

sybs  = ["!","#","$","%",'&',"(",")","*","+","-","/"]

fixed_pwd = []
random_pwd = ""

for i in range(0,user_char):
    fixed_pwd.append(chars[random.randint(0,len(chars)-1)])

for i in range(0,user_num):
    fixed_pwd.append(nums[random.randint(0,len(nums)-1)])

for i in range(0,user_syb):
    fixed_pwd.append(sybs[random.randint(0,len(sybs)-1)])

fixed_pwd_dup = fixed_pwd[:]

for i in range(0,user_char+user_num+user_syb):
    x = fixed_pwd[random.randint(0,len(fixed_pwd)-1)]
    random_pwd = random_pwd + x
    fixed_pwd.remove(x)

print(random_pwd)

for i in random_pwd:
    if i in fixed_pwd_dup:
        continue
    else:
        print("All Characters,Number and Sysbols of fixed_pwd are not used in random_pwd")
        print(i)
        break