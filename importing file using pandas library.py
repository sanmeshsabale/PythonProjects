# Importing csv file using pandas

import pandas as pd

data=pd.read_csv("em-9EhjTEemU7w7-EFnPcg_7aa34fc018d311e980c2cb6467517117_happyscore_income.csv")
happy=data['happyScore']
income=data['avg_income']
ineq=data['income_inequality']
income.max()
