import pandas as pd


top_companies = {
    'company': ['Apple', 'Microsoft', 'Amazon', 'Nvidia', 'Google'],
    'share': ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOG'],
    'cost of the share': [211, 510, 225, 172, 186],
    'number of workers': [154_000, 228_000, 1_500_000, 36_000, 182_000],
    'foundation date': ['1976-04-01', '1975-04-04', '1994-07-05', '1993-04-05', '1998-09-04']
}

df = pd.DataFrame(top_companies)
df['foundation date'] = pd.to_datetime(df['foundation date']) #Convertation of 'str' dates into the real dates to work with them properly

df['Country'] = 'USA' #Adding an element
df['cost of the share'] = [212, 509, 220, 175, 185] #Changing the values


capitalization = {
    'Capitalization in billions': [2790, 3500, 1115, 4000, 1870]
}
df2 = pd.DataFrame(capitalization)

main_df = pd.concat([df, df2], axis=1) #Merging two data frames

print(main_df.sort_values('Capitalization in billions', ascending=False)) #Sorting values by capitalization
