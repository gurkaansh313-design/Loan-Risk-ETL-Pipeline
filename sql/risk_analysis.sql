select 
RiskCategory,COUNT (*) AS Total_Customers
from `loan-risk-project.loan_analytics.loan_data`
GROUP BY RiskCategory;