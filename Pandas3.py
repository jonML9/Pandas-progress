import pandas as pd

top_companies = {
    'company': ['Apple', 'Microsoft', 'Amazon', 'Nvidia', 'Google'],
    'share': ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOG'],
    'cost_of_the_shares': [211, 510, 225, 172, 186],
    'number_of_workers': [154_000, 228_000, 1_500_000, 36_000, 182_000]
}

df = pd.DataFrame(top_companies)

print(df['cost_of_shares'].value_counts())
print(df['cost_of_shares'].sort_values(ascending=False)) #I think you know what the ascending means:)
print(df.loc[2]) #Prints the element with the index '2' in 'y' axis
print(df.loc[2:3]) #And here from 2 to 3
print(df.iloc[2, 0:3]) #The same 2nd element, but lines 0 to 3(excluded)




