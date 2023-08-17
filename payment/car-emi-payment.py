import pandas as pd
import numpy as np
car_loan = 10000
interest = 0.07
years = 5
car_payments = np.pmt(rate = interest, nper = years, pv = -car_loan)
loan_table = np.zeros((5,6))
loan_table = pd.DataFrame(loan_table)
loan_table.columns = ["Year", 'Initial_Balance', "Payments", "Interest",
                                "Principal", "Ending_Balance"]
loan_table.iloc[0,0] = 1
loan_table.iloc[0,1] = car_loan
loan_table.iloc[0,2] = car_payments
loan_table.iloc[0,3] = car_loan * interest
loan_table.iloc[0,4] = car_payments - (car_loan * interest)
loan_table.iloc[0,5] = car_loan - (car_payments - (car_loan * interest))
for i in range(1,5):
    loan_table.iloc[i,0] = i + 1
    loan_table.iloc[i,1] = loan_table.iloc[(i-1), 5]
    loan_table.iloc[i,2] = car_payments
    loan_table.iloc[i,3] = loan_table.iloc[i,1] * interest
    loan_table.iloc[i,4] = car_payments - (loan_table.iloc[i,1] * interest)
    loan_table.iloc[i,5] = loan_table.iloc[i,1] - (car_payments - (loan_table.iloc[i,1] * interest))
    
loan_table = loan_table.round(2)
    
with pd.option_context("display.max_rows",None,"display.max_columns", None):
    print(loan_table)