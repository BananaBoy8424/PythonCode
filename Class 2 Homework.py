import time
print("Welcome to my high or low detector where I tell you if a number is high or low!")
time.sleep(2)

int_1 = int(input("Please choose an integer from 1 to 100"))
statement1 = (str(int_1)+" is your number.")
print(statement1)

int_2 = int(input("Please choose another integer from 1 to 100"))
statement2 = (str(int_2)+" is your number.")
print(statement2)

int_3 = int(input("Please choose the last integer from 1 to 100"))
statement3 = (str(int_3)+" is your number.")
print(statement3)

time.sleep(2)
float_1 = float(input("Please choose a float number"))
statement4 = (str(float_1)+" is your number.")

float_2 = float(input("Please choose a float number"))
statement5 = (str(float_2)+" is your number.")

if int_1 < 50:
    print("Your first number is low.")
elif int_1 > 50:
    print("Your first number is high.")
else:
    print("Your first number is neither nigh nor low.")

if int_2 < 50:
    print("Your second number is low.")
elif int_2 > 50:
    print("Your second number is high.")
else:
    print("Your second number is neither nigh nor low.")

if int_3 < 50:
    print("Your third number is low.")
elif int_3 > 50:
    print("Your third number is high.")
else:
    print("Your third number is neither nigh nor low.")

if float_1 < 50:
    print("Your fourth number is low.")
elif float_1 > 50:
    print("Your fourth number is high.")
else:
    print("Your fourth number is neither nigh nor low.")

if float_2 < 50:
    print("Your fifth number is low.")
elif float_2 > 50:
    print("Your fifth number is high.")
else:
    print("Your fifth number is neither nigh nor low.")
    
print("Thanks! :)")
