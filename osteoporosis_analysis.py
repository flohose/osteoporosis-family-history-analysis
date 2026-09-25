## Load Libraries - loading, cleaning, and visualizing data && the 2 required figures
import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path

##Step 1: Load and Inspect Data
SCRIPT_DIR = Path(__file__).parent
df = pd.read_csv(SCRIPT_DIR / 'osteoporosis.csv')
print(df.shape)

## I am printing the first 10 rows 
## I am hecking the data types of each column
## I will get To know if I need to clean/ change the data types
df.head(10)
df.info()
df.dtypes

## I will drop colums that I am not using 
## No data types to fix

columns_to_keep = ["Family History", "Age", "Osteoporosis",
                 "Calcium Intake", "Vitamin D Intake", "Physical Activity"]

df = df[columns_to_keep]
print(df.shape)

## Diagonosis Rate by Familty History -Main Question 


## Does the Gap Hold Across Age Groups?

## Do Lifestyle Factors Influence the Gap?

## Figure 1: Diagnosis Rate by Family History

##Figure 2: Diagnosis Rate by Age Group and Family History