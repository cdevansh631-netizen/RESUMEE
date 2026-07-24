#PANDAS NOTES :
import pandas as pd


#1-Creating a DataFrame:

# Data={"Name":["Dev","Raj","Anaya","Manay"],"Roll_No":[43,54,23,91],"Subject":["Chem","Physics","Math","Yoga"]}
# print(pd.DataFrame(Data))




#2-Reading a File-:
# -it only read plain file ie csv,excel-:
# print(pd.read_csv("Book1.csv"))




#3-Exploring Data in csv:-
# data=pd.read_csv("Book1.csv")
# print(data)
# print(data.head(1))            #1st row only
# print(data.tail(2))            #Last 2
# print(data.info())               #Dtype ie info
# print(data.describe())
# print(data.isnull().sum())        #It tell wheather any cotent have null value or not




#4-Handling Duplicate Value in python:-

# data=pd.read_excel("Duplicate.xlsx")
# print(data)
#Drop on bases of Primary Key Only:--
# print(data.drop_duplicates("Emplyee id"))




#5..Working With Missing data in python:
# data=pd.read_excel("Duplicate.xlsx")
# print(data)
# print(data.isnull().sum())  #give sum of no of nul value in column.
# print(data.dropna())   #drop a row if any clumn caary null value.
# print(data.replace(np.nan,"69%"))    #It Replace all nan value 69%
#print(data.fillna(0,inplace=True))
#df.rename(columns={"Customer ID":"Customer_ID","Customer Name":"Customer_Name"},inplace=True)  #RENAME COLUMN NAME.

#What if i want to replace nan only at one column at which nan occur.
# data["Math"]=data["Math"].replace(np.nan,"68%")
# print(data)
# print(data.fillna(method="bfill")) #It fill nan value with nxt value to it.
# print(data.fillna(method="ffill"))  #It fill nan value with value come before to it.





#6--Column Transformation :--
#1--
#It create a new column and give BONUS/No BONUS based on that that it get or not.
# df=pd.read_excel("Duplicate.xlsx")
# df.loc[(df["Math"]<30),"Result"]="Failed"
# df.loc[(df["Math"]>30),"Result"]="Pass"
# print(df)

#2--
# data=pd.read_excel("Duplicate.xlsx")
# data["Full name"]=data["Name"].str.capitalize()+" "+data["last name"]    #IT ceate a new column of full name.
# print(data)

#3--
# data=pd.DataFrame({"Month":["January","Febraury","MArch","April"]})
# def extract(value):
#     return value[0:3]
# data["Short month"]=data["Month"].map(extract)
# print(data)





#7:-Z---Group by in Pandas:--
# df=pd.DataFrame({"EID":[123,123,456,788,456],"Chemistry":["Organic","Inorganic","Inorganic","Organic","Inorganic"],
# "Gender":["Male","Female","Female","Male","Female"]})
# gp=df.groupby("Chemistry").agg({"Gender":"count"})
# gp=df.groupby(["Chemistry","Gender"]).agg({"EID":"count"})  #Similarly for max,min,mean etc:
# print(gp)
 

 #8:--MERGE JOIN AND CONCATENATE IN PANDAS :

#MERGE:----
# CASE:
# CASE:2 if df1 and df2 has different primary key.[it create new dataframe base on commain emplyee id os 1st and 2nd and of 1st not of 2nd 
# df1=pd.DataFrame({"Emp id":["C-101","C-102","C-103","C-104","C-105","C-106"],
#                      "Name":["Amit","Abhay","Anni","Saksham","Raj","Dev"]
#                      ,"Age":[23,54,2,45,67,87]})
# df2=pd.DataFrame({"Emp id":["C-101","C-106","C-103","C-107","C-105","C-108"],
#                    "Salary":[22000,40000,34500,34500,29999,90000]})
# print(pd.merge(left=df1,right=df2,on = "Emp id",how="left"))


#JOIN:--
# df1=pd.DataFrame({"Name":["Sunny","Dev","Mayank"]},index=[1,2,3])
# df2=pd.DataFrame({"Marks":[98,78,89]},index=[1,2,7])
# print(df1.join(df2))
# print(df2.join(df1))
# # print(df2)

#CONCATENATE:---
# df1=pd.DataFrame({"Emp id":["C-101","C-102","C-103","C-104","C-105","C-106"],
#                      "Name":["Amit","Abhay","Anni","Saksham","Raj","Dev"]
#                      ,"Age":[23,54,2,45,67,87]})
# df2=pd.DataFrame({"Emp id":["C-107","C-108","C-109","C-110","C-111","C-112"],
#                      "Name":["Sanjay","Pradeep","Kartik","Devansh","Kalam","poppi"]
#                   ,"Age":[12,13,42,56,65,34]})
# print(pd.concat([df1,df2]))




#9:--Uses of [--loc--] AND [--iloc--] :

#LOC USES:--[--Location by Name--] --(Row,column)=(number,word/Name)
#Loc is used to select row and column by label(name),not by Position.

# df = pd.DataFrame({
#     "Name": ["Sunny", "Dev", "Mayank"],
#     "Marks": [98, 78, 89],
#     "City": ["Delhi", "Mumbai", "Pune"]
# })
# print(df)

#1--Select a Row:-
# print(df.loc[1])

#2--Select Multiple row:--
# print(df.loc[1:2])  #2 and 3 Row.
# print(df.loc[[0,2]])   #1 and 3 Row.

#3--Select Column:--
# print(df.loc[:,"City"])       #Single Column.
# print(df.loc[:,["City","Marks"]])   #Multiple Column.

