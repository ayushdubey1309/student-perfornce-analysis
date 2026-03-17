#load the data sheet 
import pandas as pd

df = pd.read_csv("/home/bog/day1/StudentsPerformance.csv")

print ("first 5 row of data sheet")

print(df.head())


print("\n shape of data sheet")
print(df.shape)

print("\n column of data sheet")
print(df.columns.tolist())



# data Analysis
#avrage score

print("avrage score")
print("math:" ,df ['math score'] .mean(), round(2))
print("reading",df['reading score'].mean(),round(2))
print("writing" ,df ['writing score'].mean(),round(2))

#who score better Male of Female

print("\n score by gendder")
print(df.groupby('gender') [['math score', 'reading score' , 'writing score']].mean().round(2))


#does test prepration help

print("\n    impect of test prepration cource")
print(df.groupby("test preparation course")[['math score', 'reading score', 'writing score']].mean().round(2))


#top 5 student name

print("  Top 5 scores")
print(df.nlargest (5, 'math score') [['gender' , 'math score' , 'reading score' , 'writing score']])
      

