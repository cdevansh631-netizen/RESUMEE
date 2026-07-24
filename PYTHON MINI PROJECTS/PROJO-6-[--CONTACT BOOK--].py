# 6. Contact Book (Very simple version)

# Concepts: dictionary
# Store name → phone number
# Search by name.

Dict={}
print("1-FOR ADDING CONTACT\n2-FOR SEARCHING CONTACT\n3-SHOWING ALL CONTACT\n4-FOR DELETTING CONTACT\n5-EXIT")
while True:
    c=int(input("Choose :"))
    if c==1:
        Name=input("Enter Name :")
        Pno=int(input("Enter NO : "))
        Dict[Name]=Pno
    elif c==2:
        Name=input("Name in your Contact book : ")
        if Name in Dict:
            print(Name,":",Dict[Name])

        else:
            print("NO CONTACT FOUND!!")
    elif c==3:
        for i,(Name,Pno) in enumerate(Dict.items(),1):
            print(i,":",Name,"--",Pno)
    elif  c==4:
        Name=input("Enter name : ")
        if Name in Dict:
            Dict.pop(Name)
            print("Contact Deleted :",Name)
        else:
            print("CONTACT NOT FOUND")


    elif c==5:
        print("Exit--")
        break

    else:
        print("INVALID NO--TRY AGAIN")




