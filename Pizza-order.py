print("Welcome to Python Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni= input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill=0
if size =='S':
    bill = 15
    print(f"Small size pizza costs ${bill}")
    
elif size =='M':
    bill = 20
    print(f"Medium size pizza costs ${bill}")
elif size =='L':
    bill = 25
    print(f"Large size pizza costs ${bill}")
else:
    print("Oops, Invalid input entered!")

if pepperoni== 'Y' and size == 'S':
    bill+=2
    print("Pepperoni added for cost of $2")
elif pepperoni == 'Y':
    bill+=3
    print("Pepperoni added for cost of $3")

if extra_cheese == 'Y':
    bill+=1
    print("Extra cheese added for cost of $1")

print(f"Total bill for your pizza order is ${bill}, happy orderingg!")


# #OUTPUT
# Welcome to Python Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Large size pizza costs $25
# Pepperoni added for cost of $3
# Total bill for your pizza order is $28, happy orderingg!