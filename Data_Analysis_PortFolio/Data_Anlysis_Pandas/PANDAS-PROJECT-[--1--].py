# 🔹 Basic Understanding
# View the dataset
# Check column names & data types
# Get basic statistics
# 🔹 Core Analysis
# Add Total Marks column
# Add Average Marks column
# Find the Topper
# Find the Lowest scorer
# 🔹 Performance Analysis
# List students who failed (avg < 60)
# Count how many students failed--------
# Find subject-wise average marks
# 🔹 Group Analysis
# Gender-wise average marks
# Gender-wise topper
# 🔹 Sorting & Filtering
# Sort students by total marks (highest first)
# List students scoring more than 85 in any subject
# 🔹 Thinking Like Analyst (Important)
# Which subject is most difficult? (lowest average)
# Which student is most consistent? (smallest marks difference)


#MINI PROJECT 1: STUDENT PERFORMANCE ANALYZER:-[--🎯Goal Understand the data and answer simple questions using Pandas--]
import pandas as pd
import numpy as np

df= pd.DataFrame({
    "Name": ["Dev", "Aman", "Riya", "Neha", "Rahul"],
    "Math": [78, 85, 67, 33, 56],
    "Science": [72, 88, 70, 95, 60],
    "English": [98, 75, 68, 92, 58],
    "Gender": ["Male", "Male", "Female", "Female", "Male"]
})
print(df)
# --DATA TYPE:
print(df.info())

#Adding new column of Total Mark And Avg Mark:
df["Total Mark"]=df["Math"]+df["Science"]+df["English"]
df["Average Mark"]=round((df["Total Mark"])/3,2)
print(df)

#Toppper and Bottamer:-
print("TOPPER:--")
print(", ".join(df.loc[df["Total Mark"]==df["Total Mark"].max(),"Name"]),"With",df["Total Mark"].max(),"Marks")
print("BOTTAMER:--")
print(df.loc[df["Total Mark"]==df["Total Mark"].min(),"Name"].to_string(index="False"),"\n")


#STUDENT FAILED:-
print("STUDENT FAILED:--")
print(df.loc[df["Average Mark"]<60,"Name"].to_string(index="False"))
print("No of Student Failed :",(df["Average Mark"]<60).sum(),"\n")

#SUBJECT WISE AVERAGE MARKS:-
print(df[["Math","Science","English"]].mean().to_frame("Average Marks"),"\n")

#GENDER WISE TOPPER AND AVERAGE MARKS:--
gp=df.groupby("Gender").agg({"Average Mark":"mean"}).round(2)
print(gp)

#GENDER WISE TOPPER:
male=df[df["Gender"]=="Male"]
female=df[df["Gender"]=="Female"]
male_max=male["Total Mark"].max()
female_max=female["Total Mark"].max()
print("Male Toppper : ",", ".join(male[male["Total Mark"]==male_max]["Name"]))
print("Female Topper:", ", ".join(female[female["Total Mark"] == female_max]["Name"]),"\n")

#SORTING:--
print(df.sort_values("Total Mark",ascending=False),"\n")

#LIST OF STUDENT SCORING MORE THAN 85:-
print("STUDENT SCORE ABOVE 85 :--")
print(df.loc[(df[["Math","Science","English"]]>85).any(axis=1),"Name"].to_string(index=False),"\n")
#MOST CONSISTANT:--
df["Std_dev"]=df[["Math","Science","English"]].std(axis=1).round(2)
print("MOST CONSISTANT :-\n",df.loc[df["Std_dev"]==df["Std_dev"].min(),"Name"].to_string(index=False))