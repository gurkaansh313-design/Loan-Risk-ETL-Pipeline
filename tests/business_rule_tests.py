import pandas as pd

df = pd.read_csv("cleaned_loan_risk_data0001.csv")

# Customers below 600 must be High Risk
high_risk_customers = df[df["CreditScore"] < 600]

assert (
    high_risk_customers["RiskCategory"] == "High Risk"
).all(), "FAIL: Risk Category Logic Incorrect"

print("BUSINESS RULE TEST PASSED")