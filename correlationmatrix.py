import pandas as pd

df = pd.read_csv("Advertising.csv")

analysis_df = df[["TV", "Radio", "Newspaper", "Sales"]]

corr =  analysis_df.corr().round(3)

corr.to_csv(
    "Advertisment_correlationMatrix.csv",
    index=True,
    index_label="variable"
)
print(corr)