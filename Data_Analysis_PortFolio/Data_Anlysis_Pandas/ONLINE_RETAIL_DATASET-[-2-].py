#ONLINE_RETAIL_DATASET-[--2--]

import pandas as pd

df=pd.read_csv("online_retail.csv")


#DATA UNDERSTANDING :-

print(df.columns,"\n")
print(df.head(),"\n")
print(df.tail(),"\n")
print(df.info(),"\n")
print(df.describe(include="object"),"\n")
print("(ROWS,COLUMN) :",df.shape)


#DATA HANDLING:-

print(df.isnull().sum())
df.dropna(inplace=True)  #DROP ALL ROW IF THERE IS NULL VALUE :-
df.drop_duplicates("InvoiceNo",inplace=True)
df.rename(columns={"InvoiceDate":"Invoice_Date"},inplace=True)
df["Invoice_Date"]=pd.to_datetime(df["Invoice_Date"])
df["MONTH"]=df["Invoice_Date"].dt.month
df["YEAR"]=df["Invoice_Date"].dt.year
df=df.loc[~df["InvoiceNo"].astype(str).str.startswith("C")]

#ORDER AMOUNT COLUMN :-
df["Order_Amount"]=df["Quantity"]*df["UnitPrice"]

#YEAR WISE TOTAL SALES :-
print("YEAR WISE TOTAL SALES :-")
print(df.groupby(df["YEAR"]).agg({"Order_Amount":"sum"}),"\n")
print("BEST YEAR FOR SALE :-")
print(df.groupby(df["YEAR"])["Order_Amount"].sum().idxmax(),"\n")

#MONTH WISE TOTAL SALES:-
print("MONTH WISE TOTAL SALES :-")
print(df.groupby(df["MONTH"]).agg({"Order_Amount":"sum"}),"\n")
print("BEST MONTH FOR SALES :-")
print(df.groupby(df["MONTH"])["Order_Amount"].sum().idxmax(),"\n")

#NUMBERS OF PRODUCTS :-
print("NUMBERS OF PRODUCTS :-")
print(df["Description"].nunique(),"\n")

#NO OF TIMES SOLD:-
print(df["InvoiceNo"].value_counts(),"\n")


#MOST SELLING PRODUCT :-
print("MOST SELLING PRODUCT :-")
print(df.groupby("Description")["Quantity"].sum().idxmax(),"\n")
print("LEAST SELLING PRODUCT :-")
print(df.groupby("Description")["Quantity"].sum().idxmin(),"\n")

#COUNTRY WITH MOST SALES :-
print("COUNTRY WITH MOST SALES :-")
print(df.groupby("Country")["Quantity"].sum().idxmax(),"\n") 
print("COUNTRY WITH least SALES :-")
print(df.groupby("Country")["Quantity"].sum().idxmin(),"\n") 

#MOST EXPENSIVE AND CHEAPEST PRODUCT :-
print("MOST EXPENSIVE PRODUCT :-")
print(df.loc[df["UnitPrice"]==df["UnitPrice"].max(),"Description"].to_string(index=False),"\n")
print("CHEAPEST PRODUCT :-")
print(df.loc[df["UnitPrice"]==df["UnitPrice"].min(),"Description"].to_string(index=False),"\n")

#TOP 3 WITH MOST SALE:-
print(df.nlargest(3,"Order_Amount")[["InvoiceNo","Description","Order_Amount"]],"\n")

#BIGGEST ORDER GIVEN BY:-
print("BIGGEST ORDER GIVEN BY:-")
print(df.loc[df["Order_Amount"]==df["Order_Amount"].max(),["CustomerID"]])








 