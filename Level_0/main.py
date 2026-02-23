import os
import pandas as pd
import matplotlib.pyplot as plt

DF = pd.read_csv('data.csv', na_values=[" ", "NAN", "null", "nan", "NaN"])


### convert string to date time
DF['Hire Date'] = pd.to_datetime(DF['Hire Date'])

### fill empty data with avg of their respective column
# DF.fillna(avg_age, inplace=True)

### Column-wise modifying
DF['Age'] = DF['Age'].fillna(DF['Age'].mean())


### column names
def column_names():
    columns = DF.columns.tolist()
    print(f"The columns in the given Data: ")
    for col in columns:
        print(col)

###number of col and rows
def col_row():
    rows , col = DF.shape
    print(f"Rows: {rows}")
    print(f"Columns: {col}")


# welocome
print("-------------  Welcome to the Data Analyzer with a demo data:  ---------\n")
print("*"*111)

# display columns and rows
col_row()

print("*"*111)

# display column names
column_names()

print("*"*111)

### show all duplicates
print(F"There are {DF.duplicated().sum()} duplicates in the data, those are:")
print(DF[DF.duplicated()])

print("*"*111)

# display missing values
def missing():
    for col in DF.columns:
        if DF[col].isnull().sum() != 0:
            print(f"The missing or null values in the {col} are: ")
            ms = DF[DF[col].isnull()]
            print(ms)
            print(" "*10 + "~"*60)
missing()

print("*"*111)

# display min, max and mean
min = DF['Salary'].min()
max = DF['Salary'].max()
mean = DF['Salary'].mean()
print(f"Minimum Salary: ${min}/-")
print(f"Maximum Salary: ${max}/-")
print(f"Average Salary: ${mean}/-")

print("*"*111)

# histogram and bar chart 
# make a folder named graphs, if doesn't exist
os.makedirs("graphs", exist_ok=True)
#1 salary v/s name
plt.barh(DF['Name'], DF['Salary'], color='purple')
plt.xlabel("Salary of the Employee")
plt.ylabel("Name of the Employee")
plt.title("salary v/s employee")
plt.savefig("graphs/sal_emp.png", dpi=310, bbox_inches="tight")
plt.show()

#2 graph by age
plt.hist(DF['Age'], bins=10)
plt.xlabel("Age of an Employee")
plt.ylabel("Number of Employees")
plt.title("Number of Employees belonging to that Age")
plt.savefig("graphs/age_count.png", dpi=310, bbox_inches="tight")
plt.show()

print("Graphs of Salary v/s Name and Graph by Age is saved in Graphs folder:")

print("*"*111)