#4--Multiple Row and Column:--
# print(df.loc[1:2,["Name","City"]])

#5--Filtering Using Condition:--
# print(df.loc[df["Marks"]>85])

#6--Update Value Using loc:--
# df.loc[df["Name"]=="Dev","Marks"]=100
# print(df)

#7-Using loc with Custom Index:--
# df2=df.set_index("Name")
# print(df2)
# print(df2.loc[["Dev","Mayank"]])




#iloc:
#Mean Index Location by Number.--(Row,column)=(number,number)

# df = pd.DataFrame({
#     "Name": ["Sunny", "Dev", "Mayank"],
#     "Marks": [98, 78, 89],
#     "City": ["Delhi", "Mumbai", "Pune"]
# })

#1--Select Row:
# print(df.iloc[1])  #Single Row.
# print(df.iloc[1:3]) #2 and 3 row .iloc exclude end pt.
# print(df.iloc[[0,2]])  #1 and 3 row.

#2-Specific row and column:
# print(df.iloc[1:3,1:3])

#Update Using iloc:
# df.iloc[1,2]="Nanital"
# print(df)





#-10--[-- PANDAS | COMPARE DATAFRAME --]--:

# df1=pd.DataFrame({"Fruit":["Mango","Apple","Orange","Banana"],"Price":[100,120,140,40],"Quantity-(KG)":[2,5,6,2]})
# df2=df1.copy()
# df2.loc[0,"Price"]=80
# df2.loc[1,"Price"]=110
# df2.loc[2,"Price"]=170
# df2.loc[0,"Quantity-(KG)"]=7
# df2.loc[1,"Quantity-(KG)"]=9
# df2.loc[2,"Quantity-(KG)"]=7
# print(df1.compare(df2,align_axis=0))  #Compare Only those value which Changes.--By default axis=1
# print(df1.compare(df2,keep_shape=False))
# print(df1)



#--11--[--Pivoting and Melting DataFrame--]
#-Pivoting mean to Changing Data.ie-row into column or vica versa. For better Analysis.

# df = pd.DataFrame({
#     "Month": ["Jan", "Jan", "Feb", "Feb"],
#     "Product": ["Phone", "Laptop", "Phone", "Laptop"],
#     "Sales": [100, 200, 150, 250]
# })
# print(df)
# print(df.pivot(index="Product",columns="Month",values="Sales"))

#Melting:-Convert column into row:-Opposite of Pivot.
# df=pd.DataFrame({"Name":["john","Ben","David","Peten"],"House":["red","blue","Green","red"],"Grade":["3rd","8th","9th","8th"]})
# print(pd.melt(df,id_vars=["Name"],value_vars=["House","Grade"],var_name="Houses and Grade",value_name="Values"))



#-12:--SORTING-:

# df = pd.DataFrame({
#     "Name": ["Dev", "Aman", "Neha", "Riya", "Rahul"],
#     "Total Mark": [248, 248, 240, 235, 240],
#     "Gender": ["Male", "Male", "Female", "Female", "Male"]
# })
# # print(df)
# print(df.sort_values("Total Mark",ascending=False))  #By default it is True:-
# print(df.sort_values(["Total Mark", "Name"], ascending=[False, True])) #First sorted by Total Mark descending If Total Mark is same → sorted by Name ascending


#-13--[--idmax/idmin--]-
# idxmin() → Returns the index/row label of the minimum value
# idxmax() → Returns the index/row label of the maximum value

# marks = pd.Series([78, 92, 85, 64, 99], index=["Aman", "Dev", "Neha", "Riya", "Rahul"])

# print("Marks:\n", marks)

# print("Highest mark index:", marks.idxmax())
# print("Lowest mark index:", marks.idxmin())


#-14-:--
# to_frame() converts a pandas Series into a DataFrame
# to_string() converts pandas data into plain text for printing
# ie-use it like :--print(df[["Math","Science","English"]].mean().to_frame("Average Marks"))



#15:--
# | Method             | Returns      | Interview-friendly |
# | ------------------ | ------------ | ------------------ |
# | DataFrame + idxmax | Series       | ❌ less clean      |
# | Series + idxmax    | Single value | ✅ best            |
#Series Approach + idxmax:-GIVES SINGLE VALUE
# df.groupby("Region")["PROFIT"].sum().idxmax()

#DATAFRAME + idxmax:-RETURN A SERIES:
#df.groupby("Region").agg({"PROFIT":"sum"}).idxmax()


#To see Columns:-
# print(df.columns)  #GIVE ALL COLUMN NAME.
# print(df.head().T)  #Give all Column nam
#print(df.iloc[:,0:3])  #GIVES COLUMN U WANT BEST WAY.


# df = pd.DataFrame({
#     "Emp_ID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Neha", "Rohit", "Priya", "Karan", "Anjali"],
#     "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
#     "Experience": [2, 5, 3, 7, 1, 4],   
#     "Performance_Score": [78, 88, 65, 92, 55, 81],
#     "Salary": [40000, 55000, 42000, 75000, 38000, 60000]
# })
#Value_Count :-[--COUNT NO HOW MANY TIMES DOES A CATEGORY APPEAR--]
# print(df["Department"].value_counts())

#nunique :-[--COUNT IN DEPARTMENT COLUMN HOW MANY UNIQUE VALUE THERE--]
# print(df["Department"].nunique())

#nlargest/nsmallest :-[--IT SORT ACC TO U WANT HIGHEST __ OR LOWEST __--]
# print(df.nlargest(2,"Salary")[["Name","Salary"]])





