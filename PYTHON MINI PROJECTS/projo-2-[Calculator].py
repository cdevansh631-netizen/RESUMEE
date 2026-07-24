#SIMPLE CALCULATOR:

print("SELECT :\n1-FOR-ADDITION\n2-FOR-SUBTRACTION\n3-FOR-MULTIPLICATION\n4-FOR-DIVISION")
def calculator(a,b):
    x=int(input("Choose : "))
    if x==1:
        print("ADDITION--:",a+b)
    elif x==2:
        print("SUBTRACTION--:",a-b)
    elif x==3:
        print("MULTIPLICATION--:",a*b)
    elif x==4:
        if b==0:
            print("not calculatable")
        else:
            print("DIVISION--:",a/b)

a=int(input("Enter 1st No : "))
b=int(input("ENter 2nd No : "))
calculator(a,b)

