num1=float(input("Enter first number"))
num2=float(input("Enter second number"))
print("Press\n A-Add\n S-Sub\n M-Multiply\n D-Divide\n")
choice=input('Enter your choice')
if(choice.upper()=="A"):
    print(num1+num2)
elif(choice.upper()=="S"):
    print(num1-num2)
elif(choice.upper()=="M"):
    print(num1*num2)
elif(choice.upper()=="D"):
    if(num2==0):
        print(num1/num2)
    else:
        print(num1/num2)
else:
    print("Select the Options")