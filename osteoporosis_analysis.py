## Load Libraries for loading, cleaning, and visualizing data && the 2 required figures
import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path

##Step 1: Load and Inspect Data
SCRIPT_DIR = Path(__file__).parent
df = pd.read_csv(SCRIPT_DIR / 'osteoporosis.csv')
print(df.shape)

## I am printing the first 10 rows && checking the data types of each column
## To see ifanything needs to cleaned or changed
df.head(10)
df.info()
df.dtypes

## I will drop all columns that I am not using 
## No data types issues found 

columns_to_keep = ["Family History", "Age", "Osteoporosis",
                 "Calcium Intake", "Vitamin D Intake", "Physical Activity"]

df = df[columns_to_keep]
print(df.shape)
## Main Question: Does family history raise the osteoporosis diagnosis rate?
## Figure 1: Osteoporosis Diagnosis Rate by Family History
main_result = df.groupby("Family History")["Osteoporosis"].apply(
    lambda x: (x == 1).mean() * 100
)
main_result.plot(kind="bar", color=["salmon", "steelblue"])
plt.title("Osteoporosis Diagnosis Rate by Family History")
plt.xlabel("Family History")
plt.ylabel("% Diagnosed with Osteoporosis")
plt.xticks(rotation=0)
plt.savefig("figure1_family_history.png")
plt.show()

## Figure 2: Diagnosis Rate by Family History Across Age Groups
df["Age Group"] = pd.cut(df["Age"], bins=[0, 40, 60, 100], labels=["Under 40", "40-60", "60+"])

age_pivot = df.groupby(["Age Group", "Family History"])["Osteoporosis"].apply(
    lambda x: (x == 1).mean() * 100
).unstack()

age_pivot.plot(kind="bar")
plt.title("Diagnosis Rate by Family History Across Age Groups")
plt.xlabel("Age Group")
plt.ylabel("% Diagnosed with Osteoporosis")
plt.xticks(rotation=0)
plt.legend(title="Family History")
plt.savefig("figure2_age_groups.png")
plt.show()

## Sub-Question 2: Do lifestyle factors offset risk among those with family history?
##Figure 2: Diagnosis Rate by Family Across Age Groups 
fh_only = df[df["Family History"] == "Yes"]

calcium_result = fh_only.groupby("Calcium Intake")["Osteoporosis"].apply(lambda x: (x == 1).mean() * 100)
vitamin_result = fh_only.groupby("Vitamin D Intake")["Osteoporosis"].apply(lambda x: (x == 1).mean() * 100)
activity_result = fh_only.groupby("Physical Activity")["Osteoporosis"].apply(lambda x: (x == 1).mean() * 100)

print("Calcium Intake:")
print(calcium_result)
print()
print("Vitamin D Intake:")
print(vitamin_result)
print()
print("Physical Activity:")
print(activity_result)

## Figure 3:  Lifestyle Factors and Diagnosis Rate (Among Those With Family History)
labels = ['Calcium\n(Adequate)', 'Calcium\n(Low)', 
          'Vitamin D\n(Insufficient)', 'Vitamin D\n(Sufficient)',
          'Activity\n(Active)', 'Activity\n(Sedentary)']
values = [49.78, 50.00, 49.25, 50.51, 50.59, 49.11]

plt.figure(figsize=(9, 5))
plt.bar(labels, values, color='mediumpurple')
plt.title("Diagnosis Rate by Lifestyle Factors (Among Those With Family History)")
plt.ylabel("% Diagnosed with Osteoporosis")
plt.ylim(0, 100)
plt.savefig("figure3_lifestyle_factors.png")
plt.show()

