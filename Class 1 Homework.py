import time
print("Welcome to Nathan Yang's math machine. I will be telling you what your favorite number plus your age is. Give me a sec to boot up...")
time.sleep(5)
fav_number = int(input("What is your favorite number?"))
age = int(input("What is your age?"))
print("Thank you. Cacluating...")
time.sleep(5)
print("Your favorite number plus your age is")
print(fav_number + age)
yesorno = int(input("Did I get it right? 1=Yes 2=No"))
if(yesorno > 1):
    print("Aww :( I'll get it next time!")
else:
    print("Yay :) Thanks for playing!")
    
