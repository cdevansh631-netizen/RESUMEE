# To-Do List App (Console)

# Concepts: list, while loop
# Add tasks, show tasks, delete tasks.
print("1-FOR ADDITION\n2-SHOW TASK\n3-DELETE TASK")

result=[]
while True:
    C=int(input("Choose : "))
    if C==1:
        T=input("Enter task : ")
        result.append(T)
        print("Task Added")
    elif C==2:
        for i,t in enumerate(result,1):
            print(f"{i}. {t}")
    elif C==3:
        num=int(input("Enter task number to delete : "))
        if 1<=num<len(result):
            deleted=result.pop(num-1)
            print("Deleted :",deleted)
        else:
            print("Invalid task number")
    elif C==4:
        print("Exit")
        break
    else:
        print("Invalid choice")
    



