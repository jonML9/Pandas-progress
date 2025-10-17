import pandas as pd

top_companies = {
    'company': ['Apple', 'Microsoft', 'Amazon', 'Nvidia', 'Google'],
    'share': ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOG'],
    'cost of the share': [211, 510, 225, 172, 186],
    'number of workers': [154_000, 228_000, 1_500_000, 36_000, 182_000],
    'foundation date': ['1976-04-01', '1975-04-04', '1994-07-05', '1993-04-05', '1998-09-04']
}

df = pd.DataFrame(top_companies)

df.drop(['foundation date'], axis=1, inplace=True) #Deleting specific column
df.drop([1], axis=0, inplace=True) #Deleting specific row

df.to_csv('top_companies.csv', sep = ';', index=False) #Converting into a csv file. ';' is for Excel to put everything in separate columns

df = pd.read_csv('top_companies.csv') #In order to work further with the created table

print(df)