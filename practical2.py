import pandas as pd

# Student data
data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Rohan", "Kavya", "Arjun", "Simran"],
    "Department": ["BCA", "BCA", "MCA", "BCA", "MCA", "MCA", "BCA", "MCA"],
    "Age": [20, 21, 22, 20, 23, 22, 21, 24],
    "Marks": [85, 92, 67, 78, 88, 95, 55, 73]
}

df = pd.DataFrame(data)

# Q1. Display the complete DataFrame
print("\nQ1. Complete DataFrame")
print(df)

# Q2. Display the first 3 records
print("\nQ2. First 3 records")
print(df.head(3))

# Q3. Display the last 2 records
print("\nQ3. Last 2 records")
print(df.tail(2))

# Q4. Find the number of rows and columns
print("\nQ4. Number of rows and columns")
print(df.shape)

# Q5. Display all column names
print("\nQ5. Column names")
print(df.columns)

# Q6. Display the data types of all columns
print("\nQ6. Data types")
print(df.dtypes)

# Q7. Display only the Name column
print("\nQ7. Name column")
print(df["Name"])

# Q8. Display Name and Marks
print("\nQ8. Name and Marks")
print(df[["Name", "Marks"]])

# Q9. Students who scored more than 80
print("\nQ9. Marks more than 80")
print(df[df["Marks"] > 80])

# Q10. Students who scored less than 70
print("\nQ10. Marks less than 70")
print(df[df["Marks"] < 70])

# Q11. Students whose marks are between 70 and 90
print("\nQ11. Marks between 70 and 90")
print(df[df["Marks"].between(70, 90)])

# Q12. Students belonging to the BCA department
print("\nQ12. BCA students")
print(df[df["Department"] == "BCA"])

# Q13. MCA students who scored more than 80
print("\nQ13. MCA students with marks above 80")
print(df[(df["Department"] == "MCA") & (df["Marks"] > 80)])

# Q14. Students whose age is greater than 21
print("\nQ14. Age greater than 21")
print(df[df["Age"] > 21])

# Q15. Average marks
print("\nQ15. Average marks")
print(df["Marks"].mean())

# Q16. Maximum marks
print("\nQ16. Maximum marks")
print(df["Marks"].max())

# Q17. Minimum marks
print("\nQ17. Minimum marks")
print(df["Marks"].min())

# Q18. Median marks
print("\nQ18. Median marks")
print(df["Marks"].median())

# Q19. Number of students who scored above 75
print("\nQ19. Students scoring above 75")
print((df["Marks"] > 75).sum())

# Q20. Average marks of BCA students
print("\nQ20. Average marks of BCA students")
print(df.loc[df["Department"] == "BCA", "Marks"].mean())

# Q21. Average marks of MCA students
print("\nQ21. Average marks of MCA students")
print(df.loc[df["Department"] == "MCA", "Marks"].mean())

# Q22. Highest-scoring student
print("\nQ22. Highest-scoring student")
print(df.loc[df["Marks"].idxmax()])

# Q23. Add a Bonus column with 5 marks for every student
print("\nQ23. Add Bonus column")
df["Bonus"] = 5
print(df)

# Q24. Create FinalMarks
print("\nQ24. FinalMarks column")
df["FinalMarks"] = df["Marks"] + df["Bonus"]
print(df[["Name", "Marks", "Bonus", "FinalMarks"]])

# Q25. Create Result column
print("\nQ25. Result column")
df["Result"] = df["Marks"].apply(lambda marks: "Pass" if marks >= 40 else "Fail")
print(df[["Name", "Marks", "Result"]])

# Q26. Create Grade column
print("\nQ26. Grade column")
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    return "D"

df["Grade"] = df["Marks"].apply(get_grade)
print(df[["Name", "Marks", "Grade"]])

# Q27. Sort students from highest to lowest marks
print("\nQ27. Students sorted by marks")
print(df.sort_values("Marks", ascending=False))

# Q28. Display the top 3 students
print("\nQ28. Top 3 students")
print(df.nlargest(3, "Marks"))

# Q29. Add a Rank column based on marks
print("\nQ29. Rank column")
df["Rank"] = df["Marks"].rank(ascending=False, method="min").astype(int)
print(df[["Name", "Marks", "Rank"]].sort_values("Rank"))

# Q30-Q33. Group analysis by department
print("\nQ30-Q33. Department-wise analysis")
print(df.groupby("Department")["Marks"].agg(["count", "mean", "max", "min"]))

# Challenge: Create a merit list and export it to Excel
print("\nChallenge. Final merit list")
merit_list = df[["RollNo", "Name", "Department", "Marks", "Grade", "Result", "Rank"]].copy()
merit_list = merit_list.sort_values("Marks", ascending=False)
merit_list = merit_list[["Rank", "RollNo", "Name", "Department", "Marks", "Grade", "Result"]]
print(merit_list)

merit_list.to_excel("student_merit_list.xlsx", index=False)
print("\nMerit list saved as student_merit_list.xlsx")
