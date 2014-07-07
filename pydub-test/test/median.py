import pandas as pd

s = pd.DataFrame([1, 2, 3, 4, 5])

print(s.describe())
print(s.quantile(.25)[0])