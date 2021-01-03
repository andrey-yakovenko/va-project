import pandas as pd

source_covid = pd.read_csv("us-covid-info-by-state.csv", index_col=0)

print(max(source_covid.cases_total))  # 2208843
print(max(source_covid.deaths_total))  # 37118
