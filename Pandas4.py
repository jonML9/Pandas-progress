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

#print(df[df['cost_of_the_share'] > 200]) #Finding a company with a cost of shares more than 200
#print(df[(df['cost_of_the_share'] > 200) & (df['number_of_workers'] < 200_000)]) #However, we are sorting companies by 2 given parameters. We should put only '&' symbol, as 'and' is not used in pandas
#print(df[df['cost_of_the_share'].isin([211, 510])]) #Finds given values in DataFrame
#print(df[df['cost_of_the_share'].isin(range(211, 300))])
my_date_range = pd.date_range(start='1994-01-01', end='1995-01-01') #Creating a time frame to work on
print(df[df['foundation date'].isin(my_date_range)]) #Finds companies in the given time frame


