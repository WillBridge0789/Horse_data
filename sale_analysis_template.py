"""
    Please write a script to read in the sale results csv file, remove all rows where out is true ('t')
    Using pandas plot method to create the following 4 png files
    - Total sales for the top 10 sires by total sale price
    - Avg sale price for the top 10 buyers by total sale price
    - Avg sale price by book and by sex
    - Avg sale price by month of birth
"""
# Need to install pandas library 
import pandas as pd

# Need to install plotly library 
pd.options.plotting.backend = "plotly"

# File path
# file_path = #Path to the supplied CSV file "keesep_2023_results.csv"
file_path = 'C:\\Users\\WILLIAM BURBRIDGE\\Downloads\\keepsep_2023_results.csv'


# Your code here
# 1. Read in the csv file to pandas dataframe
df = pd.read_csv(file_path)

# 2. Remove outs from the data
df = df[df['out'] != 't']

# 3. Total sale for the top 10 sires by gross sale price
top_10_sires = df.groupby('sire').sum().sort_values(by='price', ascending=False).head(10)
fig1 = top_10_sires['price'].plot.bar(title='Total Sales for the Top 10 Sires by Total Sale Price')

# 4. Avg sale price for top 10 buyers by gross sale price
top_10_buyers = df.groupby('buyer').mean().sort_values(by='price', ascending=False).head(10)
fig2 = top_10_buyers['price'].plot.bar(title='Avg Sale Price for the Top 10 Buyers by Total Sale Price')

# 5. Avg sale price by book by sex
fig3 = df.groupby(['book', 'sex']).mean()['price'].unstack().plot.bar(title='Avg Sale Price by Book and Sex')

# 6. Avg sale price by month of birth
df['month_of_birth'] = pd.to_datetime(df['foal_date']).dt.month
fig4 = df.groupby('month_of_birth').mean()['price'].plot.bar(title='Avg Sale Price by Month of Birth')

