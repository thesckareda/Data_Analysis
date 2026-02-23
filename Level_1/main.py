import pandas as pd
import matplotlib.pyplot as plt

DF = pd.read_csv('data.csv')

# welocome
print("-------------  Welcome to the Data Analyzer(level_2) with a demo data:  ---------")
print("***type 'end' to stop the application***")
print("-"*111)

### convert string to date time
DF['Hire Date'] = pd.to_datetime(DF['Hire Date'])

### changing null values to average of the respective column
DF['Age'] = DF['Age'].fillna(DF['Age'].mean())
DF['Salary'] = DF['Salary'].fillna(DF["Salary"].mean())
DF['Performance Score'] = DF['Performance Score'].fillna(DF['Performance Score'].mean())

### deleting all duplicates with identical names
DF.drop_duplicates(subset=['Name'], inplace=True)      # inplace=True is used to change the original dataframe

### average of age
def avg_age():
    avg_age = DF['Age'].mean()
    print(f"Average age is: {avg_age}")


### average of salary
def avg_salary():
    avg_sal = DF['Salary'].mean()
    print(f"Average Salary is {avg_sal} ruppees.")

### column names
def column_names():
    columns = DF.columns.tolist()
    print(f"The columns are: ")
    for col in columns:
        print(col)


### Sort by Salary
def sort_sal():
    salary_des = DF.sort_values(by='Salary', ascending=False)
    print(salary_des[['Name', 'Salary']].reset_index(drop=True))

### Graph of Salary
def graph_salary_emp():
    plt.barh(DF['Name'], DF['Salary'], color='purple')
    plt.xlabel("Salary of the Employee")
    plt.ylabel("Name of the Employee")
    plt.title("salary v/s employee")
    plt.show()

### Graph by performance score
def graph_score():
    plt.barh(DF['Name'], DF['Performance Score'], color='green')
    plt.xlabel("Performance Score of the Employee")
    plt.ylabel("Name of the Employee")
    plt.title("Analysis of Employee's Performance Score")
    plt.show()

### Sort by Performance Score
def sort_performance():
    performance_order = DF.sort_values(by='Performance Score', ascending=False)
    print(performance_order[['Name', 'Performance Score']].reset_index(drop=True))


### Sort by Hire Date
def sort_hire_date():
    hire_date = DF.sort_values(by='Hire Date')
    print(hire_date[['Name', 'Hire Date']].reset_index(drop=True))

### total data
def data():
    print(DF)

### information of the functions
def info():
    print("You can retrieve rows, columns, data, average salary or, age, sort by performance or, salary and plots. ")

over = True

while(over):
    query = str(input("Enter the query(only one function at a time, enter 'info' to know): ")).lower()

    if "column" in query and "name" in query:
        column_names()

    elif "size" in query and "data" in query:
        print(f"Rows and Columns are {DF.shape} respectively.")

    elif "data" in query:
        data()
    
    elif "average" in query and "salary" in query:
        avg_salary()

    elif "average" in query and "age" in query:
        avg_age()

    elif "sort" in query and "salary" in query:
        sort_sal()

    elif "sort" in query and "performance" in query:
        sort_performance()

    elif "sort" in query and "hir" in query:
        sort_hire_date()
        
    elif "employee" in query and "salary" in query:
        graph_salary_emp()

    elif "employee" in query and "performance" in query:
        graph_score()

    elif "info" in query:
        info()

    elif "end" in query:
        over = False
    
    else: 
        print("Oops! It is not a valid function or we are working on it.")
    
    print("-"*111)

        