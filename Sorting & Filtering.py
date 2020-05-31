# sorting and Filtering of dataframe

import numpy as np

data.sort_values("avg_income", inplace=True)
richest=data[data["avg_income"]>15000]

richest.iloc[0]
np.mean(data["avg_income"])
np.mean(richest["avg_income"])
