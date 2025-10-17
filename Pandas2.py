import pandas as pd

top_companies = {
    'companies': ['Apple', 'Microsoft', 'Amazon', 'Nvidia', 'Google'],
    'shares': ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOG'],
    'cost_of shares': [211, 510, 225, 172, 186],
    'number of workers': [154_000, 228_000, 1_500_000, 36_000, 182_000]
}

df = pd.DataFrame(top_companies) #Before using attributes of pandas, we have to convert the data into a dataframe

print(df.columns) #Names of all columns
print(df.select_dtypes(include='object')) #Shows objects
print(df.select_dtypes(exclude='object')) #Shows everything expect for objects
print(df.describe().round(2)) #Gives the min, max values and other types of basic analytical info



