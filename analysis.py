import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_salaries():
    """
    Function to analyze and visualize employee salaries from a CSV file.
    The user will input the file path once, and it will be reused.
    """
    
    # Load data from CSV file
    df = pd.read_csv("employee_data.csv")
    
    # Check if required columns exist
    required_columns = {'EmployeeID', 'Age', 'Department', 'Experience', 'Salary'}
    if not required_columns.issubset(df.columns):
        print("Error: CSV file must contain columns: EmployeeID, Age, Department, Experience, Salary")
        return
    
    # Calculate overall statistics
    avg_salary = df['Salary'].mean()
    max_salary = df['Salary'].max()
    min_salary = df['Salary'].min()
    
    # Calculate department-wise average salary
    dept_avg_salary = df.groupby('Department')['Salary'].mean()
    
    # Display results
    print("\nEmployee Salary Analysis:")
    print(f"Total Employees: {len(df)}")
    print(f"Average Salary: {avg_salary:.2f}")
    print(f"Highest Salary: {max_salary}")
    print(f"Lowest Salary: {min_salary}")
    print("\nDepartment-wise Average Salary:")
    print(dept_avg_salary)
    
    # Visualization
    plt.figure(figsize=(10, 5))
    sns.barplot(x=dept_avg_salary.index, y=dept_avg_salary.values, palette='viridis')
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    plt.title("Average Salary by Department")
    plt.xticks(rotation=45)
    plt.show()
    
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Salary'], bins=10, kde=True, color='blue')
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.title("Salary Distribution")
    plt.show()
    
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=df['Experience'], y=df['Salary'], hue=df['Department'], palette='deep')
    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.title("Salary vs Experience")
    plt.legend(title='Department')
    plt.show()

# Run the analysis function
analyze_salaries()
