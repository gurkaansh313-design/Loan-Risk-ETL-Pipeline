import pandas as pd

df = pd.read_csv("loan_risk_data.csv")

print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()

df = df.drop_duplicates()

df = df.drop(df[df["Income"] <= 0].index)

df['RiskCategory'] = df['CreditScore'].apply(
    lambda x: 'High Risk' if x < 600 else 'Low Risk'
)

df['LoanDecision'] = df.apply(
    lambda row: 'Reject'
    if row['CreditScore'] < 600 or row['Income'] < 30000
    else 'Approve',
    axis=1
)

df.to_csv("cleaned_loan_risk_data0001.csv", index=False)

print("\nData cleaned successfully!")