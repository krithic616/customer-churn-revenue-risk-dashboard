import pandas as pd

df = pd.read_csv("churn_data.csv")

df.dropna(inplace=True)

df["Risk Category"] = df["Churn_Probability"].apply(
    lambda x: "High Risk" if x > 0.7 else ("Medium Risk" if x > 0.4 else "Low Risk")
)

df.to_csv("processed_churn_data.csv", index=False)
