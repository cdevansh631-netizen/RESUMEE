import pandas as pd
import numpy as np

#MINI PROJECT 4:--[--Sales Performance & Profit Analysis--] :-

#View first & last 3 rows
#Check shape, columns, data types
#Check missing values
#Fill missing Discount with 0
#Check & remove duplicates (if any)
#Create a new column Discount_Flag (Yes / No)
#Create Revenue column
#Create Cost column
#Create Profit column
#Create Profit_Margin (%)
#Total Revenue & Total Profit
#Product-wise total profit
#Region-wise average profit
#Top profit product
#Least profitable region
#Orders where Profit < 20,000
#Orders with Profit_Margin > 30%
#Sort orders by Profit (descendingOrders where Profit < 20,000
#Orders with Profit_Margin > 30%
#Sort orders by Profit (descending)
#Extract Year & Month
#Month-wise total sales
#Best month by profit
#Customer-wise total profit
#Which product sells best in North region?
#Does discount reduce profit? (logic answer)
df = pd.DataFrame({ 
    "Order_ID": [101,102,103,104,105,106,107,108,109,110],
    "Order_Date": [
        "2023-01-05","2023-01-15","2023-02-10","2023-02-20",
        "2023-03-05","2023-03-18","2023-04-02","2023-04-25",
        "2023-05-10","2023-05-28"
    ],
    "Customer": ["Amit","Neha","Ravi","Amit","Pooja","Neha","Ravi","Amit","Pooja","Neha"],
    "Product": ["Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop","Mobile","Tablet","Laptop"],
    "Category": ["Electronics"] * 10,
    "Region": ["North","South","East","West","North","South","East","West","North","South"],
    "Units_Sold": [2,3,1,4,5,2,3,4,2,1],
    "Selling_Price": [60000,20000,30000,62000,21000,29000,61000,20500,29500,60000],
    "Cost_Price": [45000,15000,22000,47000,16000,23000,46000,15500,22500,45000],
    "Discount": [0,5,np.nan,10,0,5,np.nan,10,0,5]
})


#OVERVIEW:-
print(df.head(3),"\n")
print(df.tail(3),"\n")

#CHECKING OF SHAPE,COLUMN AND DATATYPE:-
print(df.info(),"\n")
print("(ROW,COLUMN):",df.shape,"\n")

#MISSING VALUES:-
print(df.isnull().sum(),"\n")

#REMOVE DUPLICACY (IF ANY):-
df.drop_duplicates("Order_ID",inplace=True)

#REPLACE NAN VALUE IN DISCOUNT WITH 0:-
df.replace(np.nan,0,inplace=True)

#DISCOUNT FLAG:-
df.loc[df["Discount"]>0,"Discount_Flag"]="YES"
df.loc[df["Discount"]==0,"Discount_Flag"]="NO"

#REVENUE COLUMN:-
df["REVENUE"]=df["Units_Sold"]*df["Selling_Price"]
#COST COLUMN:-
df["COST"]=df["Units_Sold"]*df["Cost_Price"]
#PROFIT_COLUMN:-
df["PROFIT"]=df["REVENUE"]-df["COST"]
#PROFIT_MARGIN COLUMN:-
df["PROFIT_MARGIN"]=((df["PROFIT"]/df["COST"])*100).round(2)

#TOTAL REVENUNE / TOTAL PROFIT :-
print("TOTAL PROFIT :",df["PROFIT"].sum())
print("TOTAL REVENUE :",df["REVENUE"].sum(),"\n")

#PRODUCT WISE TOTAL PROFIT :-
print("PRODUCT WISE TOTAL PROFIT :-")
print(df.groupby("Product").agg("PROFIT").sum(),"\n")

#REGION WISE AVERAGE PROFIT :
print("REGION WISE AVERAGE PROFIT :-")
print(df.groupby("Region").agg({"PROFIT":"mean"}),"\n")

#TOP PROFIT PRODUCT:-
print("TOP PROFIT PRODUCT :-")
print(df.groupby("Product")["PROFIT"].sum().idxmax(),"\n")

#LEAST PROFITABLE REGION:-
print("LEAST PROFITABLE REGION :-")
print(df.groupby("Region")["PROFIT"].sum().idxmin(),"\n")

#ORDER WHERE PROFIT<20,000 :-
print("ORDER WHERE PROFIT < 20,000 :-",)
print(df.loc[(df["PROFIT"]<20000),"Order_ID"].to_string(index=False),"\n")

#ORDER WHERE PROFIT _MARGIN > 30 :-
print("ORDER WHERE PROFIT MARGIN >30 :-")
print(df.loc[df["PROFIT_MARGIN"]>30,"Order_ID"].to_string(index=False),"\n")

#SORTING BY PROFIT :-
print(df[df["PROFIT"]<20000].sort_values("PROFIT",ascending=False))

#EXTRACT YEAR AND MONTH:-
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
df["YEAR"]=df["Order_Date"].dt.year
df["Month"]=df["Order_Date"].dt.month
df["Month_Name"]=df["Order_Date"].dt.month_name()
print(df[["Order_Date","YEAR","Month","Month_Name"]],"\n")

#MONTH WISE TOTAL SALE:-
print("MONTH WISE TOTAL SALE :-")
print(df.groupby(df["Month"]).agg({"REVENUE":"sum"}),"\n")

#BEST MONTH PROFIT :-
print("BEST MONTH PROFIT :-")
print(df.groupby(df["Month"])["PROFIT"].sum().idxmax(),"\n")

#CUSTOMER WISE TOTAL PROFIT :-
print("CUSTOMER WISE TOTAL PROFIT :-")
print(df.groupby("Customer").agg({"PROFIT":"sum"}),"\n")

#STAR PRODUCT OF NORTH REGION:-
print("STAR PRODUCT OF NORTH REGION :-")
print(df[df["Region"]=="North"].groupby("Product")["PROFIT"].sum().idxmax(),"\n")

#CRITERIA COLUMN:-
# print(df[["Discount","PROFIT"]].head())
print(df.groupby("Discount")["PROFIT"].mean().sort_index().to_string())
print("BY ANALYZING WE CAN SAY THAT PROFIT GOES DOWN IF WE GIVE LOW DISCOUNT BUT IF DISOUNT INCREASE TO HIGHER DISCOUNT THEN PROFIT ALSO INCREASE.")
