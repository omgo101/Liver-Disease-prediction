# Project Title
## Liver Disease Prediction using Logistic Regression

### Table of Contents
<ins> **Introduction** </ins> <br />
<ins> **Technologies** </ins> <br />
<ins>**Dataset** </ins> <br />
<ins>**Files** </ins> <br />
<ins> **Deployment**  </ins> <br />
### Introduction
This project aims to predict the occurrence of liver disease in patients using logistic regression. Logistic regression is a popular method for binary classification problems where the response variable has only two values (e.g., yes/no or 0/1). In this project, we use logistic regression to predict the presence or absence of liver disease based on various factors such as age, sex, and blood test results.

### Technologies
The project was implemented using the following technologies:

Python 3.9.2 <br />
Streamlit 1.4.0 <br />
Scikit-learn 0.24.2 <br />
Pandas 1.2.4 <br />
Numpy 1.20.3 <br />
Matplotlib 3.4.2 <br />
Seaborn 0.11.1 <br />
### Dataset
**Data Set Details**: The number of instances (rows) in the data set is 615, and the number of variables (columns) is 13. Nearly all input variables are numeric-valued except one, Sex, which is binary, and most of them represent measurements from blood and urine analysis. The following list summarizes the variables information:
**category(diagnose)**: No disease, suspect disease, hepatitis c, fibrosis or cirrhosis.<br />
**age**: (0-100). The normal ranges change depending on the age.<br />
**sex**: (f or m). The normal ranges change depending on the sex.<br />
**albumin:** (normal range 34-54g/L). A blood albumin level below normal may be a sign of kidney disease or liver disease as Hepatisis o Cirrhosis.<br />
**alkaline_phosphatase**: (40-129 U/L). It is an alkaline phosphatase test to check for liver disease or liver damage. The main causes or conditions that can cause normal levels to rise is liver disease.<br />
**alanine_aminotransferase**: (7-55 U/L). Alanine aminotransferase or ALT is an enzyme found primarily in the liver. An elevated amount indicates liver damage from hepatitis, infection, cirrhosis, liver cancer, or other liver diseases. <br />
**aspartate_aminotransferase**: (8-48 U/L). It is an enzyme found primarily in the liver, but also in the muscles. Elevated levels of AST in the blood may indicate hepatitis, cirrhosis, mononucleosis, or other liver diseases. <br />
**bilirubin**: (1-12 mg/L). It is a yellowish substance that forms during the normal process of breaking down red blood cells in the body. Lower-than-normal bilirubin levels are generally not a concern. Elevated levels may indicate liver disease or damage. <br />
**cholinesterase**: (8-18 U/L). It is a blood test that studies the levels of 2 substances that help the nervous system to function properly. Cholinesterase deficiency causes liver disease, renal disease... <br />
**cholesterol**: (Less than 5,2 mmol/L). Cholesterol is a waxy, fat-like substance found in every cell in your body. A high level could cause carotid artery disease, stroke, and peripheral artery disease... <br />
**creatinina**: (61.9-114.9 ??mol/L for m and 53-97.2 ??mol/L for f). It measures the level of creatinine in the blood. High level of creatinine in the blood and low level in the urine indicate kidney disease or affecting the function of the kidneys <br />
**gamma_glutamyl_transferase** : (from 0 to 30-50 IU/L.). It is an enzyme that indicates cholestasis. The higher the level of GGT, the greater the level of liver damage. <br />
**protein**: (Less than 80 mg). It measures the amount of protein in the urine. If protein levels in the urine are elevated, this could indicate kidney damage or another medical problem. <br />

### Files
**r1.py**: This file contains the code for the Streamlit app used to deploy the model.<br />
**project_2.ipynb**: This file contains the code used to perform exploratory data analysis (EDA), visualize the data, evaluate the logistic regression model, and select the final model.<br />

### Presentation
A presentation on this project can be found in ds_project.ppt. <br />
### Deployment
The logistic regression model is deployed using a Streamlit app. To run the app, navigate to the project directory in the command prompt and run the following command:streamlit run file location(r1.py) <br />
The app will open in a web browser, where the user can input the required parameters and obtain a prediction for the presence or absence of liver disease. <br />
