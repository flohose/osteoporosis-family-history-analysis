1.  Background    
My grandmother, on my mother's side, has osteoporosis. We didn't know until she started losing her ability to move freely - her bones were quietly breaking down for years before anyone recognized what was happening. By the time we understood what osteoporosis was, the damage was already done. That experience left me wondering: now that we know it runs in our family, are my siblings, cousins, and I at greater risk? And if family history really does matter, what could we be doing differently, starting now, to lower that risk?
2.  Problem Statement      
In this dataset, do individuals with a family history of osteoporosis have a higher rate of osteoporosis diagnosis than those without one? 
Smaller questions: 
-	Does the gap between the two groups (family history vs. no family history) hold up across different age groups, or is it mainly driven by older individuals?
-	Among individuals with a family history, do those with sufficient calcium/vitamin D intake and regular physical activity have a lower diagnosis rate than those without?
3.  Data      
My data comes from Kaggle: Lifestyle Factors Influencing Osteoporosis. Each row represents one individual, with 1,958 rows and 16 columns. Of the 16 columns, this analysis primarily uses Family History, Age, Osteoporosis (diagnosis status), Calcium Intake, Vitamin D Intake, and Physical Activity.
4.  Analysis      
The original dataset had 16 columns. For this analysis, I kept only the 6 columns needed to answer my questions: Family History, Age, Osteoporosis, Calcium Intake, Vitamin D Intake, and Physical Activity. This reduced the dataset to 1,958 rows and 6 columns.


5.  Visualization     
 
Family History
 In this dataset, people with a family history of osteoporosis were diagnosed at almost the same rate (approximately 50%) as those without one, suggesting family history is not associated with higher diagnosis rates here
 
Family History Across Age Groups 
The gap between family-history groups was small but present under age 40; from age 40 onward, diagnosis rates were near 100% for everyone regardless of family history, suggesting age -not family history- drives the outcome in this dataset.

 
Lifestyle Factors (Among Those with Family History) 
None of the three lifestyle factors meaningfully changed the diagnosis rate because all six groups hovered around 50%, suggesting that in this dataset, lifestyle choices did not offset or influence osteoporosis risk among those with a family history.

 
This output confirms the exact percentages behind Figure 3: calcium intake, vitamin D intake, and physical activity each showed diagnosis rates within 1-2 percentage points of each other, regardless of category.
6.  Conclusion     
In this study I learned that family history of osteoporosis was not associated with a higher diagnosis rate in this dataset. Both groups, with and without family history were diagnosed at nearly identical rates overall -approximately 50%, and this held true within each age group as well: under 40, both groups showed a similarly low rate as approximately 23-24%, from 40 ongoing, both groups showed a rate near 100%. This suggests that age, not family history, is the dominant factor driving diagnosis in this dataset.

Going in, I assumed family history would show at least some independent effect, based on both the clinical literature and my own family's experience. Instead, age appears to overwhelm any family-history signal so completely that by age 40 ongoing, virtually everyone is diagnosed regardless of family background which raises the question of whether this dataset reflects real biological patterns or was generated in a way where age and diagnosis are more tightly linked than family history and diagnosis.

Among individuals with a family history of osteoporosis, lifestyle factors also showed no meaningful association with diagnosis rate: calcium intake (49.8% adequate vs. 50.0% low), vitamin D intake (49.3% insufficient vs. 50.5% sufficient), and physical activity (50.6% active vs. 49.1% sedentary) all produced nearly identical diagnosis rates. This reinforces the pattern seen with family history and age: in this dataset, diagnosis does not appear to be meaningfully driven by any of the behavioral or genetic risk factors typically associated with osteoporosis -age is the one variable that shows a clear relationship.

7.  Limitations     
Because this analysis only compares group percentages, I could not determine whether age itself directly causes higher diagnosis rates, or whether age is simply correlated with something else in the data that better explains the pattern. A crosstab can show that two groups differ, but it cannot isolate which factor is truly driving the outcome when multiple variables (age, family history, lifestyle factors) are considered together. A more advanced statistical model - one built specifically to control for multiple factors at once - would be needed to answer that question with confidence.
