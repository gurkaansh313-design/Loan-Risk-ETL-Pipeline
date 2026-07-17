Select LoanDecision,
COUNT (*) as Total 
From 'loan-risk-project.loan_analytics.loan_data'
GROUP BY LoanDecision;