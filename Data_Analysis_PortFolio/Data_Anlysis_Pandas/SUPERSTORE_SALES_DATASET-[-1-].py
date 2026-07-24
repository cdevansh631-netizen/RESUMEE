#1ST KAGGLE DATASET.-[--SUPERSTORE_SALES_DATASET--] :-
import pandas as pd
 
df=pd.read_csv("train.csv")
print(df.columns)

# UNDERSTANDING DATA:-
print(df.head())
print(df.tail())
print("NDERSTANDING DATA:-","\n")
print("COLUMNS :-",df.columns,"\n")
print("DATA TYPE :-",df.info(),"\n")
print(df.describe(include="object"))
print("(ROWS,COLUMN) :-",df.shape,"\n")



# DATA HANDLING :-
print(df.isnull().sum())
print(df.fillna(14231,inplace=True),"/n") #fill null postal code with 14321.
df.drop_duplicates("Order ID",inplace=True) #Remove Duplicacy.
df["Order Date"]=pd.to_datetime(df["Order Date"],dayfirst=True)
df["MONTH"]=df["Order Date"].dt.month
df["YEAR"]=df["Order Date"].dt.year
df.rename(columns={"Customer ID":"Customer_ID","Customer Name":"Customer_Name"},inplace=True)
print(df.info(),"\n")

#SORTING ACC TO HIGHEST SALE PRODUCT TO LOWEST :-
print("SORTING FROM HIGHEST SALE PRODUCT TO LOWEST :-")
print(df.sort_values("Sales",ascending=False),"\n")

#MOST LOYAL CUSTOMER-WHO SPEND MOST MONEY :-
print("MOST LOYAL CUSTOMER :",df.groupby("Customer_Name")["Sales"].sum().idxmax(),"\n")

#STAR CATEGORY,SUB CATEGORY,STAR PRODUCT-MOST SALE CATEGORY:-
print("STAR CATEGORY :",df.groupby("Category").size().idxmax())
print("STAR SUBCATEGORY :",df.groupby("Sub-Category").size().idxmax(),"\n")
print("STAR PRODUCT :",df.groupby("Product Name").size().idxmax(),"\n")

#CHEAPEST AND COSTLIST PRODUCT :-
print("CHEAPEST SALED PRODUCT :",df.groupby("Product Name")["Sales"].max().idxmin())
print("COSTLIAST SALED PRODUCT :",df.groupby("Product Name")["Sales"].max().idxmax(),"\n")

#REGION WISE TOP CATEGORY :-
X=df.groupby(["Region","Category"]).size().reset_index(name="Order")
Y=X.sort_values("Order",ascending=False).drop_duplicates("Region")
print(Y,"\n")

#PRODUCT WITH SALES>1499 :-
print(df.loc[(df["Sales"]>1499),["Product Name"]],"\n")

#MONTH/YEAR WISE TOTAL SALES:-
print("MONTH WISE TOTAL SALES:-")
print(df.groupby(df["MONTH"]).agg({"Sales":"sum"}).round(2),"\n")
print("YEAR WISE TOTAL SALES :-")
print(df.groupby(df["YEAR"]).agg({"Sales":"sum"}).round(2),"\n")

#BEST MONTH AND YEAR IN TERM OF SALES:-
print("BEST MONTH IN TERM OF SALES:-")
print(df.groupby("MONTH")["Sales"].sum().idxmax(),"th  MONTH")
print("BEST YEAR IN TERM OF SALES:-")
print(df.groupby("YEAR")["Sales"].sum().idxmax(),"YEAR","\n")
