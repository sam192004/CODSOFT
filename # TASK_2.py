num1=int(input("Enter number1 ="))
num2=int(input("Enter number2 ="))
def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def mult(num1,num2):
    return(num1*num2)
def div(num1,num2):
    return(num1/num2)
def mod(num1,num2):
    return(num1%num2)
print("Enter your choice :")
choice=str(input("select - a. b. c. d. e. "))
if choice=="a":
    print("answer=",add(num1,num2))
elif choice=="b":
    print("answer=",sub(num1,num2))
elif choice=="c":
    print("answer=",mult(num1,num2))
elif choice=="d":
    print("answer=",div(num1,num2))
elif choice=="e":
    print("answer=",div(num1,num2))
else:
    print("enter valid choice ")