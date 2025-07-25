import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"], index=["x","y","z"])
print("show first 5 rows of table\n")
print(df.head)
print("show information about the dataframe\n")
print(df.info())
print("shows count, mean, std, etc. about a dataframe\n")
print(df.describe())
print("shows how many unique numbers are in every column\n")
print(df.nunique())
print("shows unique values of a filtered column")
print(df['A'].unique())
print("shows the shape of the dataframe (rows, cols)")
print(df.shape)
print("shows the total number of entries in the dataframe")
print(df.size)

## Load from file

print("load data from csv file")
coffee = pd.read_csv("./data/coffee.csv")
print(coffee.head())
#alternatively coffee.head(10)
print("get sample of 10 random entries")
print(coffee.sample(10))

print("load data from parquet")
results = pd.read_parquet("./data/results.parquet")
print(results.head())

bios = pd.read_csv("./data/bios.csv")

print("filter by rows and columns")
print("usage: coffee.loc[#Rows, #Cols]")
print(coffee.loc[[0,1,2]])
print(coffee.loc[0:3])
print(coffee.loc[0:3, ["Day", "Units Sold"]])
print("iloc = loc but with index for columns")
print("usage: coffee.loc[0:3, [\"Day\", \"Units Sold\"]] == coffee.iloc[0:3, [0,2]]")
print("with iloc the upper index of the slice is not inclusive (0:3 means 0,1 and 2 - with loc it also means 3)")
print(coffee.iloc[0:3, [0,2]])

# reset index of dataframe
# coffee.index = coffee.Day // coffee["Day"]
# after that it is possible to do
# coffee.loc["Monday":"Wednesday"]
# but not coffee.loc[0:3] anymore

print("edit value in dataframe:")
coffee.loc[1, "Units Sold"] = 10
print(coffee.head())

print("locate single value (at = loc / iat = iloc)")
print(coffee.at[0, "Units Sold"])
print(coffee.iat[0, 2])
print(coffee.loc[0, "Units Sold"])
print(coffee.iloc[0, 2])

# sorting values
print("sorting values descending by multiple cols")
print(coffee.sort_values(["Units Sold", "Coffee Type"], ascending=False))
#alternatively print(coffee.sort_values(["Units Sold", "Coffee Type"], ascending=[0,1]))

#do not do this! (memory heavy operation! - losing performance bonus of pandas dataframe)
for index, row in coffee.iterrows():
    print(index)
    print(row["Units Sold"])
    print("\n\n\n\n\n")

# 24:15