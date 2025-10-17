import pandas as pd
import matplotlib.pyplot as plt


top_companies = {
    'company': ['Apple', 'Microsoft', 'Amazon', 'Nvidia', 'Google'],
    'share': ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOG'],
    'cost of the share': [211, 510, 225, 172, 186],
    'number of workers': [154_000, 228_000, 1_500_000, 36_000, 182_000],
    'foundation date': ['1976-04-01', '1975-04-04', '1994-07-05', '1993-04-05', '1998-09-04']
}

df = pd.DataFrame(top_companies)

df['Country'] = 'USA' #Adding an element
df['cost of the share'] = [212, 509, 220, 175, 185]


capitalization = {
    'Capitalization in billions': [2790, 3500, 1115, 4000, 1870]
}

w_economy = {'The world economy' : [109_000]}

df2 = pd.DataFrame(capitalization)
df3 = pd.DataFrame(w_economy)

main_df = pd.concat([df, df2, df3], axis=1)



total = main_df['Capitalization in billions'].sum()
mean = main_df['Capitalization in billions'].mean()


#print('Total:', total, 'billion')
#print('Mean:', int(mean), 'billion')

plt.bar(main_df['company'], main_df['Capitalization in billions'], color = ['black', 'red', 'yellow', 'green', 'blue']) #The first is for 'x' axis, giving the names if companies. The second is for 'y' axis, giving the numbers
plt.show() #Creates a bar based on the prompt above
