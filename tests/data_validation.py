import pandas as pd

# Load source file
df = pd.read_csv("cleaned_loan_risk_data0001.csv")

# Test 1: No null credit scores
assert df["CreditScore"].isnull().sum() == 0, \
    "FAIL: Null Credit Scores Found"

# Test 2: No null income
assert df["Income"].isnull().sum() == 0, \
    "FAIL: Null Income Found"

# Test 3: Income should be positive
assert (df["Income"] > 0).all(), \
    "FAIL: Negative Income Found"

print("SOURCE DATA VALIDATION PASSED")