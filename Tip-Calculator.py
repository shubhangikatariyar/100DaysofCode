#PEMDASLR

print("Welcome to the tip calculator!")
bill= float(input("What was the total bill? \n$"))
tip=int((input("How much tip would you like to give? 10, 12, or 15? \n")))
n= int(input("How many people to split the bill? \n"))
cost= round((((100+tip)/100)*bill/n),2)
print("Each person should pay: $",cost)


# OUTPUT:
# Welcome to the tip calculator!
# What was the total bill? 
# $153.45
# How much tip would you like to give? 10, 12, or 15? 
# 15
# How many people to split the bill? 
# 5
# Each person should pay: $ 35.29