# MINI PROJECT 3:--[--PRODUCT SALES AND PROFIT ANALYZER--]:--

#1-> View the dataset.
#2-> Check data types
#3-> Get basic statistics
#4-> Add Revenue column
#5-> Add Cost Column
#6-> Add profit column
#7-> Add Profit Margin.
#8-> Find Top Profit Product
#9-> Find Lowest Profit Product
#10-> List products with Profit < 50,000
#11-> Count how many low-profit entries
#12-> Category-wise total revenue
#13-> Product-wise average profit
#14-> Region-wise top profit product
#15-> Sort orders by Profit (descending)
#16-> List orders where Profit_Margin > 25%
#17-> Which product is most profitable overall?
#18-> Which region is least profitable?
#19-> Which product gives best value for money?




import pandas as pd

df = pd.DataFrame({
    "Order_ID": [201, 202, 203, 204, 205, 206, 207, 208],
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Units_Sold": [5, 10, 6, 4, 12, 7, 3, 9],
    "Selling_Price": [60000, 20000, 30000, 62000, 21000, 29000, 61000, 20500],
    "Cost_Price": [45000, 15000, 22000, 47000, 16000, 23000, 46000, 15500]
})

#DATA TYPE:--
print(df.info(),"\n")

#REVENUE COLUMN:--
df.loc[:,"REVENUE"]=df.loc[:,"Units_Sold"]*df.loc[:,"Selling_Price"]

#COST COLUMN:--
df.loc[:,"COST"]=df.loc[:,"Units_Sold"]*df.loc[:,"Cost_Price"]

#PROFIT COLUMN:--
df.loc[:,"PROFIT"]=df.loc[:,"REVENUE"]-df.loc[:,"COST"]

#PROFIT MARGIN COLUMN:--
df.loc[:,"PROFIT MARGIN"]=((df.loc[:,"PROFIT"]/df.loc[:,"REVENUE"])*100).round(2)

# #TOP/LOW PROFIT PRODUCT:--
print("TOP PROFIT PRODUCTS :",df.groupby("Product")["PROFIT"].sum().idxmax())
print("LOW PROFIT PRODUCT :",df.groupby("Product")["PROFIT"].sum().idxmin(),"\n")

#PRODUCT WITH PROFIT LESS THAN 50000:-
print("PRODUCT WITH PROFIT LESS THAN 50000:--")
print(df.loc[df["PROFIT"]<50000,["Product","Region"]].to_string(index=False),"\n")

#LOW PROFIT ENTERIES:-
print("NUMBER OF LOW PROFIT ENTRIES:--")
print(df.loc[df["PROFIT"]<50000,["Product"]].count().to_string(index=False),"\n")

#CATEGORY WISE TOTAL REVENUE:-
print("CATEGORY WISE TOTAL REVENUE:--")
print(df.groupby("Category").agg({"REVENUE":"sum"}),"\n")

# PRODUCT WISE AVERAGE PROFIT:--
print("PRODUCT WISE AVERAGE PROFIT:--")
print(df.groupby("Product").agg({"PROFIT":"mean"}).round(2),"\n")

#Region Wise Top Profit Product:--
print("Region Wise Top Profit Product:--")
print(df.loc[df.groupby("Region")["PROFIT"].idxmax(),["Region","Product"]].to_string(index=False),"\n")

#SORTED ORDER OF PROFIT:--
print(df.sort_values("PROFIT",ascending=False),"\n")

#ORDER ID WHERE PROFIT MARGIN >25.:---
print("ORDER ID WHERE PROFIT MARGIN >25:-")
print(df.loc[(df["PROFIT MARGIN"]>25),"Order_ID"].to_string(index=False),"\n")

#MOST PROFITABLE PRODUCT:--
print("MOST PROFITABLE PRODUCT:-")
print(df.loc[df["PROFIT MARGIN"]==df["PROFIT MARGIN"].max(),"Product"].to_string(index=False),"\n")

#REGION WITH LEAST PROFIT:- 
print("REGION WITH LEAST PROFIT :-")
print(df.groupby('Region')["PROFIT"].sum().idxmin(),"\n")

#BEST VALUE FOR MONEY:--
#HERE FOR SELLER VALUE FOR MONEY PRODUCT WHERE RATIO OF PROFIT:Units_sold higher as possible:-
print("BEST VALUE FOR MONEY PRODUCT FOR SELLER:-")
df["Profit:Units_Sold"]=(df["PROFIT"]/df["Units_Sold"]) 
print(df.groupby("Product")["Profit:Units_Sold"].max().idxmax())

